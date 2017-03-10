namespace mc
{
    class MyClass
    {
    protected:
        /**
         * @brief This is my value
         */
        int _value;
    public:
        /**
         * @brief Construct a value
         * @param value value to construct
         */
        MyClass(int value);
        /**
         * @brief Destroy a value
         */
        ~MyClass();
    public:
        /**
         * @brief Get my value
         * @return my good self
         */
        int get_value();
        /**
         * @brief Set my value
         * @param your good self
         */
        void set_value(int value);
    };
}
