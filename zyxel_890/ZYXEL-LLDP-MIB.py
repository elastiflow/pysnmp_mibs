# SNMP MIB module (ZYXEL-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-LLDP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:46:16 2025
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

(BridgeId,
 Timeout,
 dot1dBasePort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "dot1dBasePort")

(OperationResponseStatus,) = mibBuilder.importSymbols(
    "DISMAN-PING-MIB",
    "OperationResponseStatus")

(dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepIdentifier")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ospfAddressLessIf,
 ospfAreaId,
 ospfIfIpAddress,
 ospfLsdbAreaId,
 ospfLsdbLsid,
 ospfLsdbRouterId,
 ospfLsdbType,
 ospfNbrAddressLessIndex,
 ospfNbrIpAddr,
 ospfVirtIfAreaId,
 ospfVirtIfNeighbor) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "ospfAddressLessIf",
    "ospfAreaId",
    "ospfIfIpAddress",
    "ospfLsdbAreaId",
    "ospfLsdbLsid",
    "ospfLsdbRouterId",
    "ospfLsdbType",
    "ospfNbrAddressLessIndex",
    "ospfNbrIpAddr",
    "ospfVirtIfAreaId",
    "ospfVirtIfNeighbor")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysObjectID")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelLldp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelLldpSetup_ObjectIdentity = ObjectIdentity
zyxelLldpSetup = _ZyxelLldpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 1)
)
_ZyLldpState_Type = EnabledStatus
_ZyLldpState_Object = MibScalar
zyLldpState = _ZyLldpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 1, 1),
    _ZyLldpState_Type()
)
zyLldpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLldpState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-LLDP-MIB",
    **{"zyxelLldp": zyxelLldp,
       "zyxelLldpSetup": zyxelLldpSetup,
       "zyLldpState": zyLldpState}
)
