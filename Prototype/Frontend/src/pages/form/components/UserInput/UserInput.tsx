import { Stack, Switch } from "@mantine/core"
import { useState } from "react";
import { Form, FormAnswer } from "../../../../generated";
import FullTextInput from "./FullTextInput";
import RecorderInput from "./RecorderInput";

type SubmitFieldProps = {
    answers: FormAnswer;
    setAnswers: (answers: FormAnswer) => void;
    form: Form;
}

const UserInput = ( { answers, setAnswers, form }: SubmitFieldProps ) => {

    
    

    const [useRecorder, setUseRecorder] = useState<boolean>(false);

    
    
    return (
      <Stack> 
        <Switch label="Use recorder" checked={useRecorder} onChange={() => setUseRecorder(!useRecorder)} />
        {!useRecorder ?
        <FullTextInput form={form} setAnswers={setAnswers} answers={answers} />
        :
        <RecorderInput form={form} setAnswers={setAnswers} answers={answers} />
        }
        
    </Stack>
    );
};

export default UserInput;