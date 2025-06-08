# SNMP MIB module (A3COM-HUAWEI-OBJECT-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-OBJECT-INFO-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:03:52 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

h3cObjectInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55)
)
if mibBuilder.loadTexts:
    h3cObjectInfo.setRevisions(
        ("2004-12-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cObjectInformation_ObjectIdentity = ObjectIdentity
h3cObjectInformation = _H3cObjectInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1)
)
_H3cObjectInfoTable_Object = MibTable
h3cObjectInfoTable = _H3cObjectInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1)
)
if mibBuilder.loadTexts:
    h3cObjectInfoTable.setStatus("current")
_H3cObjectInfoEntry_Object = MibTableRow
h3cObjectInfoEntry = _H3cObjectInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1, 1)
)
h3cObjectInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-OBJECT-INFO-MIB", "h3cObjectInfoOID"),
    (0, "A3COM-HUAWEI-OBJECT-INFO-MIB", "h3cObjectInfoType"),
    (0, "A3COM-HUAWEI-OBJECT-INFO-MIB", "h3cObjectInfoTypeExtension"),
)
if mibBuilder.loadTexts:
    h3cObjectInfoEntry.setStatus("current")
_H3cObjectInfoOID_Type = ObjectIdentifier
_H3cObjectInfoOID_Object = MibTableColumn
h3cObjectInfoOID = _H3cObjectInfoOID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1, 1, 1),
    _H3cObjectInfoOID_Type()
)
h3cObjectInfoOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cObjectInfoOID.setStatus("current")


class _H3cObjectInfoType_Type(Integer32):
    """Custom type h3cObjectInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 1),
          ("accessType", 2),
          ("dataType", 3),
          ("dataRange", 4),
          ("dataLength", 5))
    )


_H3cObjectInfoType_Type.__name__ = "Integer32"
_H3cObjectInfoType_Object = MibTableColumn
h3cObjectInfoType = _H3cObjectInfoType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1, 1, 2),
    _H3cObjectInfoType_Type()
)
h3cObjectInfoType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cObjectInfoType.setStatus("current")


class _H3cObjectInfoTypeExtension_Type(OctetString):
    """Custom type h3cObjectInfoTypeExtension based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_H3cObjectInfoTypeExtension_Type.__name__ = "OctetString"
_H3cObjectInfoTypeExtension_Object = MibTableColumn
h3cObjectInfoTypeExtension = _H3cObjectInfoTypeExtension_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1, 1, 3),
    _H3cObjectInfoTypeExtension_Type()
)
h3cObjectInfoTypeExtension.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cObjectInfoTypeExtension.setStatus("current")
_H3cObjectInfoValue_Type = OctetString
_H3cObjectInfoValue_Object = MibTableColumn
h3cObjectInfoValue = _H3cObjectInfoValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1, 1, 4),
    _H3cObjectInfoValue_Type()
)
h3cObjectInfoValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cObjectInfoValue.setStatus("current")
_H3cObjectInfoMIBConformance_ObjectIdentity = ObjectIdentity
h3cObjectInfoMIBConformance = _H3cObjectInfoMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 2)
)
_H3cObjectInfoMIBCompliances_ObjectIdentity = ObjectIdentity
h3cObjectInfoMIBCompliances = _H3cObjectInfoMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 2, 1)
)
_H3cObjectInfoMIBGroups_ObjectIdentity = ObjectIdentity
h3cObjectInfoMIBGroups = _H3cObjectInfoMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 2, 2)
)

# Managed Objects groups

h3cObjectInfoTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 2, 2, 1)
)
h3cObjectInfoTableGroup.setObjects(
    ("A3COM-HUAWEI-OBJECT-INFO-MIB", "h3cObjectInfoValue")
)
if mibBuilder.loadTexts:
    h3cObjectInfoTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h3cObjectInfoMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 2, 1, 1)
)
h3cObjectInfoMIBCompliance.setObjects(
    ("A3COM-HUAWEI-OBJECT-INFO-MIB", "h3cObjectInfoTableGroup")
)
if mibBuilder.loadTexts:
    h3cObjectInfoMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-OBJECT-INFO-MIB",
    **{"h3cObjectInfo": h3cObjectInfo,
       "h3cObjectInformation": h3cObjectInformation,
       "h3cObjectInfoTable": h3cObjectInfoTable,
       "h3cObjectInfoEntry": h3cObjectInfoEntry,
       "h3cObjectInfoOID": h3cObjectInfoOID,
       "h3cObjectInfoType": h3cObjectInfoType,
       "h3cObjectInfoTypeExtension": h3cObjectInfoTypeExtension,
       "h3cObjectInfoValue": h3cObjectInfoValue,
       "h3cObjectInfoMIBConformance": h3cObjectInfoMIBConformance,
       "h3cObjectInfoMIBCompliances": h3cObjectInfoMIBCompliances,
       "h3cObjectInfoMIBCompliance": h3cObjectInfoMIBCompliance,
       "h3cObjectInfoMIBGroups": h3cObjectInfoMIBGroups,
       "h3cObjectInfoTableGroup": h3cObjectInfoTableGroup}
)
