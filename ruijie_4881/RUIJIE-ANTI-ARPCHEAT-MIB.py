# SNMP MIB module (RUIJIE-ANTI-ARPCHEAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-ANTI-ARPCHEAT-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:06:23 2025
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

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieAntiArpcheatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 41)
)
if mibBuilder.loadTexts:
    ruijieAntiArpcheatMIB.setRevisions(
        ("2007-01-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieAntiArpcheatMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAntiArpcheatMIBObjects = _RuijieAntiArpcheatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 41, 1)
)
_RuijieTrustedArpDelete_Type = Integer32
_RuijieTrustedArpDelete_Object = MibScalar
ruijieTrustedArpDelete = _RuijieTrustedArpDelete_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 41, 1, 1),
    _RuijieTrustedArpDelete_Type()
)
ruijieTrustedArpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieTrustedArpDelete.setStatus("current")
_RuijieTrustedArpTable_Object = MibTable
ruijieTrustedArpTable = _RuijieTrustedArpTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 41, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieTrustedArpTable.setStatus("current")
_RuijieTrustedArpEntry_Object = MibTableRow
ruijieTrustedArpEntry = _RuijieTrustedArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 41, 1, 2, 1)
)
ruijieTrustedArpEntry.setIndexNames(
    (0, "RUIJIE-ANTI-ARPCHEAT-MIB", "trustedArpIfIndex"),
    (0, "RUIJIE-ANTI-ARPCHEAT-MIB", "trustedArpIp"),
)
if mibBuilder.loadTexts:
    ruijieTrustedArpEntry.setStatus("current")
_TrustedArpIfIndex_Type = IfIndex
_TrustedArpIfIndex_Object = MibTableColumn
trustedArpIfIndex = _TrustedArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 41, 1, 2, 1, 1),
    _TrustedArpIfIndex_Type()
)
trustedArpIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpIfIndex.setStatus("current")
_TrustedArpIp_Type = IpAddress
_TrustedArpIp_Object = MibTableColumn
trustedArpIp = _TrustedArpIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 41, 1, 2, 1, 2),
    _TrustedArpIp_Type()
)
trustedArpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpIp.setStatus("current")
_TrustedArpMediaPhysAddress_Type = MacAddress
_TrustedArpMediaPhysAddress_Object = MibTableColumn
trustedArpMediaPhysAddress = _TrustedArpMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 41, 1, 2, 1, 3),
    _TrustedArpMediaPhysAddress_Type()
)
trustedArpMediaPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpMediaPhysAddress.setStatus("current")
_TrustedArpVlan_Type = VlanId
_TrustedArpVlan_Object = MibTableColumn
trustedArpVlan = _TrustedArpVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 41, 1, 2, 1, 4),
    _TrustedArpVlan_Type()
)
trustedArpVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpVlan.setStatus("current")
_TrustedArpOperationType_Type = Integer32
_TrustedArpOperationType_Object = MibTableColumn
trustedArpOperationType = _TrustedArpOperationType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 41, 1, 2, 1, 5),
    _TrustedArpOperationType_Type()
)
trustedArpOperationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpOperationType.setStatus("current")
_RuijieAntiArpcheatMIBConformance_ObjectIdentity = ObjectIdentity
ruijieAntiArpcheatMIBConformance = _RuijieAntiArpcheatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 41, 2)
)
_RuijieAntiArpcheatMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieAntiArpcheatMIBCompliances = _RuijieAntiArpcheatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 41, 2, 1)
)
_RuijieAntiArpcheatMIBGroups_ObjectIdentity = ObjectIdentity
ruijieAntiArpcheatMIBGroups = _RuijieAntiArpcheatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 41, 2, 2)
)

# Managed Objects groups

ruijieAntiArpcheatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 41, 2, 2, 1)
)
ruijieAntiArpcheatMIBGroup.setObjects(
      *(("RUIJIE-ANTI-ARPCHEAT-MIB", "ruijieTrustedArpDelete"),
        ("RUIJIE-ANTI-ARPCHEAT-MIB", "trustedArpIfIndex"),
        ("RUIJIE-ANTI-ARPCHEAT-MIB", "trustedArpIp"),
        ("RUIJIE-ANTI-ARPCHEAT-MIB", "trustedArpMediaPhysAddress"),
        ("RUIJIE-ANTI-ARPCHEAT-MIB", "trustedArpVlan"),
        ("RUIJIE-ANTI-ARPCHEAT-MIB", "trustedArpOperationType"))
)
if mibBuilder.loadTexts:
    ruijieAntiArpcheatMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieAntiArpcheatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 41, 2, 1, 1)
)
ruijieAntiArpcheatMIBCompliance.setObjects(
    ("RUIJIE-ANTI-ARPCHEAT-MIB", "ruijieAntiArpcheatMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieAntiArpcheatMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-ANTI-ARPCHEAT-MIB",
    **{"ruijieAntiArpcheatMIB": ruijieAntiArpcheatMIB,
       "ruijieAntiArpcheatMIBObjects": ruijieAntiArpcheatMIBObjects,
       "ruijieTrustedArpDelete": ruijieTrustedArpDelete,
       "ruijieTrustedArpTable": ruijieTrustedArpTable,
       "ruijieTrustedArpEntry": ruijieTrustedArpEntry,
       "trustedArpIfIndex": trustedArpIfIndex,
       "trustedArpIp": trustedArpIp,
       "trustedArpMediaPhysAddress": trustedArpMediaPhysAddress,
       "trustedArpVlan": trustedArpVlan,
       "trustedArpOperationType": trustedArpOperationType,
       "ruijieAntiArpcheatMIBConformance": ruijieAntiArpcheatMIBConformance,
       "ruijieAntiArpcheatMIBCompliances": ruijieAntiArpcheatMIBCompliances,
       "ruijieAntiArpcheatMIBCompliance": ruijieAntiArpcheatMIBCompliance,
       "ruijieAntiArpcheatMIBGroups": ruijieAntiArpcheatMIBGroups,
       "ruijieAntiArpcheatMIBGroup": ruijieAntiArpcheatMIBGroup}
)
