import { FieldType, Form, FormItem } from "../../../generated";

const LunchLabels = () : Form => {
  return {
    name: "Lunch",
    fields: [
      {
        fieldName: "Number of Attendees",
        fieldType: FieldType.TEXT,
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
        fieldType: FieldType.DATE,
      },
      {
        fieldName: "Start Time",
        fieldType: FieldType.TIME,
      },
      {
        fieldName: "End Time",
        fieldType: FieldType.TIME,
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