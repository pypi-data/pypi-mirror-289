#include <typeinfo>

#include <snde/metadata.hpp>
#include "snde/recmath_parameter.hpp"
#include "snde/recmath.hpp"
#include "snde/recstore.hpp"
#include "snde/quaternion.h"

namespace snde {

  math_parameter::math_parameter(unsigned paramtype) :
    paramtype(paramtype)
  {

  }

  std::string math_parameter::get_string(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index)
  {
    throw math_parameter_mismatch("Cannot get string value from parameter of class %s for parameter %d of %s",(char *)typeid(*this).name(),parameter_index,fcn_def->definition_command.c_str()); 
  }
  
  int64_t math_parameter::get_int(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index)
  {
    throw math_parameter_mismatch("Cannot get integer value from parameter of class %s for parameter %d of %s",(char *)typeid(*this).name(),parameter_index,fcn_def->definition_command.c_str()); 
    
  }

  uint64_t math_parameter::get_unsigned(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index)
  {
    throw math_parameter_mismatch("Cannot get unsigned integer value from parameter of class %s for parameter %d of %s",(char *)typeid(*this).name(),parameter_index,fcn_def->definition_command.c_str()); 
    
  }

  double math_parameter::get_double(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index)
  {
    throw math_parameter_mismatch("Cannot get double value from parameter of class %s for parameter %d of %s",(char *)typeid(*this).name(),parameter_index,fcn_def->definition_command.c_str()); 

  }

  snde_bool math_parameter::get_bool(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index)
  {
    throw math_parameter_mismatch("Cannot get bool value from parameter of class %s for parameter %d of %s",(char *)typeid(*this).name(),parameter_index,fcn_def->definition_command.c_str()); 
    
  }
  
  snde_coord3 math_parameter::get_vector(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index)
  {
    throw math_parameter_mismatch("Cannot get vector value from parameter of class %s for parameter %d of %s",(char *)typeid(*this).name(),parameter_index,fcn_def->definition_command.c_str()); 

  }

  snde_orientation3 math_parameter::get_orientation(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index)
  {
    throw math_parameter_mismatch("Cannot get vector value from parameter of class %s for parameter %d of %s",(char *)typeid(*this).name(),parameter_index,fcn_def->definition_command.c_str()); 

  }

  std::vector<snde_index> math_parameter::get_indexvec(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index)
  {
    throw math_parameter_mismatch("Cannot get index vector value from parameter of class %s for parameter %d of %s",(char *)typeid(*this).name(),parameter_index,fcn_def->definition_command.c_str()); 

  }

  std::shared_ptr<constructible_metadata> math_parameter::get_metadata(std::shared_ptr<recording_set_state> rss, const std::string& channel_path_context, const std::shared_ptr<math_definition>& fcn_def, size_t parameter_index)
  {
    throw math_parameter_mismatch("Cannot get metadata value from parameter of class %s for parameter %d of %s", (char*)typeid(*this).name(), parameter_index, fcn_def->definition_command.c_str());

  }
  
  std::shared_ptr<recording_base> math_parameter::get_recording(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index) // should only return ready recordings
  {
    throw math_parameter_mismatch("Cannot get recording value from parameter of class %s for parameter %d of %s",(char *)typeid(*this).name(),parameter_index,fcn_def->definition_command.c_str()); 

  }

  std::shared_ptr<ndarray_recording_ref> math_parameter::get_ndarray_recording_ref(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index) // should only return ready recordings. parameter_index starting at 1, just for printing messages
  {
    throw math_parameter_mismatch("Cannot get recording value from parameter of class %s for parameter %d of %s",(char *)typeid(*this).name(),parameter_index,fcn_def->definition_command.c_str()); 

  }
  
  std::set<std::string> math_parameter::get_prerequisites(/*std::shared_ptr<recording_set_state> rss,*/ const std::string &channel_path_context) // obtain immediate dependencies of this parameter (absolute path channel names); typically only the recording
  {
    return std::set<std::string>(); // default to no prerequisites
  }


