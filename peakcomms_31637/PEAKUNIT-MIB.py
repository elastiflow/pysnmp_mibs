# SNMP MIB module (PEAKUNIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKUNIT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:02 2025
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

(ChannelInternalStateType,
 ChannelModeType,
 ChannelNumberType,
 FaultType,
 OnOffType,
 OnlineOfflineType,
 RedundancyModeType,
 RedundancyPriorityType,
 RedundancyTypeType,
 RemoteLocalType,
 YesNoType,
 unit) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "ChannelInternalStateType",
    "ChannelModeType",
    "ChannelNumberType",
    "FaultType",
    "OnOffType",
    "OnlineOfflineType",
    "RedundancyModeType",
    "RedundancyPriorityType",
    "RedundancyTypeType",
    "RemoteLocalType",
    "YesNoType",
    "unit")

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

peakUnitModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 2)
)
if mibBuilder.loadTexts:
    peakUnitModule.setRevisions(
        ("2015-09-15 10:00",
         "2014-06-13 09:00",
         "2011-11-30 09:00",
         "2011-06-15 09:00",
         "2011-03-08 09:00",
         "2010-06-21 09:00",
         "2010-04-30 09:00",
         "2009-12-16 09:00",
         "2008-12-03 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UnitType_Type = OctetString
_UnitType_Object = MibScalar
unitType = _UnitType_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 2, 1),
    _UnitType_Type()
)
unitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitType.setStatus("current")


class _UnitSerialNo_Type(Integer32):
    """Custom type unitSerialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_UnitSerialNo_Type.__name__ = "Integer32"
_UnitSerialNo_Object = MibScalar
unitSerialNo = _UnitSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 2, 2),
    _UnitSerialNo_Type()
)
unitSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSerialNo.setStatus("current")
_UnitSoftwareVersion_Type = OctetString
_UnitSoftwareVersion_Object = MibScalar
unitSoftwareVersion = _UnitSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 2, 3),
    _UnitSoftwareVersion_Type()
)
unitSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSoftwareVersion.setStatus("current")
_UnitOnline_Type = OnlineOfflineType
_UnitOnline_Object = MibScalar
unitOnline = _UnitOnline_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 2, 4),
    _UnitOnline_Type()
)
unitOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitOnline.setStatus("current")
_UnitRemote_Type = RemoteLocalType
_UnitRemote_Object = MibScalar
unitRemote = _UnitRemote_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 2, 5),
    _UnitRemote_Type()
)
unitRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitRemote.setStatus("current")
_UnitExternalRef_Type = OnOffType
_UnitExternalRef_Object = MibScalar
unitExternalRef = _UnitExternalRef_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 2, 6),
    _UnitExternalRef_Type()
)
unitExternalRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitExternalRef.setStatus("current")
_UnitSummaryAlarm_Type = FaultType
_UnitSummaryAlarm_Object = MibScalar
unitSummaryAlarm = _UnitSummaryAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 2, 7),
    _UnitSummaryAlarm_Type()
)
unitSummaryAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSummaryAlarm.setStatus("current")
_UnitConvGroups_ObjectIdentity = ObjectIdentity
unitConvGroups = _UnitConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 2, 10)
)
_UnitConvConformance_ObjectIdentity = ObjectIdentity
unitConvConformance = _UnitConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 2, 11)
)
_UnitReset_Type = YesNoType
_UnitReset_Object = MibScalar
unitReset = _UnitReset_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 2, 99),
    _UnitReset_Type()
)
unitReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitReset.setStatus("current")
_UnitOKSince_Type = OctetString
_UnitOKSince_Object = MibScalar
unitOKSince = _UnitOKSince_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 2, 100),
    _UnitOKSince_Type()
)
unitOKSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitOKSince.setStatus("current")
_PeakEthernetModule_ObjectIdentity = ObjectIdentity
peakEthernetModule = _PeakEthernetModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 100)
)
_EthernetDHCP_Type = OnOffType
_EthernetDHCP_Object = MibScalar
ethernetDHCP = _EthernetDHCP_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 100, 1),
    _EthernetDHCP_Type()
)
ethernetDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetDHCP.setStatus("current")


class _EthernetIPv4Address_Type(OctetString):
    """Custom type ethernetIPv4Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_EthernetIPv4Address_Type.__name__ = "OctetString"
_EthernetIPv4Address_Object = MibScalar
ethernetIPv4Address = _EthernetIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 100, 2),
    _EthernetIPv4Address_Type()
)
ethernetIPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetIPv4Address.setStatus("current")


