import { CloseButton, Group, MultiSelect, Text } from "@mantine/core";
import { FieldAnswer, FormItem } from "../../../generated";
import { forwardRef, useEffect, useState } from "react";
import ConfidenceBubble from "./ConfidenceBubble";
import { hover } from "@testing-library/user-event/dist/hover";

type MultiSelectFieldProps = {
  formItem: FormItem;
  answer?: FieldAnswer;
  showConfidence?: boolean;
};

const MultiSelectField = ({ formItem, answer, showConfidence }: MultiSelectFieldProps): JSX.Element => {
  const [selected, setSelected] = useState<string[]>([]);

  const findIndex = (value: string) => {
    return formItem.params!.findIndex((param) => param === value);
  };

  useEffect(() => {
    if (answer) {
      let selected = []
      for (let i = 0; i < answer.answer.length; i++) {
        if (answer.isTrusted[i]) selected.push(answer.answer[i])
      }
      setSelected(selected);
    }
  }, [answer]);

  /**
   * A component for each item in the selected list.
   */
  const SelectedComponent = (value: any) => {
    const index = findIndex(value.label);
    return (
      <div style={{
        backgroundColor: "#f0f0f0",
        padding: "2px 4px",
        borderRadius: "4px",
        marginRight: "4px",
        marginTop: "4px",
        marginBottom: "4px",
        border: answer && showConfidence ? `2px solid ${borderColor(answer ? answer.confidence[index] : 0)}` : "none"
      }}
      >
        <Group spacing={"xs"}>
          <Text fz={"sm"}>{value.label}</Text>
          {answer && showConfidence ? <ConfidenceBubble confidence={answer ? answer.confidence[index] : 0} /> : null}
          <CloseButton size="xs" onClick={() => {
            setSelected(selected.filter((item) => item !== value.label));
          }
          } />
        </Group>

      </div>
    )
  }

  /**
   * A component for each item in the dropdown menu.
   */
  const ItemComponent = forwardRef<HTMLDivElement, any>((props, ref) => {
    const index = findIndex(props.label);
    const [hover, setHover] = useState(false);
    return (
      <div ref={ref} style={{
        backgroundColor: hover ? "#f0f0f0" : "#ffffff",
        padding: "4px",
        margin: "2px",
        borderRadius: "4px",
        border: answer && showConfidence ? `2px solid ${borderColor(answer ? answer.confidence[index] : 0)}` : "none"
      }}
        onClick={() => {
          setSelected([...selected, props.label]);
        }}
        onMouseEnter={() => setHover(true)}
        onMouseLeave={() => setHover(false)}
      >
        <Group spacing={"xs"}>
          <Text fz={"sm"}>{props.label}</Text>
          {answer && showConfidence ?
            <ConfidenceBubble confidence={answer ? answer.confidence[index] : 0} />
            : null
          }
        </Group>
      </div>
    )
  }
  )


  return (
    <MultiSelect data={formItem.params!}
      label={formItem.fieldName}
      value={selected}
      onChange={setSelected}
      valueComponent={SelectedComponent}
      itemComponent={ItemComponent}
      filter={(value, selected, item) =>
        !selected && item.toLowerCase().startsWith(value.toLowerCase())
      }
    />
  );
};

/** 
 * Returns a border color based on the confidence of the answer.
 * @param confidence The confidence of the answer. Should be between 0 and 1.
 * @returns  A CSS hsl color string fading from red to orange to yellow to green.
 */
const borderColor = (confidence: number): string => {
  const hue = confidence * 0.4 * 360;
  const saturation = 90;
  const lightness = 50;
  return `hsl(${hue}, ${saturation}%, ${lightness}%)`;
};

export default MultiSelectField;