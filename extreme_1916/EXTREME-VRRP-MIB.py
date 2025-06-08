# SNMP MIB module (EXTREME-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-VRRP-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:41:50 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(vrrpOperVrId,) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "vrrpOperVrId")


# MODULE-IDENTITY

extremeVrrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 49)
)
if mibBuilder.loadTexts:
    extremeVrrpMIB.setRevisions(
        ("2016-01-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeVrrpOperations_ObjectIdentity = ObjectIdentity
extremeVrrpOperations = _ExtremeVrrpOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 49, 1)
)
_ExtremeVrrpOperTable_Object = MibTable
extremeVrrpOperTable = _ExtremeVrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 49, 1, 1)
)
if mibBuilder.loadTexts:
    extremeVrrpOperTable.setStatus("current")
_ExtremeVrrpOperEntry_Object = MibTableRow
extremeVrrpOperEntry = _ExtremeVrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 49, 1, 1, 1)
)
extremeVrrpOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
)
if mibBuilder.loadTexts:
    extremeVrrpOperEntry.setStatus("current")


class _ExtremeVrrpFabricRoutingMode_Type(Integer32):
    """Custom type extremeVrrpFabricRoutingMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ExtremeVrrpFabricRoutingMode_Type.__name__ = "Integer32"
_ExtremeVrrpFabricRoutingMode_Object = MibTableColumn
extremeVrrpFabricRoutingMode = _ExtremeVrrpFabricRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 49, 1, 1, 1, 1),
    _ExtremeVrrpFabricRoutingMode_Type()
)
extremeVrrpFabricRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeVrrpFabricRoutingMode.setStatus("current")
_ExtremeVrrpConformance_ObjectIdentity = ObjectIdentity
extremeVrrpConformance = _ExtremeVrrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 49, 2)
)
_ExtremeVrrpMIBCompliances_ObjectIdentity = ObjectIdentity
extremeVrrpMIBCompliances = _ExtremeVrrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 49, 2, 1)
)
_ExtremeVrrpMIBGroups_ObjectIdentity = ObjectIdentity
extremeVrrpMIBGroups = _ExtremeVrrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 49, 2, 2)
)

# Managed Objects groups

extremeVrrpOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 49, 2, 2, 1)
)
extremeVrrpOperGroup.setObjects(
    ("EXTREME-VRRP-MIB", "extremeVrrpFabricRoutingMode")
)
if mibBuilder.loadTexts:
    extremeVrrpOperGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

extremeVrrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1916, 1, 49, 2, 1, 1)
)
extremeVrrpMIBCompliance.setObjects(
    ("EXTREME-VRRP-MIB", "extremeVrrpOperGroup")
)
if mibBuilder.loadTexts:
    extremeVrrpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-VRRP-MIB",
    **{"extremeVrrpMIB": extremeVrrpMIB,
       "extremeVrrpOperations": extremeVrrpOperations,
       "extremeVrrpOperTable": extremeVrrpOperTable,
       "extremeVrrpOperEntry": extremeVrrpOperEntry,
       "extremeVrrpFabricRoutingMode": extremeVrrpFabricRoutingMode,
       "extremeVrrpConformance": extremeVrrpConformance,
       "extremeVrrpMIBCompliances": extremeVrrpMIBCompliances,
       "extremeVrrpMIBCompliance": extremeVrrpMIBCompliance,
       "extremeVrrpMIBGroups": extremeVrrpMIBGroups,
       "extremeVrrpOperGroup": extremeVrrpOperGroup}
)
