import { Group, Text } from "@mantine/core";

const ConfidenceBubble = ({confidence} : {confidence: number}) : JSX.Element => {
  return (
    <Group spacing={3}>
      <div
        style={{
          width: "10px",
          height: "10px",
          borderRadius: "100%",
          backgroundColor: borderColor(confidence),
          display: "inline-block",
        }}
      />
      <Text fz={"xs"}>{(confidence*100).toFixed(1)}%</Text>
    </Group>
  );
};

/** 
 * Returns a border color based on the confidence of the answer.
 * @param confidence The confidence of the answer. Should be between 0 and 1.
 * @returns  A CSS hsl color string fading from red to orange to yellow to green.
 */
const borderColor = (confidence: number) : string => {
  const hue = confidence * 0.4 * 360;
  const saturation = 90;
  const lightness = 50;
  return `hsl(${hue}, ${saturation}%, ${lightness}%)`;
};

export default ConfidenceBubble;