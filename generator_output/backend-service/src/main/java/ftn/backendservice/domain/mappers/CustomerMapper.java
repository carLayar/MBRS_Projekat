// WARNING: This file was autogenerated by MBRS generator.
// Do not update it because if you run generator again you changes will be deleted

package ftn.backendservice.domain.mappers;

import org.mapstruct.*;
import org.mapstruct.factory.Mappers;

import java.util.List;

import ftn.backendservice.domain.dtos.CustomerDto;
import ftn.backendservice.domain.entities.*;


@Mapper(unmappedTargetPolicy = ReportingPolicy.IGNORE,
        nullValuePropertyMappingStrategy = NullValuePropertyMappingStrategy.IGNORE)
public interface CustomerMapper {

    CustomerMapper INSTANCE = Mappers.getMapper(CustomerMapper.class);

    @Mapping(target = "accountIds", expression = "java(customer.getAccounts().stream().map(ftn.backendservice.domain.entities.Account::getId).collect(java.util.stream.Collectors.toList()))")
    @Mapping(source = "bankBranch.id", target = "bankBranchId")
    CustomerDto toDTO(Customer customer);

    List<CustomerDto> toDTO(List<Customer> customer);

}