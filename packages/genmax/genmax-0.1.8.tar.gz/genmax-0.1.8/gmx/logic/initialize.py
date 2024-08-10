import os

class InitializeLogic:
    def __init__(self) -> None:
        pass

    def initialize_genmax(self):
        project_path = "_gmx"

        data_path = os.path.join(
            project_path,
            "data"
        )
        flows_path = os.path.join(
            project_path,
            "workflows"
        )
        output_path = os.path.join(
            project_path,
            "output"
        )
        templates_path = os.path.join(
            project_path,
            "templates"
        )
        os.makedirs(project_path, exist_ok=True)
        os.makedirs(data_path, exist_ok=True) 
        os.makedirs(flows_path, exist_ok=True)
        os.makedirs(output_path, exist_ok=True)
        os.makedirs(templates_path, exist_ok=True)
        self._add_sample_data(data_path)
        self._add_sample_flow(flows_path)
        self._add_sample_template(templates_path)

    def _add_sample_data(self, data_path: str):
        sample_data_content = """app_name: "SampleWebApp"
entities:
  - name: Organization
        """
        with open(os.path.join(data_path, "sample.yml"), "w") as f:
            f.write(sample_data_content)

    def _add_sample_flow(self, flow_path: str):
        sample_flow_content = """- data: "sample.yml"
  action: "generate"
  template: "sample_template.j2"
  output: "sample>SampleOutput.txt"

- action: "write_to_file"
  template: "sample_text.j2"
  output: "sample>SampleTextFile.txt"

{% for i in range(1, 6) %}
- action: "run_command"
  command: 'echo "Hello {{ i }}"'    
{% endfor %}
        """
        with open(os.path.join(flow_path, "sample.yaml.j2"), "w") as f:
            f.write(sample_flow_content)

    def _add_sample_template(self, template_path: str):
        sample_template_content = """using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Runtime.Serialization;

namespace {{ data.app_name }}.Models;

public class {{data.entity_name}}
{
}"""
        with open(os.path.join(template_path, "sample_template.j2"), "w") as f:
            f.write(sample_template_content)

        sample_text_template_content = """Hello World!"""
        with open(os.path.join(template_path, "sample_text.j2"), "w") as f:
            f.write(sample_text_template_content)