# SNMP MIB module (CISCO-IF-LOOPBACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-IF-LOOPBACK-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:29:57 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoIfLoopbackMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399)
)
if mibBuilder.loadTexts:
    ciscoIfLoopbackMIB.setRevisions(
        ("2001-11-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIfLoopbackMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIfLoopbackMIBObjects = _CiscoIfLoopbackMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 1)
)
_CiscoIfLoopbackConfig_ObjectIdentity = ObjectIdentity
ciscoIfLoopbackConfig = _CiscoIfLoopbackConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1)
)
_CifLConfTable_Object = MibTable
cifLConfTable = _CifLConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cifLConfTable.setStatus("current")
_CifLConfEntry_Object = MibTableRow
cifLConfEntry = _CifLConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1)
)
cifLConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cifLConfEntry.setStatus("current")


class _CifLLoopback_Type(Integer32):
    """Custom type cifLLoopback based on Integer32"""
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
        *(("farEndLineLoopback", 1),
          ("farEndPayloadLoopback", 2),
          ("remoteLineLoopback", 3),
          ("remotePayloadLoopback", 4),
          ("localLoopback", 5))
    )


_CifLLoopback_Type.__name__ = "Integer32"
_CifLLoopback_Object = MibTableColumn
cifLLoopback = _CifLLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1, 1),
    _CifLLoopback_Type()
)
cifLLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifLLoopback.setStatus("current")


class _CifLLoopbackStatus_Type(Integer32):
    """Custom type cifLLoopbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("completed", 1),
          ("inProgress", 2),
          ("clockOutOfSync", 3),
          ("failed", 4))
    )


_CifLLoopbackStatus_Type.__name__ = "Integer32"
_CifLLoopbackStatus_Object = MibTableColumn
cifLLoopbackStatus = _CifLLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1, 2),
    _CifLLoopbackStatus_Type()
)
cifLLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifLLoopbackStatus.setStatus("current")


class _CifLFELoopbackDeviceAndCode_Type(Integer32):
    """Custom type cifLFELoopbackDeviceAndCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("nonLatchOCUwith1", 1),
          ("nonLatchOCUwithout1", 2),
          ("nonLatchCSU", 3),
          ("nonLatchDSU", 4),
          ("latchDS0Drop", 5),
          ("latchDS0Line", 6),
          ("latchOCU", 7),
          ("latchCSU", 8),
          ("latchDSU", 9),
          ("latchHL96", 10),
          ("v54PN127Polynomial", 11),
          ("lineInband", 12),
          ("lineLoopbackESF", 13),
          ("payloadLoopbackESF", 14),
          ("noCode", 15),
          ("lineLoopbackFEAC", 16),
          ("smartJackInband", 17))
    )


_CifLFELoopbackDeviceAndCode_Type.__name__ = "Integer32"
_CifLFELoopbackDeviceAndCode_Object = MibTableColumn
cifLFELoopbackDeviceAndCode = _CifLFELoopbackDeviceAndCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1, 3),
    _CifLFELoopbackDeviceAndCode_Type()
)
cifLFELoopbackDeviceAndCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifLFELoopbackDeviceAndCode.setStatus("current")
_CifLRowStatus_Type = RowStatus
_CifLRowStatus_Object = MibTableColumn
cifLRowStatus = _CifLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1, 4),
    _CifLRowStatus_Type()
)
cifLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifLRowStatus.setStatus("current")
_CiscoIfLoopbackMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIfLoopbackMIBConformance = _CiscoIfLoopbackMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 8)
)
_CiscoIfLoopbackMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIfLoopbackMIBCompliances = _CiscoIfLoopbackMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 8, 1)
)
_CiscoIfLoopbackMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIfLoopbackMIBGroups = _CiscoIfLoopbackMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 8, 2)
)

# Managed Objects groups

ciscoIfLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 8, 2, 1)
)
ciscoIfLoopbackGroup.setObjects(
      *(("CISCO-IF-LOOPBACK-MIB", "cifLLoopback"),
        ("CISCO-IF-LOOPBACK-MIB", "cifLLoopbackStatus"),
        ("CISCO-IF-LOOPBACK-MIB", "cifLFELoopbackDeviceAndCode"),
        ("CISCO-IF-LOOPBACK-MIB", "cifLRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoIfLoopbackGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIfLoopbackMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 8, 1, 1)
)
ciscoIfLoopbackMIBCompliance.setObjects(
    ("CISCO-IF-LOOPBACK-MIB", "ciscoIfLoopbackGroup")
)
if mibBuilder.loadTexts:
    ciscoIfLoopbackMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IF-LOOPBACK-MIB",
    **{"ciscoIfLoopbackMIB": ciscoIfLoopbackMIB,
       "ciscoIfLoopbackMIBObjects": ciscoIfLoopbackMIBObjects,
       "ciscoIfLoopbackConfig": ciscoIfLoopbackConfig,
       "cifLConfTable": cifLConfTable,
       "cifLConfEntry": cifLConfEntry,
       "cifLLoopback": cifLLoopback,
       "cifLLoopbackStatus": cifLLoopbackStatus,
       "cifLFELoopbackDeviceAndCode": cifLFELoopbackDeviceAndCode,
       "cifLRowStatus": cifLRowStatus,
       "ciscoIfLoopbackMIBConformance": ciscoIfLoopbackMIBConformance,
       "ciscoIfLoopbackMIBCompliances": ciscoIfLoopbackMIBCompliances,
       "ciscoIfLoopbackMIBCompliance": ciscoIfLoopbackMIBCompliance,
       "ciscoIfLoopbackMIBGroups": ciscoIfLoopbackMIBGroups,
       "ciscoIfLoopbackGroup": ciscoIfLoopbackGroup}
)