class _EthernetSubnetMask_Type(OctetString):
    """Custom type ethernetSubnetMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_EthernetSubnetMask_Type.__name__ = "OctetString"
_EthernetSubnetMask_Object = MibScalar
ethernetSubnetMask = _EthernetSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 100, 3),
    _EthernetSubnetMask_Type()
)
ethernetSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetSubnetMask.setStatus("current")


class _EthernetGateway_Type(OctetString):
    """Custom type ethernetGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_EthernetGateway_Type.__name__ = "OctetString"
_EthernetGateway_Object = MibScalar
ethernetGateway = _EthernetGateway_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 100, 4),
    _EthernetGateway_Type()
)
ethernetGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetGateway.setStatus("current")
_EthernetTCPPort_Type = Integer32
_EthernetTCPPort_Object = MibScalar
ethernetTCPPort = _EthernetTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 100, 5),
    _EthernetTCPPort_Type()
)
ethernetTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetTCPPort.setStatus("current")


class _EthernetSNMPTrapAddress_Type(OctetString):
    """Custom type ethernetSNMPTrapAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_EthernetSNMPTrapAddress_Type.__name__ = "OctetString"
_EthernetSNMPTrapAddress_Object = MibScalar
ethernetSNMPTrapAddress = _EthernetSNMPTrapAddress_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 100, 6),
    _EthernetSNMPTrapAddress_Type()
)
ethernetSNMPTrapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetSNMPTrapAddress.setStatus("current")
_EthernetUpdateSettings_Type = YesNoType
_EthernetUpdateSettings_Object = MibScalar
ethernetUpdateSettings = _EthernetUpdateSettings_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 100, 7),
    _EthernetUpdateSettings_Type()
)
ethernetUpdateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetUpdateSettings.setStatus("current")
_EthernetTCPTimeout_Type = Integer32
_EthernetTCPTimeout_Object = MibScalar
ethernetTCPTimeout = _EthernetTCPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 100, 8),
    _EthernetTCPTimeout_Type()
)
ethernetTCPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetTCPTimeout.setStatus("current")
_EthernetConvGroups_ObjectIdentity = ObjectIdentity
ethernetConvGroups = _EthernetConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 100, 10)
)
_EthernetConvConformance_ObjectIdentity = ObjectIdentity
ethernetConvConformance = _EthernetConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 100, 11)
)
_PeakRedundancyModule_ObjectIdentity = ObjectIdentity
peakRedundancyModule = _PeakRedundancyModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 110)
)
_RedundancyOnlineStatus_Type = OnlineOfflineType
_RedundancyOnlineStatus_Object = MibScalar
redundancyOnlineStatus = _RedundancyOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 110, 1),
    _RedundancyOnlineStatus_Type()
)
redundancyOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyOnlineStatus.setStatus("current")
_RedundancyType_Type = RedundancyTypeType
_RedundancyType_Object = MibScalar
redundancyType = _RedundancyType_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 110, 2),
    _RedundancyType_Type()
)
redundancyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyType.setStatus("current")
_RedundancyMode_Type = RedundancyModeType
_RedundancyMode_Object = MibScalar
redundancyMode = _RedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 110, 3),
    _RedundancyMode_Type()
)
redundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyMode.setStatus("current")


class _RedundancyIdentifier_Type(OctetString):
    """Custom type redundancyIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_RedundancyIdentifier_Type.__name__ = "OctetString"
_RedundancyIdentifier_Object = MibScalar
redundancyIdentifier = _RedundancyIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 110, 4),
    _RedundancyIdentifier_Type()
)
redundancyIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyIdentifier.setStatus("current")
_RedundancyPriority_Type = RedundancyPriorityType
_RedundancyPriority_Object = MibScalar
redundancyPriority = _RedundancyPriority_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 110, 5),
    _RedundancyPriority_Type()
)
redundancyPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyPriority.setStatus("current")


class _RedundancyRedundancyStatus_Type(OctetString):
    """Custom type redundancyRedundancyStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_RedundancyRedundancyStatus_Type.__name__ = "OctetString"
_RedundancyRedundancyStatus_Object = MibScalar
redundancyRedundancyStatus = _RedundancyRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 110, 6),
    _RedundancyRedundancyStatus_Type()
)
redundancyRedundancyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyRedundancyStatus.setStatus("current")


class _RedundancyCoaxPosition_Type(OctetString):
    """Custom type redundancyCoaxPosition based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_RedundancyCoaxPosition_Type.__name__ = "OctetString"
