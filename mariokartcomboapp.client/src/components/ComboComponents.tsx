import styles from "../styles/ComboComponents.module.css";

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
      <div className={styles.componentsContainer}>
        {Object.entries(props.mkComponents).map(([key, component]) => (
          <div key={key} className={styles.componentCard}>
            <span className={styles.componentType}>{component.type}</span>
            {component.imgURL && (
              <div>
                <img
                  src={component.imgURL}
                  alt={component.name}
                  className={styles.componentImage}
                />
              </div>
            )}
            <span className={styles.componentName}>{component.name}</span>
            {/*If there is an imgURL, render the image*/}
          </div>
        ))}
      </div>
    </>
  );
};

export default ComboComponents;
