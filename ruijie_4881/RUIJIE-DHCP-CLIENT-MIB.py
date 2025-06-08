# SNMP MIB module (RUIJIE-DHCP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-DHCP-CLIENT-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:39 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieDhcpClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 135)
)
if mibBuilder.loadTexts:
    ruijieDhcpClientMIB.setRevisions(
        ("2015-02-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieDhcpClientMIBObjects_ObjectIdentity = ObjectIdentity
ruijieDhcpClientMIBObjects = _RuijieDhcpClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 135, 0)
)
_RuijieDhcpClientConfig_ObjectIdentity = ObjectIdentity
ruijieDhcpClientConfig = _RuijieDhcpClientConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 135, 0, 1)
)
_RuijieDhcpClientIntfTable_Object = MibTable
ruijieDhcpClientIntfTable = _RuijieDhcpClientIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 135, 0, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieDhcpClientIntfTable.setStatus("current")
_RuijieDhcpClientIntfEntry_Object = MibTableRow
ruijieDhcpClientIntfEntry = _RuijieDhcpClientIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 135, 0, 1, 2, 1)
)
ruijieDhcpClientIntfEntry.setIndexNames(
    (0, "RUIJIE-DHCP-CLIENT-MIB", "ruijieDhcpIntfClientIndex"),
)
if mibBuilder.loadTexts:
    ruijieDhcpClientIntfEntry.setStatus("current")
_RuijieDhcpIntfClientIndex_Type = InterfaceIndex
_RuijieDhcpIntfClientIndex_Object = MibTableColumn
ruijieDhcpIntfClientIndex = _RuijieDhcpIntfClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 135, 0, 1, 2, 1, 1),
    _RuijieDhcpIntfClientIndex_Type()
)
ruijieDhcpIntfClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpIntfClientIndex.setStatus("current")


class _RuijieDhcpClientIpAddrDhcpStatus_Type(Integer32):
    """Custom type ruijieDhcpClientIpAddrDhcpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieDhcpClientIpAddrDhcpStatus_Type.__name__ = "Integer32"
_RuijieDhcpClientIpAddrDhcpStatus_Object = MibTableColumn
ruijieDhcpClientIpAddrDhcpStatus = _RuijieDhcpClientIpAddrDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 135, 0, 1, 2, 1, 2),
    _RuijieDhcpClientIpAddrDhcpStatus_Type()
)
ruijieDhcpClientIpAddrDhcpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpClientIpAddrDhcpStatus.setStatus("current")
_RuijieDhcpClientMIBConformance_ObjectIdentity = ObjectIdentity
ruijieDhcpClientMIBConformance = _RuijieDhcpClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 135, 2)
)
_RuijieDhcpClientMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieDhcpClientMIBCompliances = _RuijieDhcpClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 135, 2, 1)
)
_RuijieDhcpClientMIBGroups_ObjectIdentity = ObjectIdentity
ruijieDhcpClientMIBGroups = _RuijieDhcpClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 135, 2, 2)
)

# Managed Objects groups

ruijieDhcpClientIntfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 135, 2, 2, 1)
)
ruijieDhcpClientIntfConfigGroup.setObjects(
    ("RUIJIE-DHCP-CLIENT-MIB", "ruijieDhcpClientIpAddrDhcpStatus")
)
if mibBuilder.loadTexts:
    ruijieDhcpClientIntfConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieDhcpClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 135, 2, 1, 1)
)
ruijieDhcpClientMIBCompliance.setObjects(
    ("RUIJIE-DHCP-CLIENT-MIB", "ruijieDhcpClientIntfConfigGroup")
)
if mibBuilder.loadTexts:
    ruijieDhcpClientMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-DHCP-CLIENT-MIB",
    **{"ruijieDhcpClientMIB": ruijieDhcpClientMIB,
       "ruijieDhcpClientMIBObjects": ruijieDhcpClientMIBObjects,
       "ruijieDhcpClientConfig": ruijieDhcpClientConfig,
       "ruijieDhcpClientIntfTable": ruijieDhcpClientIntfTable,
       "ruijieDhcpClientIntfEntry": ruijieDhcpClientIntfEntry,
       "ruijieDhcpIntfClientIndex": ruijieDhcpIntfClientIndex,
       "ruijieDhcpClientIpAddrDhcpStatus": ruijieDhcpClientIpAddrDhcpStatus,
       "ruijieDhcpClientMIBConformance": ruijieDhcpClientMIBConformance,
       "ruijieDhcpClientMIBCompliances": ruijieDhcpClientMIBCompliances,
       "ruijieDhcpClientMIBCompliance": ruijieDhcpClientMIBCompliance,
       "ruijieDhcpClientMIBGroups": ruijieDhcpClientMIBGroups,
       "ruijieDhcpClientIntfConfigGroup": ruijieDhcpClientIntfConfigGroup}
)
