import { Container, Group, Select, Stack, Title } from "@mantine/core"
import { useState } from "react";
import FormComponent from "./components/FormComponent";
import LunchLabels from "./components/LunchLabels";
import SecurityForm from "./components/SecurityForm";
import { Form, FormAnswer } from "../../generated";
import UseZenyaForms from "./components/UseZenyaForms";
import UserInput from "./components/UserInput/UserInput";

/**
 * Page for displaying a form and submitting it.
 * @returns 
 */
const FormPage = () => {
  const [answers, setAnswers] = useState<FormAnswer>({ answers: {} } as FormAnswer);

  const { forms: zenyaForms, arePending } = UseZenyaForms();

  const forms = {
    "Lunch": LunchLabels,
    "Security": SecurityForm,
    ...zenyaForms
  } as { [key: string]: () => Form };

  const [form, setForm] = useState(forms["Lunch"]());

  return (
    <Container>
      <Title order={1}>Form</Title>
      <Group grow align="start">
        <UserInput answers={answers} setAnswers={setAnswers} form={form} />
        <Stack>
          <Select
            label="Form"
            data={Object.keys(forms)}
            value={arePending ? "Loading..." : form.name}
            disabled={arePending}
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