  math_parameter_string_const::math_parameter_string_const(std::string string_constant) :
    math_parameter(SNDE_MFPT_STR),
    string_constant(string_constant)
  {

  }


  std::string math_parameter_string_const::get_string(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index)
  // parameter_index human interpreted parameter number, starting at 1, for error messages only
  {
    return string_constant;
  }

  bool math_parameter_string_const::operator==(const math_parameter &ref) // used for comparing parameters to instantiated_math_functions
  {
    const math_parameter_string_const *sref = dynamic_cast<const math_parameter_string_const *>(&ref);

    if (!sref) {
      return false;
    }

    return string_constant == sref->string_constant;

  }
  
  bool math_parameter_string_const::operator!=(const math_parameter &ref)
  {
    return !(*this==ref);
  }


  

  math_parameter_int_const::math_parameter_int_const(int64_t int_constant) :
    math_parameter(SNDE_MFPT_INT),
    int_constant(int_constant)
  {

  }
  
  int64_t math_parameter_int_const::get_int(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index)
  // parameter_index human interpreted parameter number, starting at 1, for error messages only
  {
    return int_constant;
  }
  
  bool math_parameter_int_const::operator==(const math_parameter &ref) // used for comparing parameters to instantiated_math_functions
  {
    const math_parameter_int_const *iref = dynamic_cast<const math_parameter_int_const *>(&ref);

    if (!iref) {
      return false;
    }

    return int_constant == iref->int_constant;

  }
  
  bool math_parameter_int_const::operator!=(const math_parameter &ref)
  {
    return !(*this==ref);
  }

  


  math_parameter_unsigned_const::math_parameter_unsigned_const(uint64_t unsigned_constant) :
    math_parameter(SNDE_MFPT_INT),
    unsigned_constant(unsigned_constant)
  {

  }
  
  uint64_t math_parameter_unsigned_const::get_unsigned(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index)
  // parameter_index human interpreted parameter number, starting at 1, for error messages only
  {
    return unsigned_constant;
  }
  
  bool math_parameter_unsigned_const::operator==(const math_parameter &ref) // used for comparing parameters to instantiated_math_functions
  {
    const math_parameter_unsigned_const *uref = dynamic_cast<const math_parameter_unsigned_const *>(&ref);

    if (!uref) {
      return false;
    }

    return unsigned_constant == uref->unsigned_constant;

  }
  
  bool math_parameter_unsigned_const::operator!=(const math_parameter &ref)
  {
    return !(*this==ref);
  }






  math_parameter_sndeindex_const::math_parameter_sndeindex_const(snde_index index_constant) :
    math_parameter(SNDE_MFPT_INT),
    index_constant(index_constant)
  {

  }

  snde_index math_parameter_sndeindex_const::get_unsigned(std::shared_ptr<recording_set_state> rss, const std::string& channel_path_context, const std::shared_ptr<math_definition>& fcn_def, size_t parameter_index)
    // parameter_index human interpreted parameter number, starting at 1, for error messages only
  {
    return index_constant;
  }

  bool math_parameter_sndeindex_const::operator==(const math_parameter& ref) // used for comparing parameters to instantiated_math_functions
  {
    const math_parameter_sndeindex_const* uref = dynamic_cast<const math_parameter_sndeindex_const*>(&ref);

    if (!uref) {
      return false;
    }

    return index_constant == uref->index_constant;

  }

  bool math_parameter_sndeindex_const::operator!=(const math_parameter& ref)
  {
    return !(*this == ref);
  }

  




  
  math_parameter_double_const::math_parameter_double_const(double double_constant) :
    math_parameter(SNDE_MFPT_DBL),
    double_constant(double_constant)
  {

  }

  double math_parameter_double_const::get_double(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index)
  // parameter_index human interpreted parameter number, starting at 1, for error messages only
  {
    return double_constant;
  }


  bool math_parameter_double_const::operator==(const math_parameter &ref) // used for comparing parameters to instantiated_math_functions
  {
    const math_parameter_double_const *dref = dynamic_cast<const math_parameter_double_const *>(&ref);

    if (!dref) {
      return false;
    }
    
    return double_constant == dref->double_constant;

  }
  
