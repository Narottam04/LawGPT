import { useState } from "react";

const Accordion = ({ title, children }) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center focus:outline-none mt-2"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="flex-shrink-0 w-6 h-6 text-blue-500"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M12 4v16m8-8H4"
          />
        </svg>

        <h1 className="mx-4 text-lg text-left text-black">{title}</h1>
      </button>

      {isOpen && (
        <div className="flex mt-8 ">
          <span className="border border-gray-500"></span>
          <p className="max-w-3xl px-4 text-gray-800">{children}</p>
        </div>
      )}
      <hr className="my-4 border-gray-700" />
    </div>
  );
};

export default Accordion;
