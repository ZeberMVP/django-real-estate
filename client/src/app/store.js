import { configureStore } from '@reduxjs/toolkit';
import { FaSignInAlt, FaSignOutAlt } from "react-icons/fa";
import propertyReducer from "../features/properties/propertySlice";

export const store = configureStore({
  reducer: {
    properties: propertyReducer,
    auth: authReducer,
  },
});
