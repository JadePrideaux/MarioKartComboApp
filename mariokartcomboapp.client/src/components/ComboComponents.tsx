interface ComboComponents {
  mkComponents: {
    [key: string]: {
      name: string;
      type: string;
      imgURL?: string | null;
    };
  };
}

type Props = {
  mkComponents: ComboComponents["mkComponents"];
};

const ComboComponents = (props: Props) => {
  return (
    <>
      <h2>Components:</h2>
      <ul>
        {Object.entries(props.mkComponents).map(([key, component]) => (
          <li key={key}>
            <b>{component.type}</b>: {component.name}
            {/*If there is an imgURL, render the image*/}
            {component.imgURL && (
              <div>
                <img
                  src={component.imgURL}
                  alt={component.name}
                  style={{ width: "100px", height: "auto" }}
                />
              </div>
            )}
          </li>
        ))}
      </ul>
    </>
  );
};

export default ComboComponents;