_RedundancyCoaxPosition_Object = MibScalar
redundancyCoaxPosition = _RedundancyCoaxPosition_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 110, 7),
    _RedundancyCoaxPosition_Type()
)
redundancyCoaxPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyCoaxPosition.setStatus("current")
_RedundancySystemNumber_Type = Integer32
_RedundancySystemNumber_Object = MibScalar
redundancySystemNumber = _RedundancySystemNumber_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 110, 8),
    _RedundancySystemNumber_Type()
)
redundancySystemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancySystemNumber.setStatus("current")
_RedundancyConvGroups_ObjectIdentity = ObjectIdentity
redundancyConvGroups = _RedundancyConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 110, 10)
)
_RedundancyConvConformance_ObjectIdentity = ObjectIdentity
redundancyConvConformance = _RedundancyConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 110, 11)
)
_PeakUPCChannelModule_ObjectIdentity = ObjectIdentity
peakUPCChannelModule = _PeakUPCChannelModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 120)
)
_UpcChannelState_Type = ChannelInternalStateType
_UpcChannelState_Object = MibScalar
upcChannelState = _UpcChannelState_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 120, 1),
    _UpcChannelState_Type()
)
upcChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upcChannelState.setStatus("current")
_UpcChannelNo_Type = ChannelNumberType
_UpcChannelNo_Object = MibScalar
upcChannelNo = _UpcChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 120, 2),
    _UpcChannelNo_Type()
)
upcChannelNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upcChannelNo.setStatus("current")
_UpcChannelMode_Type = ChannelModeType
_UpcChannelMode_Object = MibScalar
upcChannelMode = _UpcChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 120, 3),
    _UpcChannelMode_Type()
)
upcChannelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upcChannelMode.setStatus("current")
_UpcChannelAttenuation_Type = OctetString
_UpcChannelAttenuation_Object = MibScalar
upcChannelAttenuation = _UpcChannelAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 120, 4),
    _UpcChannelAttenuation_Type()
)
upcChannelAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upcChannelAttenuation.setStatus("current")
_UpcChannelCompRange_Type = OctetString
_UpcChannelCompRange_Object = MibScalar
upcChannelCompRange = _UpcChannelCompRange_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 120, 5),
    _UpcChannelCompRange_Type()
)
upcChannelCompRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upcChannelCompRange.setStatus("current")
_UpcChannelConvGroups_ObjectIdentity = ObjectIdentity
upcChannelConvGroups = _UpcChannelConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 120, 10)
)
_UpcChannelConvConformance_ObjectIdentity = ObjectIdentity
upcChannelConvConformance = _UpcChannelConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 120, 11)
)

# Managed Objects groups

unitCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 2, 10, 1)
)
unitCNFReqGrp.setObjects(
      *(("PEAKUNIT-MIB", "unitType"),
        ("PEAKUNIT-MIB", "unitSerialNo"),
        ("PEAKUNIT-MIB", "unitSoftwareVersion"),
        ("PEAKUNIT-MIB", "unitOnline"),
        ("PEAKUNIT-MIB", "unitRemote"),
        ("PEAKUNIT-MIB", "unitExternalRef"),
        ("PEAKUNIT-MIB", "unitSummaryAlarm"),
        ("PEAKUNIT-MIB", "unitOKSince"),
        ("PEAKUNIT-MIB", "unitReset"))
)
if mibBuilder.loadTexts:
    unitCNFReqGrp.setStatus("current")

ethernetCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 100, 10, 1)
)
ethernetCNFReqGrp.setObjects(
      *(("PEAKUNIT-MIB", "ethernetDHCP"),
        ("PEAKUNIT-MIB", "ethernetIPv4Address"),
        ("PEAKUNIT-MIB", "ethernetSubnetMask"),
        ("PEAKUNIT-MIB", "ethernetGateway"),
        ("PEAKUNIT-MIB", "ethernetTCPPort"),
        ("PEAKUNIT-MIB", "ethernetSNMPTrapAddress"),
        ("PEAKUNIT-MIB", "ethernetUpdateSettings"),
        ("PEAKUNIT-MIB", "ethernetTCPTimeout"))
)
if mibBuilder.loadTexts:
    ethernetCNFReqGrp.setStatus("current")

redundancyCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 110, 10, 1)
)
redundancyCNFReqGrp.setObjects(
      *(("PEAKUNIT-MIB", "redundancyOnlineStatus"),
        ("PEAKUNIT-MIB", "redundancyMode"),
        ("PEAKUNIT-MIB", "redundancyIdentifier"),
        ("PEAKUNIT-MIB", "redundancyRedundancyStatus"),
        ("PEAKUNIT-MIB", "redundancyCoaxPosition"))
)
if mibBuilder.loadTexts:
    redundancyCNFReqGrp.setStatus("current")

redundancyCNFSystemGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 110, 10, 2)
)
redundancyCNFSystemGrp.setObjects(
      *(("PEAKUNIT-MIB", "redundancyType"),
        ("PEAKUNIT-MIB", "redundancyPriority"),
        ("PEAKUNIT-MIB", "redundancySystemNumber"))
)
if mibBuilder.loadTexts:
    redundancyCNFSystemGrp.setStatus("current")

upcChannelCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 120, 10, 1)
)
upcChannelCNFReqGrp.setObjects(
      *(("PEAKUNIT-MIB", "upcChannelState"),
        ("PEAKUNIT-MIB", "upcChannelNo"),
        ("PEAKUNIT-MIB", "upcChannelMode"),
        ("PEAKUNIT-MIB", "upcChannelAttenuation"),
        ("PEAKUNIT-MIB", "upcChannelCompRange"))
)
if mibBuilder.loadTexts:
    upcChannelCNFReqGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

unitCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 2, 11, 1)
)
unitCNFCompliance.setObjects(
    ("PEAKUNIT-MIB", "unitCNFReqGrp")
)
if mibBuilder.loadTexts:
    unitCNFCompliance.setStatus(
        "current"
    )

ethernetCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 100, 11, 1)
)
ethernetCNFCompliance.setObjects(
    ("PEAKUNIT-MIB", "ethernetCNFReqGrp")
)
if mibBuilder.loadTexts:
    ethernetCNFCompliance.setStatus(
        "current"
    )

redundancyCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 110, 11, 1)
)
redundancyCNFCompliance.setObjects(
      *(("PEAKUNIT-MIB", "redundancyCNFReqGrp"),
        ("PEAKUNIT-MIB", "redundancyCNFSystemGrp"))
)
if mibBuilder.loadTexts:
    redundancyCNFCompliance.setStatus(
        "current"
    )

upcChannelCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2, 120, 11, 1)
)
upcChannelCNFCompliance.setObjects(
    ("PEAKUNIT-MIB", "upcChannelCNFReqGrp")
)
if mibBuilder.loadTexts:
    upcChannelCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKUNIT-MIB",
    **{"peakUnitModule": peakUnitModule,
       "unitType": unitType,
       "unitSerialNo": unitSerialNo,
       "unitSoftwareVersion": unitSoftwareVersion,
       "unitOnline": unitOnline,
       "unitRemote": unitRemote,
       "unitExternalRef": unitExternalRef,
       "unitSummaryAlarm": unitSummaryAlarm,
       "unitConvGroups": unitConvGroups,
       "unitCNFReqGrp": unitCNFReqGrp,
       "unitConvConformance": unitConvConformance,
       "unitCNFCompliance": unitCNFCompliance,
       "unitReset": unitReset,
       "unitOKSince": unitOKSince,
       "peakEthernetModule": peakEthernetModule,
       "ethernetDHCP": ethernetDHCP,
       "ethernetIPv4Address": ethernetIPv4Address,
       "ethernetSubnetMask": ethernetSubnetMask,
       "ethernetGateway": ethernetGateway,
       "ethernetTCPPort": ethernetTCPPort,
       "ethernetSNMPTrapAddress": ethernetSNMPTrapAddress,
       "ethernetUpdateSettings": ethernetUpdateSettings,
       "ethernetTCPTimeout": ethernetTCPTimeout,
       "ethernetConvGroups": ethernetConvGroups,
       "ethernetCNFReqGrp": ethernetCNFReqGrp,
       "ethernetConvConformance": ethernetConvConformance,
       "ethernetCNFCompliance": ethernetCNFCompliance,
       "peakRedundancyModule": peakRedundancyModule,
       "redundancyOnlineStatus": redundancyOnlineStatus,
       "redundancyType": redundancyType,
       "redundancyMode": redundancyMode,
       "redundancyIdentifier": redundancyIdentifier,
       "redundancyPriority": redundancyPriority,
       "redundancyRedundancyStatus": redundancyRedundancyStatus,
       "redundancyCoaxPosition": redundancyCoaxPosition,
       "redundancySystemNumber": redundancySystemNumber,
       "redundancyConvGroups": redundancyConvGroups,
       "redundancyCNFReqGrp": redundancyCNFReqGrp,
       "redundancyCNFSystemGrp": redundancyCNFSystemGrp,
       "redundancyConvConformance": redundancyConvConformance,
       "redundancyCNFCompliance": redundancyCNFCompliance,
       "peakUPCChannelModule": peakUPCChannelModule,
       "upcChannelState": upcChannelState,
       "upcChannelNo": upcChannelNo,
       "upcChannelMode": upcChannelMode,
       "upcChannelAttenuation": upcChannelAttenuation,
       "upcChannelCompRange": upcChannelCompRange,
       "upcChannelConvGroups": upcChannelConvGroups,
       "upcChannelCNFReqGrp": upcChannelCNFReqGrp,
       "upcChannelConvConformance": upcChannelConvConformance,
       "upcChannelCNFCompliance": upcChannelCNFCompliance}
)
