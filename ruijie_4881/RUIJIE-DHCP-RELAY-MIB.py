# SNMP MIB module (RUIJIE-DHCP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-DHCP-RELAY-MIB.mib
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

ruijieDhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104)
)
if mibBuilder.loadTexts:
    ruijieDhcpMIB.setRevisions(
        ("2011-11-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieDhcpMIBObjects_ObjectIdentity = ObjectIdentity
ruijieDhcpMIBObjects = _RuijieDhcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1)
)
if mibBuilder.loadTexts:
    ruijieDhcpMIBObjects.setStatus("current")
_RuijieDhcpRelayMIBObjects_ObjectIdentity = ObjectIdentity
ruijieDhcpRelayMIBObjects = _RuijieDhcpRelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieDhcpRelayMIBObjects.setStatus("current")


class _RuijieDHCPRelayCycleStatus_Type(Integer32):
    """Custom type ruijieDHCPRelayCycleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_RuijieDHCPRelayCycleStatus_Type.__name__ = "Integer32"
_RuijieDHCPRelayCycleStatus_Object = MibScalar
ruijieDHCPRelayCycleStatus = _RuijieDHCPRelayCycleStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 1),
    _RuijieDHCPRelayCycleStatus_Type()
)
ruijieDHCPRelayCycleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDHCPRelayCycleStatus.setStatus("current")
_RuijieDhcpRelayCounters_ObjectIdentity = ObjectIdentity
ruijieDhcpRelayCounters = _RuijieDhcpRelayCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieDhcpRelayCounters.setStatus("current")
_RuijieDHCPRRxBadPktNum_Type = Integer32
_RuijieDHCPRRxBadPktNum_Object = MibScalar
ruijieDHCPRRxBadPktNum = _RuijieDHCPRRxBadPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 1),
    _RuijieDHCPRRxBadPktNum_Type()
)
ruijieDHCPRRxBadPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRRxBadPktNum.setStatus("current")
_RuijieDHCPRRxServerPktNum_Type = Integer32
_RuijieDHCPRRxServerPktNum_Object = MibScalar
ruijieDHCPRRxServerPktNum = _RuijieDHCPRRxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 2),
    _RuijieDHCPRRxServerPktNum_Type()
)
ruijieDHCPRRxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRRxServerPktNum.setStatus("current")
_RuijieDHCPRTxServerPktNum_Type = Integer32
_RuijieDHCPRTxServerPktNum_Object = MibScalar
ruijieDHCPRTxServerPktNum = _RuijieDHCPRTxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 3),
    _RuijieDHCPRTxServerPktNum_Type()
)
ruijieDHCPRTxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRTxServerPktNum.setStatus("current")
_RuijieDHCPRRxClientPktNum_Type = Integer32
_RuijieDHCPRRxClientPktNum_Object = MibScalar
ruijieDHCPRRxClientPktNum = _RuijieDHCPRRxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 4),
    _RuijieDHCPRRxClientPktNum_Type()
)
ruijieDHCPRRxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRRxClientPktNum.setStatus("current")
_RuijieDHCPRTxClientPktNum_Type = Integer32
_RuijieDHCPRTxClientPktNum_Object = MibScalar
ruijieDHCPRTxClientPktNum = _RuijieDHCPRTxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 5),
    _RuijieDHCPRTxClientPktNum_Type()
)
ruijieDHCPRTxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRTxClientPktNum.setStatus("current")
_RuijieDHCPRRxClientUniPktNum_Type = Integer32
_RuijieDHCPRRxClientUniPktNum_Object = MibScalar
ruijieDHCPRRxClientUniPktNum = _RuijieDHCPRRxClientUniPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 6),
    _RuijieDHCPRRxClientUniPktNum_Type()
)
ruijieDHCPRRxClientUniPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRRxClientUniPktNum.setStatus("current")
_RuijieDHCPRRxClientBroPktNum_Type = Integer32
_RuijieDHCPRRxClientBroPktNum_Object = MibScalar
ruijieDHCPRRxClientBroPktNum = _RuijieDHCPRRxClientBroPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 7),
    _RuijieDHCPRRxClientBroPktNum_Type()
)
ruijieDHCPRRxClientBroPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRRxClientBroPktNum.setStatus("current")
_RuijieDHCPRTxClientUniPktNum_Type = Integer32
_RuijieDHCPRTxClientUniPktNum_Object = MibScalar
ruijieDHCPRTxClientUniPktNum = _RuijieDHCPRTxClientUniPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 8),
    _RuijieDHCPRTxClientUniPktNum_Type()
)
ruijieDHCPRTxClientUniPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRTxClientUniPktNum.setStatus("current")
_RuijieDHCPRTxClientBroPktNum_Type = Integer32
_RuijieDHCPRTxClientBroPktNum_Object = MibScalar
ruijieDHCPRTxClientBroPktNum = _RuijieDHCPRTxClientBroPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 9),
    _RuijieDHCPRTxClientBroPktNum_Type()
)
ruijieDHCPRTxClientBroPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRTxClientBroPktNum.setStatus("current")
_RuijieDHCPRelayDiscoverPktNum_Type = Integer32
_RuijieDHCPRelayDiscoverPktNum_Object = MibScalar
ruijieDHCPRelayDiscoverPktNum = _RuijieDHCPRelayDiscoverPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 10),
    _RuijieDHCPRelayDiscoverPktNum_Type()
)
ruijieDHCPRelayDiscoverPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRelayDiscoverPktNum.setStatus("current")
_RuijieDHCPRelayRequestPktNum_Type = Integer32
_RuijieDHCPRelayRequestPktNum_Object = MibScalar
ruijieDHCPRelayRequestPktNum = _RuijieDHCPRelayRequestPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 11),
    _RuijieDHCPRelayRequestPktNum_Type()
)
ruijieDHCPRelayRequestPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRelayRequestPktNum.setStatus("current")
_RuijieDHCPRelayDeclinePktNum_Type = Integer32
_RuijieDHCPRelayDeclinePktNum_Object = MibScalar
ruijieDHCPRelayDeclinePktNum = _RuijieDHCPRelayDeclinePktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 12),
    _RuijieDHCPRelayDeclinePktNum_Type()
)
ruijieDHCPRelayDeclinePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRelayDeclinePktNum.setStatus("current")
_RuijieDHCPRelayReleasePktNum_Type = Integer32
_RuijieDHCPRelayReleasePktNum_Object = MibScalar
ruijieDHCPRelayReleasePktNum = _RuijieDHCPRelayReleasePktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 13),
    _RuijieDHCPRelayReleasePktNum_Type()
)
ruijieDHCPRelayReleasePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRelayReleasePktNum.setStatus("current")
_RuijieDHCPRelayInformPktNum_Type = Integer32
_RuijieDHCPRelayInformPktNum_Object = MibScalar
ruijieDHCPRelayInformPktNum = _RuijieDHCPRelayInformPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 14),
    _RuijieDHCPRelayInformPktNum_Type()
)
ruijieDHCPRelayInformPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRelayInformPktNum.setStatus("current")
_RuijieDHCPRelayOfferPktNum_Type = Integer32
_RuijieDHCPRelayOfferPktNum_Object = MibScalar
ruijieDHCPRelayOfferPktNum = _RuijieDHCPRelayOfferPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 15),
    _RuijieDHCPRelayOfferPktNum_Type()
)
ruijieDHCPRelayOfferPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRelayOfferPktNum.setStatus("current")
_RuijieDHCPRelayAckPktNum_Type = Integer32
_RuijieDHCPRelayAckPktNum_Object = MibScalar
ruijieDHCPRelayAckPktNum = _RuijieDHCPRelayAckPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 16),
    _RuijieDHCPRelayAckPktNum_Type()
)
ruijieDHCPRelayAckPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRelayAckPktNum.setStatus("current")
_RuijieDHCPRelayNakPktNum_Type = Integer32
_RuijieDHCPRelayNakPktNum_Object = MibScalar
ruijieDHCPRelayNakPktNum = _RuijieDHCPRelayNakPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 1, 1, 2, 17),
    _RuijieDHCPRelayNakPktNum_Type()
)
ruijieDHCPRelayNakPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDHCPRelayNakPktNum.setStatus("current")
_RuijieDhcpMIBConformance_ObjectIdentity = ObjectIdentity
ruijieDhcpMIBConformance = _RuijieDhcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 2)
)
if mibBuilder.loadTexts:
    ruijieDhcpMIBConformance.setStatus("current")
_RuijieDhcpMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieDhcpMIBCompliances = _RuijieDhcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 2, 1)
)
_RuijieDhcpMIBGroups_ObjectIdentity = ObjectIdentity
ruijieDhcpMIBGroups = _RuijieDhcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 2, 2)
)

# Managed Objects groups

ruijieDhcpRelayCountersObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 2, 2, 1)
)
ruijieDhcpRelayCountersObjects.setObjects(
      *(("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRelayCycleStatus"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRRxBadPktNum"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRRxServerPktNum"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRTxServerPktNum"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRRxClientPktNum"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRTxClientPktNum"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRRxClientUniPktNum"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRRxClientBroPktNum"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRTxClientUniPktNum"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRTxClientBroPktNum"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRelayDiscoverPktNum"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRelayRequestPktNum"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRelayDeclinePktNum"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRelayReleasePktNum"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRelayInformPktNum"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRelayOfferPktNum"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRelayAckPktNum"),
        ("RUIJIE-DHCP-RELAY-MIB", "ruijieDHCPRelayNakPktNum"))
)
if mibBuilder.loadTexts:
    ruijieDhcpRelayCountersObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieDhcpRelayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 104, 2, 1, 1)
)
ruijieDhcpRelayCompliance.setObjects(
    ("RUIJIE-DHCP-RELAY-MIB", "ruijieDhcpRelayCountersObjects")
)
if mibBuilder.loadTexts:
    ruijieDhcpRelayCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-DHCP-RELAY-MIB",
    **{"ruijieDhcpMIB": ruijieDhcpMIB,
       "ruijieDhcpMIBObjects": ruijieDhcpMIBObjects,
       "ruijieDhcpRelayMIBObjects": ruijieDhcpRelayMIBObjects,
       "ruijieDHCPRelayCycleStatus": ruijieDHCPRelayCycleStatus,
       "ruijieDhcpRelayCounters": ruijieDhcpRelayCounters,
       "ruijieDHCPRRxBadPktNum": ruijieDHCPRRxBadPktNum,
       "ruijieDHCPRRxServerPktNum": ruijieDHCPRRxServerPktNum,
       "ruijieDHCPRTxServerPktNum": ruijieDHCPRTxServerPktNum,
       "ruijieDHCPRRxClientPktNum": ruijieDHCPRRxClientPktNum,
       "ruijieDHCPRTxClientPktNum": ruijieDHCPRTxClientPktNum,
       "ruijieDHCPRRxClientUniPktNum": ruijieDHCPRRxClientUniPktNum,
       "ruijieDHCPRRxClientBroPktNum": ruijieDHCPRRxClientBroPktNum,
       "ruijieDHCPRTxClientUniPktNum": ruijieDHCPRTxClientUniPktNum,
       "ruijieDHCPRTxClientBroPktNum": ruijieDHCPRTxClientBroPktNum,
       "ruijieDHCPRelayDiscoverPktNum": ruijieDHCPRelayDiscoverPktNum,
       "ruijieDHCPRelayRequestPktNum": ruijieDHCPRelayRequestPktNum,
       "ruijieDHCPRelayDeclinePktNum": ruijieDHCPRelayDeclinePktNum,
       "ruijieDHCPRelayReleasePktNum": ruijieDHCPRelayReleasePktNum,
       "ruijieDHCPRelayInformPktNum": ruijieDHCPRelayInformPktNum,
       "ruijieDHCPRelayOfferPktNum": ruijieDHCPRelayOfferPktNum,
       "ruijieDHCPRelayAckPktNum": ruijieDHCPRelayAckPktNum,
       "ruijieDHCPRelayNakPktNum": ruijieDHCPRelayNakPktNum,
       "ruijieDhcpMIBConformance": ruijieDhcpMIBConformance,
       "ruijieDhcpMIBCompliances": ruijieDhcpMIBCompliances,
       "ruijieDhcpRelayCompliance": ruijieDhcpRelayCompliance,
       "ruijieDhcpMIBGroups": ruijieDhcpMIBGroups,
       "ruijieDhcpRelayCountersObjects": ruijieDhcpRelayCountersObjects}
)
