import { Form, FormItem } from "../../../generated";

const AccidentForm = () : Form => {
  return {
    name: "Accident Report",
    fields: [
      {
        fieldName: "Name of Person Involved"
      },
      {
        fieldName: "Date and Time of Accident"
      },
      {
        fieldName: "Location of Accident"
      },
      {
        fieldName: "Cause of Accident"
      },
      {
        fieldName: "Type of Injury"
      },
      {
        fieldName: "Medical Treatment Received"
      },
      {
        fieldName: "Reported by"
      },
      {
        fieldName: "Witnesses Present"
      }
    ] as FormItem[]
  } as Form;
};

export default AccidentForm;