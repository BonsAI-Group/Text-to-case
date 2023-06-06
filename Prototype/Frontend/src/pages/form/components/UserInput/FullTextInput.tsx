import { Textarea, Button, Stack } from "@mantine/core";
import { useState } from "react";
import { ApiConfiguration } from "../../../../api/ApiConfiguration";
import { DefaultApi, FieldSubmit, Form, FormAnswer } from "../../../../generated";

type FullTextInputProps = {
    form: Form;
    setAnswers: (answers: FormAnswer) => void;
    answers: FormAnswer;
}

const FullTextInput = ( { form, setAnswers, answers }: FullTextInputProps ) => {
    const [error, setError] = useState<string | undefined>(undefined);
    const [story, setStory] = useState<string | undefined>(undefined);
    const [sending, setSending] = useState<boolean>(false);
    const onSubmit = async () => {
        const api = new DefaultApi(ApiConfiguration);
        setSending(true);
    
        for (const field of form.fields) {
          await api.fieldSubmitFieldPost({
            context: story,
            field: field,
            formName: form.name
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
          loading={sending} 
          color={error ? "red" : "blue"} 
          >
          {error ? "Error: " + error : 
            sending ? "Sending" :
              "Submit"}
        </Button>
        </Stack> 
      )
}

export default FullTextInput;