  bool math_parameter_double_const::operator!=(const math_parameter &ref)
  {
    return !(*this==ref);
  }




  
  math_parameter_bool_const::math_parameter_bool_const(snde_bool bool_constant) :
    math_parameter(SNDE_MFPT_BOOL),
    bool_constant(bool_constant)
  {

  }

  snde_bool math_parameter_bool_const::get_bool(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index)
  // parameter_index human interpreted parameter number, starting at 1, for error messages only
  {
    return bool_constant;
  }


  bool math_parameter_bool_const::operator==(const math_parameter &ref) // used for comparing parameters to instantiated_math_functions
  {
    const math_parameter_bool_const *bref = dynamic_cast<const math_parameter_bool_const *>(&ref);
    
    if (!bref) {
      return false;
    }
    
    return ((bool)bool_constant) == ((bool)bref->bool_constant);
    
  }
  
  bool math_parameter_bool_const::operator!=(const math_parameter &ref)
  {
    return !(*this==ref);
  }


  
  math_parameter_vector_const::math_parameter_vector_const(snde_coord3 vector_constant) :
    math_parameter(SNDE_MFPT_VECTOR),
    vector_constant(vector_constant)
  {

  }

  snde_coord3 math_parameter_vector_const::get_vector(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index)
  // parameter_index human interpreted parameter number, starting at 1, for error messages only
  {
    return vector_constant;
  }


  bool math_parameter_vector_const::operator==(const math_parameter &ref) // used for comparing parameters to instantiated_math_functions
  {
    const math_parameter_vector_const *vref = dynamic_cast<const math_parameter_vector_const *>(&ref);

    if (!vref) {
      return false;
    }
    
    return equalcoord3(vector_constant,vref->vector_constant);

  }
  
  bool math_parameter_vector_const::operator!=(const math_parameter &ref)
  {
    return !(*this==ref);
  }

  math_parameter_orientation_const::math_parameter_orientation_const(snde_orientation3 orientation_constant) :
    math_parameter(SNDE_MFPT_ORIENTATION),
    orientation_constant(orientation_constant)
  {

  }

  snde_orientation3 math_parameter_orientation_const::get_orientation(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index)
  // parameter_index human interpreted parameter number, starting at 1, for error messages only
  {
    return orientation_constant;
  }


  bool math_parameter_orientation_const::operator==(const math_parameter &ref) // used for comparing parameters to instantiated_math_functions
  {
    const math_parameter_orientation_const *oref = dynamic_cast<const math_parameter_orientation_const *>(&ref);

    if (!oref) {
      return false;
    }
    
    return orientation3_equal(orientation_constant,oref->orientation_constant);

  }
  
  bool math_parameter_orientation_const::operator!=(const math_parameter &ref)
  {
    return !(*this==ref);
  }

  
  
  math_parameter_indexvec_const::math_parameter_indexvec_const(const std::vector<snde_index> & indexvec) :
    math_parameter(SNDE_MFPT_INDEXVEC),
    indexvec(indexvec)
  {

  }

  std::vector<snde_index> math_parameter_indexvec_const::get_indexvec(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index)
  {
    return indexvec;
  }

  
  bool math_parameter_indexvec_const::operator==(const math_parameter &ref) // used for comparing parameters to instantiated_math_functions
  {
    const math_parameter_indexvec_const *iref = dynamic_cast<const math_parameter_indexvec_const *>(&ref);

    if (!iref) {
      return false;
    }

    return indexvec == iref->indexvec;

  }
  
  bool math_parameter_indexvec_const::operator!=(const math_parameter &ref)
  {
    return !(*this==ref);
  }


  math_parameter_metadata_const::math_parameter_metadata_const(std::shared_ptr<snde::constructible_metadata> metadata) :
    math_parameter(SNDE_MFPT_METADATA),
    metadata(metadata)
  {

  }

  std::shared_ptr<snde::constructible_metadata> math_parameter_metadata_const::get_metadata(std::shared_ptr<recording_set_state> rss, const std::string& channel_path_context, const std::shared_ptr<math_definition>& fcn_def, size_t parameter_index)
  {
    return metadata;
  }


