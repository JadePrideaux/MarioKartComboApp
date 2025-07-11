type Props = {
  message: string;
};

const ErrorMessage = ({ message }: Props) => {
  return <p className="text-red-500">{message}</p>;
};

export default ErrorMessage;
