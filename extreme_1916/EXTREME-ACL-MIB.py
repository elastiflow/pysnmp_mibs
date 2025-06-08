# SNMP MIB module (EXTREME-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-ACL-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:22:20 2025
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

(extremeAclDirection,) = mibBuilder.importSymbols(
    "EXTREME-CLEARFLOW-MIB",
    "extremeAclDirection")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

extremeAcl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 48)
)
if mibBuilder.loadTexts:
    extremeAcl.setRevisions(
        ("2015-12-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeAclObjects_ObjectIdentity = ObjectIdentity
extremeAclObjects = _ExtremeAclObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 48, 1)
)
_ExtremeAclStatsTable_Object = MibTable
extremeAclStatsTable = _ExtremeAclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 48, 1, 1)
)
if mibBuilder.loadTexts:
    extremeAclStatsTable.setStatus("current")
_ExtremeAclStatsEntry_Object = MibTableRow
extremeAclStatsEntry = _ExtremeAclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 48, 1, 1, 1)
)
extremeAclStatsEntry.setIndexNames(
    (0, "EXTREME-ACL-MIB", "extremeAclStatsVlanIfIndex"),
    (0, "EXTREME-ACL-MIB", "extremeAclStatsPortIfIndex"),
    (0, "EXTREME-CLEARFLOW-MIB", "extremeAclDirection"),
    (0, "EXTREME-ACL-MIB", "extremeAclStatsCounterName"),
)
if mibBuilder.loadTexts:
    extremeAclStatsEntry.setStatus("current")
_ExtremeAclStatsVlanIfIndex_Type = InterfaceIndexOrZero
_ExtremeAclStatsVlanIfIndex_Object = MibTableColumn
extremeAclStatsVlanIfIndex = _ExtremeAclStatsVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 48, 1, 1, 1, 1),
    _ExtremeAclStatsVlanIfIndex_Type()
)
extremeAclStatsVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeAclStatsVlanIfIndex.setStatus("current")
_ExtremeAclStatsPortIfIndex_Type = InterfaceIndexOrZero
_ExtremeAclStatsPortIfIndex_Object = MibTableColumn
extremeAclStatsPortIfIndex = _ExtremeAclStatsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 48, 1, 1, 1, 2),
    _ExtremeAclStatsPortIfIndex_Type()
)
extremeAclStatsPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeAclStatsPortIfIndex.setStatus("current")


class _ExtremeAclDirection_Type(Integer32):
    """Custom type extremeAclDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ExtremeAclDirection_Type.__name__ = "Integer32"
_ExtremeAclDirection_Object = MibTableColumn
extremeAclDirection = _ExtremeAclDirection_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 48, 1, 1, 1, 3),
    _ExtremeAclDirection_Type()
)
extremeAclDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeAclDirection.setStatus("current")


class _ExtremeAclStatsCounterName_Type(DisplayString):
    """Custom type extremeAclStatsCounterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeAclStatsCounterName_Type.__name__ = "DisplayString"
_ExtremeAclStatsCounterName_Object = MibTableColumn
extremeAclStatsCounterName = _ExtremeAclStatsCounterName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 48, 1, 1, 1, 4),
    _ExtremeAclStatsCounterName_Type()
)
extremeAclStatsCounterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeAclStatsCounterName.setStatus("current")
_ExtremeAclStatsPktCount_Type = Counter64
_ExtremeAclStatsPktCount_Object = MibTableColumn
extremeAclStatsPktCount = _ExtremeAclStatsPktCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 48, 1, 1, 1, 5),
    _ExtremeAclStatsPktCount_Type()
)
extremeAclStatsPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeAclStatsPktCount.setStatus("current")
_ExtremeAclStatsByteCount_Type = Counter64
_ExtremeAclStatsByteCount_Object = MibTableColumn
extremeAclStatsByteCount = _ExtremeAclStatsByteCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 48, 1, 1, 1, 6),
    _ExtremeAclStatsByteCount_Type()
)
extremeAclStatsByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeAclStatsByteCount.setStatus("current")
_AclConformance_ObjectIdentity = ObjectIdentity
aclConformance = _AclConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 48, 9)
)
_AclGroups_ObjectIdentity = ObjectIdentity
aclGroups = _AclGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 48, 9, 1)
)
_AclCompliances_ObjectIdentity = ObjectIdentity
aclCompliances = _AclCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 48, 9, 2)
)

# Managed Objects groups

aclCounterStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 48, 9, 1, 1)
)
aclCounterStatsGroup.setObjects(
      *(("EXTREME-ACL-MIB", "extremeAclStatsPktCount"),
        ("EXTREME-ACL-MIB", "extremeAclStatsByteCount"))
)
if mibBuilder.loadTexts:
    aclCounterStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aclStatistics = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1916, 1, 48, 9, 2, 1)
)
aclStatistics.setObjects(
    ("EXTREME-ACL-MIB", "aclCounterStatsGroup")
)
if mibBuilder.loadTexts:
    aclStatistics.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-ACL-MIB",
    **{"extremeAcl": extremeAcl,
       "extremeAclObjects": extremeAclObjects,
       "extremeAclStatsTable": extremeAclStatsTable,
       "extremeAclStatsEntry": extremeAclStatsEntry,
       "extremeAclStatsVlanIfIndex": extremeAclStatsVlanIfIndex,
       "extremeAclStatsPortIfIndex": extremeAclStatsPortIfIndex,
       "extremeAclDirection": extremeAclDirection,
       "extremeAclStatsCounterName": extremeAclStatsCounterName,
       "extremeAclStatsPktCount": extremeAclStatsPktCount,
       "extremeAclStatsByteCount": extremeAclStatsByteCount,
       "aclConformance": aclConformance,
       "aclGroups": aclGroups,
       "aclCounterStatsGroup": aclCounterStatsGroup,
       "aclCompliances": aclCompliances,
       "aclStatistics": aclStatistics}
)
