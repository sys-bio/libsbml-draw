/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "error.h"
#include "network.h"

#include <exception>
#include <typeinfo>

namespace LibsbmlDraw {
    
    void indent(std::ostream& os, uint32 ind) {
        for(uint32 i=0; i<ind; ++i)
            os << " ";
    }

}
