import { Button, Container, Group, Stack, Textarea, Title } from "@mantine/core"
import { useState } from "react";
import FormComponent from "./components/FormComponent";
import LunchForm from "./components/LunchForm";
import { DefaultApi, FormAnswer, FormSubmit } from "../../generated";
import { ApiConfiguration } from "../../api/ApiConfiguration";

/**
 * Page for displaying a form and submitting it.
 * @returns 
 */
const FormPage = () => {

  const [story, setStory] = useState<string | undefined>(undefined);
  const [answers, setAnswers] = useState<FormAnswer | undefined>(undefined);
  const [sending, setSending] = useState<boolean>(false);
  const [error, setError] = useState<string | undefined>(undefined);

  const onSubmit = () => {
    const api = new DefaultApi(ApiConfiguration);
    setSending(true);
    api.formsFormsPost({
      context: story,
      form: LunchForm()
    } as FormSubmit).then((response) => {
      setSending(false);
      setAnswers(response.data);
      setError(undefined);
    }).catch((error) => {
      setSending(false);
      setError(error.message);
    });
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
        <FormComponent form={LunchForm()} answers={answers} />
      </Group>

    </Container>
  );
};

export default FormPage;