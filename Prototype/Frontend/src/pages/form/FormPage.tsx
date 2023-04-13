import { Button, Container, Group, Select, Stack, Textarea, Title } from "@mantine/core"
import { useState } from "react";
import FormComponent from "./components/FormComponent";
import LunchLabels from "./components/LunchLabels";
import SecurityForm from "./components/SecurityForm";
import { DefaultApi, FieldSubmit, Form, FormAnswer } from "../../generated";
import { ApiConfiguration } from "../../api/ApiConfiguration";

/**
 * Page for displaying a form and submitting it.
 * @returns 
 */
const FormPage = () => {

  const [story, setStory] = useState<string | undefined>(undefined);
  const [answers, setAnswers] = useState<FormAnswer>({answers: {}} as FormAnswer);
  const [sending, setSending] = useState<boolean>(false);
  const [error, setError] = useState<string | undefined>(undefined);

  const forms = {
    "Lunch": LunchLabels,
    "Security": SecurityForm
  } as {[key: string]: () => Form};

  const [form, setForm] = useState(forms["Lunch"]());

  const onSubmit = async () => {
    const api = new DefaultApi(ApiConfiguration);
    setSending(true);

    for (const field of form.fields) {
      await api.fieldFieldPost({
        context: story,
        field: field
      } as FieldSubmit).then((response) => {
        const newAnswers = {
          ...answers,
        }
        newAnswers.answers[field.fieldName] = response.data;
        setAnswers(newAnswers);
      }
      ).catch((error) => {
        setError(error.message);
      });
    }
    setSending(false);
  };

  return (
    <Container>
      <Title order={1}>Form</Title>
      <Group grow align="start">
        <Stack>
          <Textarea
            placeholder="Enter your story"
            label="Your story"
            value={story}
            onChange={(event) => setStory(event.currentTarget.value)}
            minRows={10}
            />            
            <Button 
              onClick={() => onSubmit()} 
              disabled={!story} 
              loading={sending} 
              color={error ? "red" : "blue"} 
              >
              {error ? "Error: " + error : 
                sending ? "Sending" :
                  "Submit"}
            </Button>
        </Stack>
        <Stack>
          <Select
            label="Form"
            data={Object.keys(forms)}
            value={form.name}
            onChange={(event) => {
              setForm(forms[event!]);
            }
            }
          />
          <FormComponent form={form} answers={answers} />
        </Stack>
        
      </Group>

    </Container>
  );
};

export default FormPage;