import { Button, Loader } from "@mantine/core";
import { useEffect, useState } from "react";
import { Microphone, PlayerStop, Tex } from "tabler-icons-react";
import useRecorder from "../../hooks/useRecorder";
import { FormAnswer, Form, DefaultApi, FieldSubmit, FormItem, AudioSubmit } from "../../../../generated";
import { ApiConfiguration } from "../../../../api/ApiConfiguration";

type RecorderProps = {
    form: Form;
    setAnswers: (answers: FormAnswer) => void;
    answers: FormAnswer;
}

const RecorderInput = ({ form }: RecorderProps) => {
    const { isRecording, audioUrl, startRecording, stopRecording } = useRecorder();

    const [error, setError] = useState<string | undefined>(undefined);
    const [sending, setSending] = useState<boolean>(false);

    const onSubmit = async () => {
        const api = new DefaultApi(ApiConfiguration);
        setSending(true);
        const audioFileWav = await fetch(audioUrl!).then((response) => response.blob());
        const audioFile = new File([audioFileWav], "audio.wav", { type: "audio/wav" });
        const formData = new FormData();
        formData.append("audioFile", audioFile);
        formData.append("formName", form.name);


        for (const field of form.fields!) {
            formData.append("field", JSON.stringify(field));
            // send post form to localhost:8000/speech
            // fetch("http://localhost:8000/speech", {
            //     method: "POST",
            //     body: formData
            // }).then((response) => {
            //     console.log(response);
            // }).catch((error) => {
            //     console.log(error);
            // });
            api.convertSpeechToTextSpeechPost(
                audioFile, JSON.stringify(field), form.name
            ).then((response) => {
                console.log(response);
            }).catch((error) => {
                console.log(error);
            });
            // api.testFileTestFilePost(audioFile).then((response) => {
            //     console.log(response);
            // }
            // ).catch((error) => {
            //     console.log(error);
            // }
            // );
        }
        setSending(false);
    };

    useEffect(() => {
        if (audioUrl) {
            onSubmit();
        }
    }
        , [audioUrl]);

    return (
        <div style={{ display: "grid", placeItems: "center", height: "330px", border: "1px solid #ccc", borderRadius: "5px", padding: "10px" }}>
            <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
                {sending ? <Loader size={50} /> :
                    <Button onClick={isRecording ? stopRecording : startRecording} style={{ borderRadius: "50%", height: "50px", width: "50px", border: `3px solid ${error ? "red" : "black"}`, background: "transparent" }} p={0}>

                        {isRecording ? <Loader variant="bars" color="red" size={24} /> : <Microphone color="black" size={24} />}
                    </Button>
                }
                {error && <p style={{ color: "red" }}>{error}</p>}
            </div>
        </div>
    );
};

export default RecorderInput;
