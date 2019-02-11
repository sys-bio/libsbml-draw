/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

//== INCLUDES ========================================================================

//- GENERAL -//
#include <sstream>

//- SPECIFIC -//
#include "SagittariusException.hpp"

namespace LibsbmlDraw
{
    //== CLASS METHODS ===============================================================
    
    //## CLASS Exception #############################################################
    Exception::Exception( const int type, const String& desc, const String& origin, const char* name, const char* file, const long line)
            : m_type( type ), m_desc( desc ), m_origin( origin ), m_name(name), m_file( file ), m_line( line ) {}
        //note: logging the exception (like Ogre) is probably a bad idea (assuming the log function
        //itself can throw exceptions).  We try to log the exception, then the log function throws
        //another exception.  We try to log that exception, and the cycle repeats ad infinitum.
        //We could declare the logging function with const throw, preventing it from throwing exceptions, but
        //then we must come up with another error handling mechanism.  All in all, I don't think
        //it's worth it.
    
    void Exception::operator = ( const Exception &rval )
    {
        m_type   = rval.m_type;
        m_desc   = rval.m_desc;
        m_origin = rval.m_origin;
        m_name   = rval.m_name;
        m_file   = rval.m_file;
        m_line   = rval.m_line;
    }
    
    String Exception::getReport() const
    {
        String report;
        std::stringstream s;
        s << m_line;
        String linestr;
        s >> linestr;
        
        report  = "EXCEPTION: ";
        report += m_name;
        report += " in ";
        report += m_origin;
        report += " (file: ";
        report += m_file;
        report += ", line: ";
        report += linestr;
        report += "):";
        report += "    ";
        report += m_desc;
        report += "\n";
        return report;
    }
    
    int Exception::getType() const throw()
    {
        return m_type;
    }
} //namespace
