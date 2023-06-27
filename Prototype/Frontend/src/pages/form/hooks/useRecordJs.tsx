import { useEffect, useState } from "react";
import Recorder from "recorder-js";

type UseRecordJsProps = {
    isRecording: boolean;
    blob: Blob | undefined;
    startRecording: () => void;
    stopRecording: () => void;
}

const UseRecordJs = (): UseRecordJsProps => {
    const [isRecording, setIsRecording] = useState<boolean>(false);
    const [blob, setBlob] = useState<Blob>();
    const [recorder, setRecorder] = useState<Recorder | undefined>(undefined);


    useEffect(() => {
        const audioContext = new AudioContext();
        const recorder = new Recorder(audioContext, {});

        navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
            recorder.init(stream);
        }).catch((error) => {
            console.log(error);
        }
        );

        setRecorder(recorder);
    }
        , []);


    const startRecording = () => {
        recorder!.start().then(() => {
            setIsRecording(true);
        }
        ).catch((error) => {
            console.log(error);
        }
        );
    };

    const stopRecording = () => {
        recorder!.stop().then(({ blob, buffer }) => {
            setBlob(blob);
            setIsRecording(false);
        }
        ).catch((error) => {
            console.log(error);
        }
        );
    };

    return {
        isRecording,
        blob,
        startRecording,
        stopRecording
    } as UseRecordJsProps;

};

export default UseRecordJs;
