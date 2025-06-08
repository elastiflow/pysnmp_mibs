# SNMP MIB module (RUIJIE-MAPINFO-MNG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-MAPINFO-MNG-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:12 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(radiusAccClientServerPortNumber,
 radiusAccServerAddress) = mibBuilder.importSymbols(
    "RADIUS-ACC-CLIENT-MIB",
    "radiusAccClientServerPortNumber",
    "radiusAccServerAddress")

(radiusAuthClientServerPortNumber,
 radiusAuthServerAddress) = mibBuilder.importSymbols(
    "RADIUS-AUTH-CLIENT-MIB",
    "radiusAuthClientServerPortNumber",
    "radiusAuthServerAddress")

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

ruijieMapinfoMngMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150)
)
if mibBuilder.loadTexts:
    ruijieMapinfoMngMIB.setRevisions(
        ("1970-01-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieMapinfoMngMIBObjects_ObjectIdentity = ObjectIdentity
ruijieMapinfoMngMIBObjects = _RuijieMapinfoMngMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1)
)
_RuijieUserObjects_ObjectIdentity = ObjectIdentity
ruijieUserObjects = _RuijieUserObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 1)
)
_RuijieUserTable_Object = MibTable
ruijieUserTable = _RuijieUserTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieUserTable.setStatus("current")
_RuijieUserEntry_Object = MibTableRow
ruijieUserEntry = _RuijieUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 1, 1, 1)
)
ruijieUserEntry.setIndexNames(
    (0, "RUIJIE-MAPINFO-MNG-MIB", "ruijieUserMacAddress"),
    (0, "RUIJIE-MAPINFO-MNG-MIB", "ruijieUserVid"),
)
if mibBuilder.loadTexts:
    ruijieUserEntry.setStatus("current")
_RuijieUserMacAddress_Type = MacAddress
_RuijieUserMacAddress_Object = MibTableColumn
ruijieUserMacAddress = _RuijieUserMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 1, 1, 1, 1),
    _RuijieUserMacAddress_Type()
)
ruijieUserMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUserMacAddress.setStatus("current")
_RuijieUserVid_Type = Unsigned32
_RuijieUserVid_Object = MibTableColumn
ruijieUserVid = _RuijieUserVid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 1, 1, 1, 2),
    _RuijieUserVid_Type()
)
ruijieUserVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUserVid.setStatus("current")
_RuijieUserDevMacAddress_Type = MacAddress
_RuijieUserDevMacAddress_Object = MibTableColumn
ruijieUserDevMacAddress = _RuijieUserDevMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 1, 1, 1, 3),
    _RuijieUserDevMacAddress_Type()
)
ruijieUserDevMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUserDevMacAddress.setStatus("current")
_RuijieUserDevSlot_Type = Unsigned32
_RuijieUserDevSlot_Object = MibTableColumn
ruijieUserDevSlot = _RuijieUserDevSlot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 1, 1, 1, 4),
    _RuijieUserDevSlot_Type()
)
ruijieUserDevSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUserDevSlot.setStatus("current")
_RuijieUserMapPort_Type = Unsigned32
_RuijieUserMapPort_Object = MibTableColumn
ruijieUserMapPort = _RuijieUserMapPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 1, 1, 1, 5),
    _RuijieUserMapPort_Type()
)
ruijieUserMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUserMapPort.setStatus("current")
_RuijieUserRowStatus_Type = ConfigStatus
_RuijieUserRowStatus_Object = MibTableColumn
ruijieUserRowStatus = _RuijieUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 1, 1, 1, 6),
    _RuijieUserRowStatus_Type()
)
ruijieUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieUserRowStatus.setStatus("current")
_RuijieFluxObjects_ObjectIdentity = ObjectIdentity
ruijieFluxObjects = _RuijieFluxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 2)
)
_RuijieFluxTable_Object = MibTable
ruijieFluxTable = _RuijieFluxTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieFluxTable.setStatus("current")
_RuijieFluxEntry_Object = MibTableRow
ruijieFluxEntry = _RuijieFluxEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 2, 1, 1)
)
ruijieFluxEntry.setIndexNames(
    (0, "RUIJIE-MAPINFO-MNG-MIB", "ruijieFluxDevMacAddress"),
    (0, "RUIJIE-MAPINFO-MNG-MIB", "ruijieFluxDevSlot"),
    (0, "RUIJIE-MAPINFO-MNG-MIB", "ruijieFluxMapPort"),
)
if mibBuilder.loadTexts:
    ruijieFluxEntry.setStatus("current")
