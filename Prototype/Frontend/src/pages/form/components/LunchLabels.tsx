import { FieldType, Form, FormItem } from "../../../generated";

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
        fieldName: "Number of Attendees",
        fieldType: FieldType.NUMERIC,
      },
      {
        fieldName: "Organizer",
        fieldType: FieldType.TEXT,
      },
      {
        fieldName: "Budget",
        fieldType: FieldType.TEXT,
      },
      {
        fieldName: "Date",
        fieldType: FieldType.TEXT,
      },
      {
        fieldName: "Start Time",
        fieldType: FieldType.TEXT,
      },
      {
        fieldName: "End Time",
        fieldType: FieldType.TEXT,
      },
      {
        fieldName: "Location",
        fieldType: FieldType.TEXT,
      },
      {
        fieldName: "Food Diets",
        fieldType: FieldType.TEXT,
      },
      {
        fieldName: "Food Allergies",
        fieldType: FieldType.TEXT,
      },
      {
        fieldName: "Created by Third Party",
        fieldType: FieldType.RADIO_BUTTON,
        params:["yes", "no"]
      },
      {
        fieldName: "Type of Lunch",
        fieldType: FieldType.MULTI_SELECT,
        params:["Seafood", "Meat", "Vegan"]
      }
    ] as FormItem[]
  } as Form;
};

export default LunchLabels;