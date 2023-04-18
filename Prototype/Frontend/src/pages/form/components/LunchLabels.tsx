import { Form, FormItem } from "../../../generated";

const LunchLabels = () : Form => {
  return {
    name: "Lunch",
    fields: [
      // {
      //   fieldName: "Number of Attendees",
      //   formType: "Normal"
      // },
      // {
      //   fieldName: "Organizer",
      //   formType: "Normal"
      // },
      // {
      //   fieldName: "Budget",
      //   formType: "Normal"
      // },
      // {
      //   fieldName: "Date",
      //   formType: "Normal"
      // },
      // {
      //   fieldName: "Start Time",
      //   formType: "Normal"
      // },
      // {
      //   fieldName: "End Time",
      //   formType: "Normal"
      // },
      // {
      //   fieldName: "Location",
      //   formType: "Normal"
      // },
      // {
      //   fieldName: "Food Allergies",
      //   formType: "Normal"
      // },
      {
        fieldName: "Food Diets",
        formType: "Normal"
      },
      {
        fieldName: "Created by Third Party",
        formType: "RadioButton",
        params:["yes", "no"]
      },
      {
        fieldName: "Type of Lunch",
        formType: "MultiChoice",
        params:["Seafood", "Meat", "Vegan"]
      }
    ] as FormItem[]
  } as Form;
};

export default LunchLabels;