_RuijieFluxDevMacAddress_Type = MacAddress
_RuijieFluxDevMacAddress_Object = MibTableColumn
ruijieFluxDevMacAddress = _RuijieFluxDevMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 2, 1, 1, 1),
    _RuijieFluxDevMacAddress_Type()
)
ruijieFluxDevMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFluxDevMacAddress.setStatus("current")
_RuijieFluxDevSlot_Type = Unsigned32
_RuijieFluxDevSlot_Object = MibTableColumn
ruijieFluxDevSlot = _RuijieFluxDevSlot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 2, 1, 1, 2),
    _RuijieFluxDevSlot_Type()
)
ruijieFluxDevSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFluxDevSlot.setStatus("current")
_RuijieFluxMapPort_Type = Unsigned32
_RuijieFluxMapPort_Object = MibTableColumn
ruijieFluxMapPort = _RuijieFluxMapPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 2, 1, 1, 3),
    _RuijieFluxMapPort_Type()
)
ruijieFluxMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFluxMapPort.setStatus("current")


class _RuijieFluxMapPortState_Type(Integer32):
    """Custom type ruijieFluxMapPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieFluxMapPortState_Type.__name__ = "Integer32"
_RuijieFluxMapPortState_Object = MibTableColumn
ruijieFluxMapPortState = _RuijieFluxMapPortState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 2, 1, 1, 4),
    _RuijieFluxMapPortState_Type()
)
ruijieFluxMapPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFluxMapPortState.setStatus("current")
_RuijieFluxInputBps_Type = Counter64
_RuijieFluxInputBps_Object = MibTableColumn
ruijieFluxInputBps = _RuijieFluxInputBps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 2, 1, 1, 5),
    _RuijieFluxInputBps_Type()
)
ruijieFluxInputBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFluxInputBps.setStatus("current")
_RuijieFluxOutputBps_Type = Counter64
_RuijieFluxOutputBps_Object = MibTableColumn
ruijieFluxOutputBps = _RuijieFluxOutputBps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 2, 1, 1, 6),
    _RuijieFluxOutputBps_Type()
)
ruijieFluxOutputBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFluxOutputBps.setStatus("current")
_RuijieFluxInputPackets_Type = Counter64
_RuijieFluxInputPackets_Object = MibTableColumn
ruijieFluxInputPackets = _RuijieFluxInputPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 2, 1, 1, 7),
    _RuijieFluxInputPackets_Type()
)
ruijieFluxInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFluxInputPackets.setStatus("current")
_RuijieFluxOutputPackets_Type = Counter64
_RuijieFluxOutputPackets_Object = MibTableColumn
ruijieFluxOutputPackets = _RuijieFluxOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 2, 1, 1, 8),
    _RuijieFluxOutputPackets_Type()
)
ruijieFluxOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFluxOutputPackets.setStatus("current")
_RuijieFluxInputBytes_Type = Counter64
_RuijieFluxInputBytes_Object = MibTableColumn
ruijieFluxInputBytes = _RuijieFluxInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 2, 1, 1, 9),
    _RuijieFluxInputBytes_Type()
)
ruijieFluxInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFluxInputBytes.setStatus("current")
_RuijieFluxOutputBytes_Type = Counter64
_RuijieFluxOutputBytes_Object = MibTableColumn
ruijieFluxOutputBytes = _RuijieFluxOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 2, 1, 1, 10),
    _RuijieFluxOutputBytes_Type()
)
ruijieFluxOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFluxOutputBytes.setStatus("current")
_RuijieFluxRowStatus_Type = ConfigStatus
_RuijieFluxRowStatus_Object = MibTableColumn
ruijieFluxRowStatus = _RuijieFluxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 1, 2, 1, 1, 11),
    _RuijieFluxRowStatus_Type()
)
ruijieFluxRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieFluxRowStatus.setStatus("current")
_RuijieMapinfoMngMIBConformance_ObjectIdentity = ObjectIdentity
ruijieMapinfoMngMIBConformance = _RuijieMapinfoMngMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 2)
)
_RuijieMapinfoMngMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieMapinfoMngMIBCompliances = _RuijieMapinfoMngMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 2, 1)
)
_RuijieMapinfoMngMIBGroups_ObjectIdentity = ObjectIdentity
ruijieMapinfoMngMIBGroups = _RuijieMapinfoMngMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 2, 2)
)

# Managed Objects groups

ruijieUserMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 2, 2, 1)
)
ruijieUserMIBGroup.setObjects(
      *(("RUIJIE-MAPINFO-MNG-MIB", "ruijieUserMacAddress"),
        ("RUIJIE-MAPINFO-MNG-MIB", "ruijieUserVid"),
        ("RUIJIE-MAPINFO-MNG-MIB", "ruijieUserDevMacAddress"),
        ("RUIJIE-MAPINFO-MNG-MIB", "ruijieUserDevSlot"),
        ("RUIJIE-MAPINFO-MNG-MIB", "ruijieUserMapPort"),
        ("RUIJIE-MAPINFO-MNG-MIB", "ruijieUserRowStatus"))
)
if mibBuilder.loadTexts:
    ruijieUserMIBGroup.setStatus("current")

ruijieFluxMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 2, 2, 2)
)
ruijieFluxMIBGroup.setObjects(
      *(("RUIJIE-MAPINFO-MNG-MIB", "ruijieFluxDevMacAddress"),
        ("RUIJIE-MAPINFO-MNG-MIB", "ruijieFluxDevSlot"),
        ("RUIJIE-MAPINFO-MNG-MIB", "ruijieFluxMapPort"),
        ("RUIJIE-MAPINFO-MNG-MIB", "ruijieFluxMapPortState"),
        ("RUIJIE-MAPINFO-MNG-MIB", "ruijieFluxInputBps"),
        ("RUIJIE-MAPINFO-MNG-MIB", "ruijieFluxOutputBps"),
        ("RUIJIE-MAPINFO-MNG-MIB", "ruijieFluxInputPackets"),
        ("RUIJIE-MAPINFO-MNG-MIB", "ruijieFluxOutputPackets"),
        ("RUIJIE-MAPINFO-MNG-MIB", "ruijieFluxInputBytes"),
        ("RUIJIE-MAPINFO-MNG-MIB", "ruijieFluxOutputBytes"),
        ("RUIJIE-MAPINFO-MNG-MIB", "ruijieFluxRowStatus"))
)
if mibBuilder.loadTexts:
    ruijieFluxMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieMapinfoMngMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 150, 2, 1, 1)
)
ruijieMapinfoMngMIBCompliance.setObjects(
      *(("RUIJIE-MAPINFO-MNG-MIB", "ruijieUserMIBGroup"),
        ("RUIJIE-MAPINFO-MNG-MIB", "ruijieFluxMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieMapinfoMngMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-MAPINFO-MNG-MIB",
    **{"ruijieMapinfoMngMIB": ruijieMapinfoMngMIB,
       "ruijieMapinfoMngMIBObjects": ruijieMapinfoMngMIBObjects,
       "ruijieUserObjects": ruijieUserObjects,
       "ruijieUserTable": ruijieUserTable,
       "ruijieUserEntry": ruijieUserEntry,
       "ruijieUserMacAddress": ruijieUserMacAddress,
       "ruijieUserVid": ruijieUserVid,
       "ruijieUserDevMacAddress": ruijieUserDevMacAddress,
       "ruijieUserDevSlot": ruijieUserDevSlot,
       "ruijieUserMapPort": ruijieUserMapPort,
       "ruijieUserRowStatus": ruijieUserRowStatus,
       "ruijieFluxObjects": ruijieFluxObjects,
       "ruijieFluxTable": ruijieFluxTable,
       "ruijieFluxEntry": ruijieFluxEntry,
       "ruijieFluxDevMacAddress": ruijieFluxDevMacAddress,
       "ruijieFluxDevSlot": ruijieFluxDevSlot,
       "ruijieFluxMapPort": ruijieFluxMapPort,
       "ruijieFluxMapPortState": ruijieFluxMapPortState,
       "ruijieFluxInputBps": ruijieFluxInputBps,
       "ruijieFluxOutputBps": ruijieFluxOutputBps,
       "ruijieFluxInputPackets": ruijieFluxInputPackets,
       "ruijieFluxOutputPackets": ruijieFluxOutputPackets,
       "ruijieFluxInputBytes": ruijieFluxInputBytes,
       "ruijieFluxOutputBytes": ruijieFluxOutputBytes,
       "ruijieFluxRowStatus": ruijieFluxRowStatus,
       "ruijieMapinfoMngMIBConformance": ruijieMapinfoMngMIBConformance,
       "ruijieMapinfoMngMIBCompliances": ruijieMapinfoMngMIBCompliances,
       "ruijieMapinfoMngMIBCompliance": ruijieMapinfoMngMIBCompliance,
       "ruijieMapinfoMngMIBGroups": ruijieMapinfoMngMIBGroups,
       "ruijieUserMIBGroup": ruijieUserMIBGroup,
       "ruijieFluxMIBGroup": ruijieFluxMIBGroup}
)
