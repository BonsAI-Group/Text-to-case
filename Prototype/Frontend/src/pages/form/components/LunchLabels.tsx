import { Form, FormItem } from "../../../generated";

const LunchLabels = () : Form => {
  return {
    name: "Lunch",
    fields: [
      {
        fieldName: "Number of Attendees"
      },
      {
        fieldName: "Organizer"
      },
      {
        fieldName: "Budget"
      },
      {
        fieldName: "Date"
      },
      {
        fieldName: "Start Time"
      },
      {
        fieldName: "End Time"
      },
      {
        fieldName: "Location"
      },
      {
        fieldName: "Food Allergies"
      },
      {
        fieldName: "Food Diets"
      }
    ] as FormItem[]
  } as Form;
};

export default LunchLabels;