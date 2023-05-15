import { useEffect, useState } from "react";
import { DefaultApi, Form } from "../../../generated";
import { ApiConfiguration } from "../../../api/ApiConfiguration";

type UseZenyaFormsProps = {
  forms: { [key: string]: () => Form; };
  arePending: boolean;
  error: string | undefined;
}

const UseZenyaForms = () => {
    const [forms, setForms] = useState<UseZenyaFormsProps["forms"]>({});
    const [arePending, setArePending] = useState<UseZenyaFormsProps["arePending"]>(true);
    const [error, setError] = useState<UseZenyaFormsProps["error"]>(undefined);

    useEffect(() => {
        const api = new DefaultApi(ApiConfiguration);
        api.formsGetAllFormsGet().then((response) => {
            console.log(response.data);
            const newForms = {
                ...forms,
            }
            for (const form of response.data) {
                newForms[form.name] = () => form;
            }
            setForms(newForms);
        }).catch((error) => {
            console.log(error);
            setError(error.message);
        }).finally(() => {
            setArePending(false);
        });
    
    }, []);

    return {
        forms,
        arePending,
        error
    }
}

export default UseZenyaForms;
