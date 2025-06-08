# SNMP MIB module (CISCO-SNMP-VACM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SNMP-VACM-EXT-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:59 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(vacmSecurityModel,
 vacmSecurityName) = mibBuilder.importSymbols(
    "SNMP-VIEW-BASED-ACM-MIB",
    "vacmSecurityModel",
    "vacmSecurityName")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoSnmpVacmExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 409)
)
if mibBuilder.loadTexts:
    ciscoSnmpVacmExtMIB.setRevisions(
        ("2004-05-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSnmpVacmExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSnmpVacmExtMIBObjects = _CiscoSnmpVacmExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 409, 1)
)
_CvacmSecurityToGroupTable_Object = MibTable
cvacmSecurityToGroupTable = _CvacmSecurityToGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1)
)
if mibBuilder.loadTexts:
    cvacmSecurityToGroupTable.setStatus("current")
_CvacmSecurityToGroupEntry_Object = MibTableRow
cvacmSecurityToGroupEntry = _CvacmSecurityToGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1)
)
cvacmSecurityToGroupEntry.setIndexNames(
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityModel"),
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityName"),
    (0, "CISCO-SNMP-VACM-EXT-MIB", "cvacmSecurityGrpName"),
)
if mibBuilder.loadTexts:
    cvacmSecurityToGroupEntry.setStatus("current")


class _CvacmSecurityGrpName_Type(SnmpAdminString):
    """Custom type cvacmSecurityGrpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CvacmSecurityGrpName_Type.__name__ = "SnmpAdminString"
_CvacmSecurityGrpName_Object = MibTableColumn
cvacmSecurityGrpName = _CvacmSecurityGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1, 1),
    _CvacmSecurityGrpName_Type()
)
cvacmSecurityGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvacmSecurityGrpName.setStatus("current")


class _CvacmSecurityGrpStorageType_Type(StorageType):
    """Custom type cvacmSecurityGrpStorageType based on StorageType"""
    defaultValue = 3


_CvacmSecurityGrpStorageType_Type.__name__ = "StorageType"
_CvacmSecurityGrpStorageType_Object = MibTableColumn
cvacmSecurityGrpStorageType = _CvacmSecurityGrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1, 2),
    _CvacmSecurityGrpStorageType_Type()
)
cvacmSecurityGrpStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvacmSecurityGrpStorageType.setStatus("current")
_CvacmSecurityGrpStatus_Type = RowStatus
_CvacmSecurityGrpStatus_Object = MibTableColumn
cvacmSecurityGrpStatus = _CvacmSecurityGrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1, 3),
    _CvacmSecurityGrpStatus_Type()
)
cvacmSecurityGrpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvacmSecurityGrpStatus.setStatus("current")
_CiscoSnmpVacmExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSnmpVacmExtMIBConformance = _CiscoSnmpVacmExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 409, 2)
)
_CiscoSnmpVacmExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSnmpVacmExtMIBCompliances = _CiscoSnmpVacmExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 1)
)
_CiscoSnmpVacmExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSnmpVacmExtMIBGroups = _CiscoSnmpVacmExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 2)
)

# Managed Objects groups

ciscoSnmpVacmExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 2, 1)
)
ciscoSnmpVacmExtGroup.setObjects(
      *(("CISCO-SNMP-VACM-EXT-MIB", "cvacmSecurityGrpStorageType"),
        ("CISCO-SNMP-VACM-EXT-MIB", "cvacmSecurityGrpStatus"))
)
if mibBuilder.loadTexts:
    ciscoSnmpVacmExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSnmpVacmExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 1, 1)
)
ciscoSnmpVacmExtMIBCompliance.setObjects(
    ("CISCO-SNMP-VACM-EXT-MIB", "ciscoSnmpVacmExtGroup")
)
if mibBuilder.loadTexts:
    ciscoSnmpVacmExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SNMP-VACM-EXT-MIB",
    **{"ciscoSnmpVacmExtMIB": ciscoSnmpVacmExtMIB,
       "ciscoSnmpVacmExtMIBObjects": ciscoSnmpVacmExtMIBObjects,
       "cvacmSecurityToGroupTable": cvacmSecurityToGroupTable,
       "cvacmSecurityToGroupEntry": cvacmSecurityToGroupEntry,
       "cvacmSecurityGrpName": cvacmSecurityGrpName,
       "cvacmSecurityGrpStorageType": cvacmSecurityGrpStorageType,
       "cvacmSecurityGrpStatus": cvacmSecurityGrpStatus,
       "ciscoSnmpVacmExtMIBConformance": ciscoSnmpVacmExtMIBConformance,
       "ciscoSnmpVacmExtMIBCompliances": ciscoSnmpVacmExtMIBCompliances,
       "ciscoSnmpVacmExtMIBCompliance": ciscoSnmpVacmExtMIBCompliance,
       "ciscoSnmpVacmExtMIBGroups": ciscoSnmpVacmExtMIBGroups,
       "ciscoSnmpVacmExtGroup": ciscoSnmpVacmExtGroup}
)
