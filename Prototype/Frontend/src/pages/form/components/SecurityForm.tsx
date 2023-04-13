import { Form, FormItem } from "../../../generated";

const SecurityForm = () : Form => {
  return {
    name: "Security",
    fields: [
      {
        fieldName: "Reported by third party?"
      },
      {
        fieldName: "Date"
      },
      {
        fieldName: "Time"
      },
      {
        fieldName: "Kind of incident"
      },
      {
        fieldName: "Priority"
      },
      {
        fieldName: "Personal data involved"
      }
    ] as FormItem[]
  } as Form;
}

export default SecurityForm;