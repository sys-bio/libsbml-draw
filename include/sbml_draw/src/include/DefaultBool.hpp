/* MIT License
*/

//== BEGINNING OF CODE ===============================================================

#ifndef __SAGITTARIUS_DEFAULT_BOOL_H_
#define __SAGITTARIUS_DEFAULT_BOOL_H_

//== INCLUDES ========================================================================

//==DEFINES/TYPES===================================//

namespace Sagittarius
{
    
    class DefaultFalseBool
    {
        private:
            bool b;
        public:
            DefaultFalseBool() : b(false) {}
            DefaultFalseBool(const DefaultFalseBool& other) : b(other.b) {}
            bool& get() { return b; }
            const bool& get() const { return b; }
    };
    
    class DefaultTrueBool
    {
        private:
            bool b;
        public:
            DefaultTrueBool() : b(true) {}
            DefaultTrueBool(const DefaultTrueBool& other) : b(other.b) {}
            bool& get() { return b; }
            const bool& get() const { return b; }
    };
    
}

#endif
