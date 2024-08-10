from pydantic import Field, BaseModel
from functools import partial
from ezllmaw.parser import PydanticLLMJsonParser
import ezllmaw as ez

def _Field(desc=None, prefix="", field_type="", require=True, default="", format_instructions=None, format=None):
    json_schema_extra = {}
    json_schema_extra["field_type"] = field_type
    json_schema_extra["prefix"] = prefix
    json_schema_extra["format"] = format
    json_schema_extra["format_instructions"] = format_instructions
    return Field(required=require, description=desc,json_schema_extra=json_schema_extra, default=default)

InputField = partial(_Field, field_type="input")
OutputField = partial(_Field, field_type="output", require=True)

class Agent(BaseModel):
    
    def __call__(self, **kwargs):
        self.update_attributes(**kwargs)
        return self.forward(**kwargs)

    def update_attributes(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @property
    def as_prompt(self):
        prompt = f"""{self.__doc__.strip().replace("    ", "")}\n\n"""
        model_fields = self.model_fields
        model_dict = self.model_dump()
        for k, v in model_dict.items():
            json_schema_extra = model_fields[k].json_schema_extra
            is_fmt_json = json_schema_extra["format"] == "json"
            is_fmt_instruction = json_schema_extra["format_instructions"] is not None
            if is_fmt_instruction & is_fmt_json:
                if json_schema_extra["field_type"] == "input":
                    prompt += "Extract a JSON schema:\n\n```json\n"
                if json_schema_extra["field_type"] == "output":
                    prompt += "Return a JSON in the following code block format:\n\n```json\n"
                prompt += f"""{json_schema_extra["format_instructions"]}"""
                prompt += "\n```\n"
            
            prompt += f"""{k}: \n\n{v}\n\n"""
        return prompt
    
    def _set_output(self, output):
        """Limitation: One agent must have only one output field"""
        model_fields = self.model_fields
        model_dict = self.model_dump()
        for k, v in model_dict.items():
            json_schema_extra = model_fields[k].json_schema_extra
            if json_schema_extra["field_type"] == "output":
                setattr(self, k, output)

    def log(self, **kwargs):
        pass

    # @property
    def forward(self, **kwargs):
        self.log(**kwargs)
        try:
            response = ez.settings.lm(self.as_prompt)
        except TypeError as e:
            raise TypeError(f"""{e}. Set your language model first: ez.configure(lm=<your-lm>)""")
        self._set_output(response)
        return self

    def as_pydantic(self, pydantic_obj):
        model_fields = self.model_fields
        model_dict = self.model_dump()
        for k, v in model_dict.items():
            json_schema_extra = model_fields[k].json_schema_extra
            if json_schema_extra["field_type"] == "output":
                output = getattr(self, k)
        json_format = PydanticLLMJsonParser()(output)
        return pydantic_obj(**json_format)

class Program:
    def __call__(self, state):
        return self.forward(state)
    def forward(self, state):
        pass