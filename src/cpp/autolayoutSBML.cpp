/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "autolayoutSBML.h"
#include "error.h"

#include "sbml/SBMLTypes.h"
#include <sstream>

void gf_freeSBMLModel(gf_SBMLModel* lo) {
    if(!lo)
        AN(0, "Not a valid layout pointer"); //null
    SBMLDocument* doc = (SBMLDocument*)lo->pdoc;
    delete doc;
    free(lo);
}

extern "C" gf_SBMLModel* gf_loadSBMLbuf(const char* buf) {
    gf_SBMLModel* r=(gf_SBMLModel*)malloc(sizeof(gf_SBMLModel));
    SBMLReader reader;
    SBMLDocument* doc = reader.readSBMLFromString(buf);
    bool success;

 //   if(doc->getLevel() == 2) {
 //       success = doc->setLevelAndVersion(3, 1);

 //       if (!success) {
 //           std::cerr << "Unable to perform conversion due to the following:" << std::endl;
 //           doc->printErrors(std::cerr);    
 //           std::cout << std::endl;
 //           std::cout << "Conversion skipped.  Either libSBML does not (yet)" << std::endl
 //           << "have the ability to convert this model or (automatic)" << std::endl
 //           << "conversion is not possible in this case." << std::endl;

 //           // delete doc;
 //           return NULL;    
 //       }
	//}

    AN(doc, "Failed to parse SBML"); //not libSBML's documented way of failing, but just in case...
    
    if(doc->getNumErrors()) {
        #if SAGITTARIUS_DEBUG_LEVEL >= 2
        fprintf(stderr, "Failed to parse SBML\n");
        for(unsigned int i=0; i<doc->getNumErrors(); ++i) {
            std::cerr << "Error " << i << ": " <<doc->getError(i)->getMessage() << "\n";
        }
        std::stringstream ss;
        ss << "Failed to parse SBML\n";
        for(unsigned int i=0; i<doc->getNumErrors(); ++i) {
            ss << "Error " << i << ": " <<doc->getError(i)->getMessage() << "\n";
        }
        gf_setError(ss.str().c_str());
        #endif
        // if all are warnings, continue - else abort
        for(unsigned int i=0; i<doc->getNumErrors(); ++i) {
          if (!doc->getError(i)->isWarning())
            return NULL;
        }
    }
    
    r->pdoc = doc;
    return r;
}

extern "C" gf_SBMLModel* gf_loadSBMLfile(const char* path) {
  char* buf;
  size_t size=0;
  FILE* file=NULL;
  size_t bytes_read;

  try {

    file = fopen(path, "rb");
    if(!file)
      SBNW_THROW(LibsbmlDraw::InternalCheckFailureException, "Failed to open file", "gf_loadSBMLfile");

    //get t3h s!z3
    fseek(file, 0, SEEK_END);
    size = ftell(file);
    rewind(file);
    #if SAGITTARIUS_DEBUG_LEVEL >= 2
  //     fprintf(stderr, "File size is %lu\n", size);
    #endif
    assert(size > 0);

    //allocated buffer
    if (sizeof(char) != 1)
      SBNW_THROW(LibsbmlDraw::InternalCheckFailureException, "char must be one byte wide", "gf_loadSBMLfile");
    buf=(char*)malloc(size+1); //one extra byte for null char
    if (!buf)
      SBNW_THROW(LibsbmlDraw::InternalCheckFailureException, "Failed to allocate buffer", "gf_loadSBMLfile");
    //read the whole file at once
    bytes_read = fread(buf, 1, size, file);
    if (bytes_read != size)
      SBNW_THROW(LibsbmlDraw::InternalCheckFailureException, "Failed to read whole file (wrong size specified?)", "gf_loadSBMLfile");
    //trip EOF indicator
    fgetc(file);
    if (!feof(file))
      SBNW_THROW(LibsbmlDraw::InternalCheckFailureException, "EOF Expected", "gf_loadSBMLfile");
    buf[size] = '\0'; //terminating null char

    /*close*/
    fclose(file);

    gf_SBMLModel* mod = gf_loadSBMLbuf(buf);

    free(buf);

    return mod;

  } catch (const LibsbmlDraw::Exception& e) {
    gf_setError( e.getReport().c_str() );
    return NULL;
  }
}


