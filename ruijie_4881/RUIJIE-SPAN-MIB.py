# SNMP MIB module (RUIJIE-SPAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-SPAN-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:11 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex")

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

ruijieSPANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 23)
)
if mibBuilder.loadTexts:
    ruijieSPANMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieSPANMIBObjects_ObjectIdentity = ObjectIdentity
ruijieSPANMIBObjects = _RuijieSPANMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 23, 1)
)
_RuijieSPANSessionNum_Type = Integer32
_RuijieSPANSessionNum_Object = MibScalar
ruijieSPANSessionNum = _RuijieSPANSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 23, 1, 1),
    _RuijieSPANSessionNum_Type()
)
ruijieSPANSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSPANSessionNum.setStatus("current")
_RuijieSPANTable_Object = MibTable
ruijieSPANTable = _RuijieSPANTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 23, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieSPANTable.setStatus("current")
_RuijieSPANEntry_Object = MibTableRow
ruijieSPANEntry = _RuijieSPANEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 23, 1, 2, 1)
)
ruijieSPANEntry.setIndexNames(
    (0, "RUIJIE-SPAN-MIB", "ruijieSPANSession"),
    (0, "RUIJIE-SPAN-MIB", "ruijieSPANIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieSPANEntry.setStatus("current")
_RuijieSPANSession_Type = Integer32
_RuijieSPANSession_Object = MibTableColumn
ruijieSPANSession = _RuijieSPANSession_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 23, 1, 2, 1, 1),
    _RuijieSPANSession_Type()
)
ruijieSPANSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSPANSession.setStatus("current")
_RuijieSPANIfIndex_Type = IfIndex
_RuijieSPANIfIndex_Object = MibTableColumn
ruijieSPANIfIndex = _RuijieSPANIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 23, 1, 2, 1, 2),
    _RuijieSPANIfIndex_Type()
)
ruijieSPANIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSPANIfIndex.setStatus("current")


class _RuijieSPANIfRole_Type(Integer32):
    """Custom type ruijieSPANIfRole based on Integer32"""
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
        *(("span-desc", 1),
          ("span-src-rx", 2),
          ("span-src-tx", 3),
          ("span-src-all", 4))
    )


_RuijieSPANIfRole_Type.__name__ = "Integer32"
_RuijieSPANIfRole_Object = MibTableColumn
ruijieSPANIfRole = _RuijieSPANIfRole_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 23, 1, 2, 1, 3),
    _RuijieSPANIfRole_Type()
)
ruijieSPANIfRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSPANIfRole.setStatus("current")
_RuijieSPANEntryStatus_Type = ConfigStatus
_RuijieSPANEntryStatus_Object = MibTableColumn
ruijieSPANEntryStatus = _RuijieSPANEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 23, 1, 2, 1, 4),
    _RuijieSPANEntryStatus_Type()
)
ruijieSPANEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSPANEntryStatus.setStatus("current")
_RuijieSPANMIBConformance_ObjectIdentity = ObjectIdentity
ruijieSPANMIBConformance = _RuijieSPANMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 23, 3)
)
_RuijieSPANMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieSPANMIBCompliances = _RuijieSPANMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 23, 3, 1)
)
_RuijieSPANMIBGroups_ObjectIdentity = ObjectIdentity
ruijieSPANMIBGroups = _RuijieSPANMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 23, 3, 2)
)

# Managed Objects groups

ruijieSPANMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 23, 3, 2, 1)
)
ruijieSPANMIBGroup.setObjects(
      *(("RUIJIE-SPAN-MIB", "ruijieSPANSession"),
        ("RUIJIE-SPAN-MIB", "ruijieSPANIfIndex"),
        ("RUIJIE-SPAN-MIB", "ruijieSPANIfRole"),
        ("RUIJIE-SPAN-MIB", "ruijieSPANEntryStatus"))
)
if mibBuilder.loadTexts:
    ruijieSPANMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieSPANMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 23, 3, 1, 1)
)
ruijieSPANMIBCompliance.setObjects(
    ("RUIJIE-SPAN-MIB", "ruijieSPANMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieSPANMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-SPAN-MIB",
    **{"ruijieSPANMIB": ruijieSPANMIB,
       "ruijieSPANMIBObjects": ruijieSPANMIBObjects,
       "ruijieSPANSessionNum": ruijieSPANSessionNum,
       "ruijieSPANTable": ruijieSPANTable,
       "ruijieSPANEntry": ruijieSPANEntry,
       "ruijieSPANSession": ruijieSPANSession,
       "ruijieSPANIfIndex": ruijieSPANIfIndex,
       "ruijieSPANIfRole": ruijieSPANIfRole,
       "ruijieSPANEntryStatus": ruijieSPANEntryStatus,
       "ruijieSPANMIBConformance": ruijieSPANMIBConformance,
       "ruijieSPANMIBCompliances": ruijieSPANMIBCompliances,
       "ruijieSPANMIBCompliance": ruijieSPANMIBCompliance,
       "ruijieSPANMIBGroups": ruijieSPANMIBGroups,
       "ruijieSPANMIBGroup": ruijieSPANMIBGroup}
)
