# SNMP MIB module (MSF-SPECIFIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/esa_162/MSF-SPECIFIC-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:16:25 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(elemSpecific,
 elementMIBCompliances,
 elementMIBGroups) = mibBuilder.importSymbols(
    "MSF-MIB",
    "elemSpecific",
    "elementMIBCompliances",
    "elementMIBGroups")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

msf_specific = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 7, 98, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ElemHwRaidArrayBitResult(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              11)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("absent", 2),
          ("nominal", 3),
          ("error", 11))
    )



# MIB Managed Objects in the order of their OIDs

_ElemHw_ObjectIdentity = ObjectIdentity
elemHw = _ElemHw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 7, 98, 5)
)
_ElemHwRaidArraySpecificInfoTable_Object = MibTable
elemHwRaidArraySpecificInfoTable = _ElemHwRaidArraySpecificInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 7, 98, 5, 2)
)
if mibBuilder.loadTexts:
    elemHwRaidArraySpecificInfoTable.setStatus("current")
_ElemHwRaidArraySpecificInfoEntry_Object = MibTableRow
elemHwRaidArraySpecificInfoEntry = _ElemHwRaidArraySpecificInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 7, 98, 5, 2, 1)
)
elemHwRaidArraySpecificInfoEntry.setIndexNames(
    (0, "MSF-SPECIFIC-MIB", "elemHwRaidArrayIndex"),
)
if mibBuilder.loadTexts:
    elemHwRaidArraySpecificInfoEntry.setStatus("current")


class _ElemHwRaidArrayIndex_Type(Integer32):
    """Custom type elemHwRaidArrayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_ElemHwRaidArrayIndex_Type.__name__ = "Integer32"
_ElemHwRaidArrayIndex_Object = MibTableColumn
elemHwRaidArrayIndex = _ElemHwRaidArrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 7, 98, 5, 2, 1, 1),
    _ElemHwRaidArrayIndex_Type()
)
elemHwRaidArrayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemHwRaidArrayIndex.setStatus("current")
_ElemHwRaidArrayID_Type = DisplayString
_ElemHwRaidArrayID_Object = MibTableColumn
elemHwRaidArrayID = _ElemHwRaidArrayID_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 7, 98, 5, 2, 1, 121),
    _ElemHwRaidArrayID_Type()
)
elemHwRaidArrayID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwRaidArrayID.setStatus("current")
_ElemHwRaidArrayPartNumber_Type = DisplayString
_ElemHwRaidArrayPartNumber_Object = MibTableColumn
elemHwRaidArrayPartNumber = _ElemHwRaidArrayPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 7, 98, 5, 2, 1, 122),
    _ElemHwRaidArrayPartNumber_Type()
)
elemHwRaidArrayPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwRaidArrayPartNumber.setStatus("current")
_ElemHwRaidArrayVersion_Type = DisplayString
_ElemHwRaidArrayVersion_Object = MibTableColumn
elemHwRaidArrayVersion = _ElemHwRaidArrayVersion_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 7, 98, 5, 2, 1, 123),
    _ElemHwRaidArrayVersion_Type()
)
elemHwRaidArrayVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwRaidArrayVersion.setStatus("current")
_ElemHwRaidArraySerialNumber_Type = DisplayString
_ElemHwRaidArraySerialNumber_Object = MibTableColumn
elemHwRaidArraySerialNumber = _ElemHwRaidArraySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 7, 98, 5, 2, 1, 124),
    _ElemHwRaidArraySerialNumber_Type()
)
elemHwRaidArraySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwRaidArraySerialNumber.setStatus("current")
_ElemHwRaidArrayBitResult_Type = ElemHwRaidArrayBitResult
_ElemHwRaidArrayBitResult_Object = MibTableColumn
elemHwRaidArrayBitResult = _ElemHwRaidArrayBitResult_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 7, 98, 5, 2, 1, 125),
    _ElemHwRaidArrayBitResult_Type()
)
elemHwRaidArrayBitResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwRaidArrayBitResult.setStatus("current")

# Managed Objects groups

elementMIBSpecificGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 7, 100, 2, 3)
)
elementMIBSpecificGroup.setObjects(
      *(("MSF-SPECIFIC-MIB", "elemHwRaidArrayID"),
        ("MSF-SPECIFIC-MIB", "elemHwRaidArrayPartNumber"),
        ("MSF-SPECIFIC-MIB", "elemHwRaidArrayVersion"),
        ("MSF-SPECIFIC-MIB", "elemHwRaidArraySerialNumber"),
        ("MSF-SPECIFIC-MIB", "elemHwRaidArrayBitResult"))
)
if mibBuilder.loadTexts:
    elementMIBSpecificGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

elementMIBSpecificCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 7, 100, 1, 2)
)
elementMIBSpecificCompliance.setObjects(
    ("MSF-SPECIFIC-MIB", "elementMIBSpecificGroup")
)
if mibBuilder.loadTexts:
    elementMIBSpecificCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MSF-SPECIFIC-MIB",
    **{"ElemHwRaidArrayBitResult": ElemHwRaidArrayBitResult,
       "msf-specific": msf_specific,
       "elemHw": elemHw,
       "elemHwRaidArraySpecificInfoTable": elemHwRaidArraySpecificInfoTable,
       "elemHwRaidArraySpecificInfoEntry": elemHwRaidArraySpecificInfoEntry,
       "elemHwRaidArrayIndex": elemHwRaidArrayIndex,
       "elemHwRaidArrayID": elemHwRaidArrayID,
       "elemHwRaidArrayPartNumber": elemHwRaidArrayPartNumber,
       "elemHwRaidArrayVersion": elemHwRaidArrayVersion,
       "elemHwRaidArraySerialNumber": elemHwRaidArraySerialNumber,
       "elemHwRaidArrayBitResult": elemHwRaidArrayBitResult,
       "elementMIBSpecificCompliance": elementMIBSpecificCompliance,
       "elementMIBSpecificGroup": elementMIBSpecificGroup}
)