  bool math_parameter_metadata_const::operator==(const math_parameter& ref) // used for comparing parameters to instantiated_math_functions
  {
    const math_parameter_metadata_const* iref = dynamic_cast<const math_parameter_metadata_const*>(&ref);

    if (!iref) {
      return false;
    }

    return metadata == iref->metadata;

  }

  bool math_parameter_metadata_const::operator!=(const math_parameter& ref)
  {
    return !(*this == ref);
  }

  
  math_parameter_recording::math_parameter_recording(std::string channel_name) :
    math_parameter(SNDE_MFPT_RECORDING),
    channel_name(channel_name),
    array_index(0),
    array_name("")
  {

  }

  math_parameter_recording::math_parameter_recording(std::string channel_name,size_t array_index) :
    math_parameter(SNDE_MFPT_RECORDING),
    channel_name(channel_name),
    array_index(array_index),
    array_name("")
  {

  }

  math_parameter_recording::math_parameter_recording(std::string channel_name,std::string array_name) :
    math_parameter(SNDE_MFPT_RECORDING),
    channel_name(channel_name),
    array_index(0),
    array_name(array_name)
  {

  }


  bool math_parameter_recording::operator==(const math_parameter &ref) // used for comparing parameters to instantiated_math_functions
  {
    const math_parameter_recording *rref = dynamic_cast<const math_parameter_recording *>(&ref);

    if (!rref) {
      return false;
    }

    return channel_name == rref->channel_name && array_index == rref->array_index && array_name==rref->array_name;

  }
  
  bool math_parameter_recording::operator!=(const math_parameter &ref)
  {
    return !(*this==ref);
  }

  std::set<std::string> math_parameter_recording::get_prerequisites(/*std::shared_ptr<recording_set_state> rss,*/ const std::string &channel_path_context)
  {
    std::set<std::string> retval;
    retval.emplace(recdb_path_join(channel_path_context,channel_name));
    return retval;
  }

  std::shared_ptr<recording_base> math_parameter_recording::get_recording(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index) // should only return ready recordings because we shouldn't be called until our deps are ready.
  // parameter_index human interpreted parameter number, starting at 1, for error messages only
  {
    std::shared_ptr<recording_base> rec;
    std::string fullpath = recdb_path_join(channel_path_context,channel_name);
    {
      //std::lock_guard<std::mutex> rsslock(rss->admin); // Think this locking is actually unnecessary
      rec=rss->recstatus.channel_map->at(fullpath).rec();
    }
    return rec; 
  }

  
  std::shared_ptr<ndarray_recording_ref> math_parameter_recording::get_ndarray_recording_ref(std::shared_ptr<recording_set_state> rss, const std::string &channel_path_context,const std::shared_ptr<math_definition> &fcn_def, size_t parameter_index) // should only return ready recordings because we shouldn't be called until our deps are ready.
  // parameter_index human interpreted parameter number, starting at 1, for error messages only
  {
    std::shared_ptr<recording_base> rec = get_recording(rss,channel_path_context,fcn_def,parameter_index);

    
    std::shared_ptr<multi_ndarray_recording> mnd_rec=std::dynamic_pointer_cast<multi_ndarray_recording>(rec);
    
    if (!mnd_rec) {
      if (typeid(*rec.get())==typeid(null_recording)) {
	// If the recording parameter is actually null,
	// still throw the error but make it silent
	throw silent_math_parameter_mismatch("Recording parameter %s relative to %s is not convertible to a multi_ndarray_recording",channel_name.c_str(),channel_path_context.c_str());
      }
      
      throw math_parameter_mismatch("Recording parameter %s relative to %s is not convertible to a multi_ndarray_recording",channel_name.c_str(),channel_path_context.c_str());
    }

    size_t index = array_index;

    if (array_name.size() > 0) { // if array_name given, use it to look up index 
      index = mnd_rec->name_mapping.at(array_name);
    }
    
    return mnd_rec->reference_ndarray(index); 
  }

}
