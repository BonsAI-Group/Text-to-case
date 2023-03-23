import { Form, FormItem } from "../../../generated";

const LunchForm = () : Form => {
  return {
    name: "Lunch",
    fields: [
      {
        fieldName: "How many people are coming?"
      },
      {
        fieldName: "Who is the organizer?"
      },
      {
        fieldName: "What is the budget?"
      },
      {
        fieldName: "What is the date?"
      },
      {
        fieldName: "What is the start time?"
      },
      {
        fieldName: "What is the end time?"
      },
      {
        fieldName: "Where will the lunch take place?"
      },
      {
        fieldName: "What allergies/diets do we need to take into account?"
      }
    ] as FormItem[]
  } as Form;
};

export default LunchForm;