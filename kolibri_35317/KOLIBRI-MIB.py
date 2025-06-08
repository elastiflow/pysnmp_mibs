# SNMP MIB module (KOLIBRI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:59:40 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

kolibriSystems = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317)
)
if mibBuilder.loadTexts:
    kolibriSystems.setRevisions(
        ("2017-04-19 12:00",
         "2017-04-19 09:45",
         "2017-04-19 08:00",
         "2017-04-18 08:00",
         "2017-04-11 15:00",
         "2015-12-01 10:34",
         "2015-07-17 09:00",
         "2011-01-09 12:13")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Kolibri_ObjectIdentity = ObjectIdentity
kolibri = _Kolibri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1)
)
_KolibriCommon_ObjectIdentity = ObjectIdentity
kolibriCommon = _KolibriCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0)
)
_KolibriValue_ObjectIdentity = ObjectIdentity
kolibriValue = _KolibriValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1)
)
_KolibriClientValue_ObjectIdentity = ObjectIdentity
kolibriClientValue = _KolibriClientValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 1)
)
_KolibriClientConnection_Type = Integer32
_KolibriClientConnection_Object = MibScalar
kolibriClientConnection = _KolibriClientConnection_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 1, 1),
    _KolibriClientConnection_Type()
)
kolibriClientConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriClientConnection.setStatus("current")
_KolibriClientAddress_Type = IpAddress
_KolibriClientAddress_Object = MibScalar
kolibriClientAddress = _KolibriClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 1, 2),
    _KolibriClientAddress_Type()
)
kolibriClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriClientAddress.setStatus("current")
_KolibriAudioValue_ObjectIdentity = ObjectIdentity
kolibriAudioValue = _KolibriAudioValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 2)
)
_KolibriAudioAddress_Type = IpAddress
_KolibriAudioAddress_Object = MibScalar
kolibriAudioAddress = _KolibriAudioAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 2, 1),
    _KolibriAudioAddress_Type()
)
kolibriAudioAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriAudioAddress.setStatus("current")
_KolibriLogValue_ObjectIdentity = ObjectIdentity
kolibriLogValue = _KolibriLogValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 3)
)
_KolibriLogAddress_Type = IpAddress
_KolibriLogAddress_Object = MibScalar
kolibriLogAddress = _KolibriLogAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 3, 1),
    _KolibriLogAddress_Type()
)
kolibriLogAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriLogAddress.setStatus("current")
_KolibriGatewayValue_ObjectIdentity = ObjectIdentity
kolibriGatewayValue = _KolibriGatewayValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 4)
)
_KolibriGatewayConnection_Type = Integer32
_KolibriGatewayConnection_Object = MibScalar
kolibriGatewayConnection = _KolibriGatewayConnection_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 4, 1),
    _KolibriGatewayConnection_Type()
)
kolibriGatewayConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriGatewayConnection.setStatus("current")
_KolibriGatewayAddress_Type = IpAddress
_KolibriGatewayAddress_Object = MibScalar
kolibriGatewayAddress = _KolibriGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 4, 2),
    _KolibriGatewayAddress_Type()
)
kolibriGatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriGatewayAddress.setStatus("current")


class _KolibriGatewayName_Type(OctetString):
    """Custom type kolibriGatewayName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KolibriGatewayName_Type.__name__ = "OctetString"
_KolibriGatewayName_Object = MibScalar
kolibriGatewayName = _KolibriGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 4, 3),
    _KolibriGatewayName_Type()
)
kolibriGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriGatewayName.setStatus("current")
_KolibriCommValue_ObjectIdentity = ObjectIdentity
kolibriCommValue = _KolibriCommValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 5)
)
_KolibriCommAddress_Type = IpAddress
_KolibriCommAddress_Object = MibScalar
kolibriCommAddress = _KolibriCommAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 5, 1),
    _KolibriCommAddress_Type()
)
kolibriCommAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriCommAddress.setStatus("current")


class _KolibriCommReference_Type(OctetString):
    """Custom type kolibriCommReference based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KolibriCommReference_Type.__name__ = "OctetString"
_KolibriCommReference_Object = MibScalar
kolibriCommReference = _KolibriCommReference_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 5, 2),
    _KolibriCommReference_Type()
)
kolibriCommReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriCommReference.setStatus("current")


class _KolibriCommInstance_Type(Integer32):
    """Custom type kolibriCommInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_KolibriCommInstance_Type.__name__ = "Integer32"
_KolibriCommInstance_Object = MibScalar
kolibriCommInstance = _KolibriCommInstance_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 5, 3),
    _KolibriCommInstance_Type()
)
kolibriCommInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriCommInstance.setStatus("current")


class _KolibriCommDevice_Type(OctetString):
    """Custom type kolibriCommDevice based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KolibriCommDevice_Type.__name__ = "OctetString"
_KolibriCommDevice_Object = MibScalar
kolibriCommDevice = _KolibriCommDevice_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 5, 4),
    _KolibriCommDevice_Type()
)
kolibriCommDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriCommDevice.setStatus("current")


class _KolibriCommGateway_Type(OctetString):
    """Custom type kolibriCommGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KolibriCommGateway_Type.__name__ = "OctetString"
_KolibriCommGateway_Object = MibScalar
kolibriCommGateway = _KolibriCommGateway_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 5, 5),
    _KolibriCommGateway_Type()
)
kolibriCommGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriCommGateway.setStatus("current")
_KolibriControlValue_ObjectIdentity = ObjectIdentity
kolibriControlValue = _KolibriControlValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 6)
)
_KolibriControlAddress_Type = IpAddress
_KolibriControlAddress_Object = MibScalar
kolibriControlAddress = _KolibriControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 6, 1),
    _KolibriControlAddress_Type()
)
kolibriControlAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriControlAddress.setStatus("current")


class _KolibriControlStandby_Type(Integer32):
    """Custom type kolibriControlStandby based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_KolibriControlStandby_Type.__name__ = "Integer32"
_KolibriControlStandby_Object = MibScalar
kolibriControlStandby = _KolibriControlStandby_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 6, 2),
    _KolibriControlStandby_Type()
)
kolibriControlStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriControlStandby.setStatus("current")
_KolibriConfigValue_ObjectIdentity = ObjectIdentity
kolibriConfigValue = _KolibriConfigValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 7)
)
_KolibriConfigAddress_Type = IpAddress
_KolibriConfigAddress_Object = MibScalar
kolibriConfigAddress = _KolibriConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 7, 1),
    _KolibriConfigAddress_Type()
)
kolibriConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriConfigAddress.setStatus("current")
_KolibriLinkValue_ObjectIdentity = ObjectIdentity
kolibriLinkValue = _KolibriLinkValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 8)
)
_KolibriLinkAddress_Type = IpAddress
_KolibriLinkAddress_Object = MibScalar
kolibriLinkAddress = _KolibriLinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 8, 1),
    _KolibriLinkAddress_Type()
)
kolibriLinkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriLinkAddress.setStatus("current")
_KolibriDAIValue_ObjectIdentity = ObjectIdentity
kolibriDAIValue = _KolibriDAIValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 9)
)
_KolibriDAIAddress_Type = IpAddress
_KolibriDAIAddress_Object = MibScalar
kolibriDAIAddress = _KolibriDAIAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 9, 1),
    _KolibriDAIAddress_Type()
)
kolibriDAIAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriDAIAddress.setStatus("current")
_KolibriLoggingValue_ObjectIdentity = ObjectIdentity
kolibriLoggingValue = _KolibriLoggingValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 10)
)
_KolibriLoggingAddress_Type = IpAddress
_KolibriLoggingAddress_Object = MibScalar
kolibriLoggingAddress = _KolibriLoggingAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 10, 1),
    _KolibriLoggingAddress_Type()
)
kolibriLoggingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriLoggingAddress.setStatus("current")
_KolibriVideoValue_ObjectIdentity = ObjectIdentity
kolibriVideoValue = _KolibriVideoValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 11)
)
_KolibriVideoAddress_Type = IpAddress
_KolibriVideoAddress_Object = MibScalar
kolibriVideoAddress = _KolibriVideoAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 11, 1),
    _KolibriVideoAddress_Type()
)
kolibriVideoAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriVideoAddress.setStatus("current")
_KolibriMapValue_ObjectIdentity = ObjectIdentity
kolibriMapValue = _KolibriMapValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 12)
)
_KolibriMapAddress_Type = IpAddress
_KolibriMapAddress_Object = MibScalar
kolibriMapAddress = _KolibriMapAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 12, 1),
    _KolibriMapAddress_Type()
)
kolibriMapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriMapAddress.setStatus("current")
_KolibriInstanceValue_ObjectIdentity = ObjectIdentity
kolibriInstanceValue = _KolibriInstanceValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 13)
)


class _KolibriInstanceName_Type(OctetString):
    """Custom type kolibriInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KolibriInstanceName_Type.__name__ = "OctetString"
_KolibriInstanceName_Object = MibScalar
kolibriInstanceName = _KolibriInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 13, 1),
    _KolibriInstanceName_Type()
)
kolibriInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriInstanceName.setStatus("current")
_KolibriExtClientValue_ObjectIdentity = ObjectIdentity
kolibriExtClientValue = _KolibriExtClientValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 14)
)
_KolibriExtClientConnection_Type = Integer32
_KolibriExtClientConnection_Object = MibScalar
kolibriExtClientConnection = _KolibriExtClientConnection_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 14, 1),
    _KolibriExtClientConnection_Type()
)
kolibriExtClientConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriExtClientConnection.setStatus("current")


class _KolibriExtClientName_Type(OctetString):
    """Custom type kolibriExtClientName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KolibriExtClientName_Type.__name__ = "OctetString"
_KolibriExtClientName_Object = MibScalar
kolibriExtClientName = _KolibriExtClientName_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 14, 2),
    _KolibriExtClientName_Type()
)
kolibriExtClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriExtClientName.setStatus("current")
_KolibriExtClientTargetPort_Type = Integer32
_KolibriExtClientTargetPort_Object = MibScalar
kolibriExtClientTargetPort = _KolibriExtClientTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 1, 14, 3),
    _KolibriExtClientTargetPort_Type()
)
kolibriExtClientTargetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kolibriExtClientTargetPort.setStatus("current")
_KolibriGroups_ObjectIdentity = ObjectIdentity
kolibriGroups = _KolibriGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 2)
)
_KolibriDispatch_ObjectIdentity = ObjectIdentity
kolibriDispatch = _KolibriDispatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1)
)
_KoliDispatch_ObjectIdentity = ObjectIdentity
koliDispatch = _KoliDispatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1)
)
_KolibriService_ObjectIdentity = ObjectIdentity
kolibriService = _KolibriService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2)
)
_KoliAudio_ObjectIdentity = ObjectIdentity
koliAudio = _KoliAudio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 1)
)
_KoliControl_ObjectIdentity = ObjectIdentity
koliControl = _KoliControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2)
)
_KoliConfig_ObjectIdentity = ObjectIdentity
koliConfig = _KoliConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 3)
)
_KoliWatch_ObjectIdentity = ObjectIdentity
koliWatch = _KoliWatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 4)
)
_KoliDAI_ObjectIdentity = ObjectIdentity
koliDAI = _KoliDAI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 5)
)
_KoliArchive_ObjectIdentity = ObjectIdentity
koliArchive = _KoliArchive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 6)
)
_KoliAudioLog_ObjectIdentity = ObjectIdentity
koliAudioLog = _KoliAudioLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 7)
)
_KoliLog_ObjectIdentity = ObjectIdentity
koliLog = _KoliLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 8)
)
_KoliReportMon_ObjectIdentity = ObjectIdentity
koliReportMon = _KoliReportMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 9)
)
_KoliState_ObjectIdentity = ObjectIdentity
koliState = _KoliState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 10)
)
_KoliLogging_ObjectIdentity = ObjectIdentity
koliLogging = _KoliLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 11)
)
_KoliVideo_ObjectIdentity = ObjectIdentity
koliVideo = _KoliVideo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 12)
)
_KolibriGateway_ObjectIdentity = ObjectIdentity
kolibriGateway = _KolibriGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3)
)
_KoliTIG_ObjectIdentity = ObjectIdentity
koliTIG = _KoliTIG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1)
)
_KoliUCGW_ObjectIdentity = ObjectIdentity
koliUCGW = _KoliUCGW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 2)
)
_KoliWeb_ObjectIdentity = ObjectIdentity
koliWeb = _KoliWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 3)
)
_KoliATIA_ObjectIdentity = ObjectIdentity
koliATIA = _KoliATIA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 4)
)
_KoliCADI_ObjectIdentity = ObjectIdentity
koliCADI = _KoliCADI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 5)
)
_KoliSDR_ObjectIdentity = ObjectIdentity
koliSDR = _KoliSDR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 6)
)
_KoliPage_ObjectIdentity = ObjectIdentity
koliPage = _KoliPage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 7)
)
_KoliBPI_ObjectIdentity = ObjectIdentity
koliBPI = _KoliBPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 8)
)
_KoliJTS_ObjectIdentity = ObjectIdentity
koliJTS = _KoliJTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 9)
)
_KoliGPS_ObjectIdentity = ObjectIdentity
koliGPS = _KoliGPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 10)
)
_KoliXML_ObjectIdentity = ObjectIdentity
koliXML = _KoliXML_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 11)
)
_KoliProcess_ObjectIdentity = ObjectIdentity
koliProcess = _KoliProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 12)
)
_KoliMail_ObjectIdentity = ObjectIdentity
koliMail = _KoliMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 13)
)
_KoliMap_ObjectIdentity = ObjectIdentity
koliMap = _KoliMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 14)
)
_KoliDB_ObjectIdentity = ObjectIdentity
koliDB = _KoliDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 15)
)
_KolibriComm_ObjectIdentity = ObjectIdentity
kolibriComm = _KolibriComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4)
)
_KoliComm_ObjectIdentity = ObjectIdentity
koliComm = _KoliComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 1)
)
_KoliSIP_ObjectIdentity = ObjectIdentity
koliSIP = _KoliSIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 2)
)
_KoliDAMM_ObjectIdentity = ObjectIdentity
koliDAMM = _KoliDAMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 3)
)
_KoliTRBO_ObjectIdentity = ObjectIdentity
koliTRBO = _KoliTRBO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 4)
)
_KoliDCS_ObjectIdentity = ObjectIdentity
koliDCS = _KoliDCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 5)
)
_KoliTRBOComm_ObjectIdentity = ObjectIdentity
koliTRBOComm = _KoliTRBOComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6)
)
_KolibriLink_ObjectIdentity = ObjectIdentity
kolibriLink = _KolibriLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5)
)
_KoliLinkClient_ObjectIdentity = ObjectIdentity
koliLinkClient = _KoliLinkClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 1)
)
_KoliLinkServer_ObjectIdentity = ObjectIdentity
koliLinkServer = _KoliLinkServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 2)
)
_KoliLinkGPSGate_ObjectIdentity = ObjectIdentity
koliLinkGPSGate = _KoliLinkGPSGate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 3)
)
_KolibriDeployment_ObjectIdentity = ObjectIdentity
kolibriDeployment = _KolibriDeployment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100)
)
_KoliUpdateServer_ObjectIdentity = ObjectIdentity
koliUpdateServer = _KoliUpdateServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100, 1)
)
_KoliUpdateAgent_ObjectIdentity = ObjectIdentity
koliUpdateAgent = _KoliUpdateAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100, 2)
)

# Managed Objects groups

kolibriGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 0, 2, 1)
)
kolibriGroup.setObjects(
      *(("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"),
        ("KOLIBRI-MIB", "kolibriAudioAddress"),
        ("KOLIBRI-MIB", "kolibriLogAddress"),
        ("KOLIBRI-MIB", "kolibriGatewayConnection"),
        ("KOLIBRI-MIB", "kolibriGatewayAddress"),
        ("KOLIBRI-MIB", "kolibriGatewayName"),
        ("KOLIBRI-MIB", "kolibriCommAddress"),
        ("KOLIBRI-MIB", "kolibriCommReference"),
        ("KOLIBRI-MIB", "kolibriCommInstance"),
        ("KOLIBRI-MIB", "kolibriCommDevice"),
        ("KOLIBRI-MIB", "kolibriCommGateway"),
        ("KOLIBRI-MIB", "kolibriControlAddress"),
        ("KOLIBRI-MIB", "kolibriControlStandby"),
        ("KOLIBRI-MIB", "kolibriConfigAddress"),
        ("KOLIBRI-MIB", "kolibriLinkAddress"),
        ("KOLIBRI-MIB", "kolibriDAIAddress"),
        ("KOLIBRI-MIB", "kolibriLoggingAddress"),
        ("KOLIBRI-MIB", "kolibriVideoAddress"),
        ("KOLIBRI-MIB", "kolibriMapAddress"),
        ("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriExtClientConnection"),
        ("KOLIBRI-MIB", "kolibriExtClientName"),
        ("KOLIBRI-MIB", "kolibriExtClientTargetPort"))
)
if mibBuilder.loadTexts:
    kolibriGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-MIB",
    **{"kolibriSystems": kolibriSystems,
       "kolibri": kolibri,
       "kolibriCommon": kolibriCommon,
       "kolibriValue": kolibriValue,
       "kolibriClientValue": kolibriClientValue,
       "kolibriClientConnection": kolibriClientConnection,
       "kolibriClientAddress": kolibriClientAddress,
       "kolibriAudioValue": kolibriAudioValue,
       "kolibriAudioAddress": kolibriAudioAddress,
       "kolibriLogValue": kolibriLogValue,
       "kolibriLogAddress": kolibriLogAddress,
       "kolibriGatewayValue": kolibriGatewayValue,
       "kolibriGatewayConnection": kolibriGatewayConnection,
       "kolibriGatewayAddress": kolibriGatewayAddress,
       "kolibriGatewayName": kolibriGatewayName,
       "kolibriCommValue": kolibriCommValue,
       "kolibriCommAddress": kolibriCommAddress,
       "kolibriCommReference": kolibriCommReference,
       "kolibriCommInstance": kolibriCommInstance,
       "kolibriCommDevice": kolibriCommDevice,
       "kolibriCommGateway": kolibriCommGateway,
       "kolibriControlValue": kolibriControlValue,
       "kolibriControlAddress": kolibriControlAddress,
       "kolibriControlStandby": kolibriControlStandby,
       "kolibriConfigValue": kolibriConfigValue,
       "kolibriConfigAddress": kolibriConfigAddress,
       "kolibriLinkValue": kolibriLinkValue,
       "kolibriLinkAddress": kolibriLinkAddress,
       "kolibriDAIValue": kolibriDAIValue,
       "kolibriDAIAddress": kolibriDAIAddress,
       "kolibriLoggingValue": kolibriLoggingValue,
       "kolibriLoggingAddress": kolibriLoggingAddress,
       "kolibriVideoValue": kolibriVideoValue,
       "kolibriVideoAddress": kolibriVideoAddress,
       "kolibriMapValue": kolibriMapValue,
       "kolibriMapAddress": kolibriMapAddress,
       "kolibriInstanceValue": kolibriInstanceValue,
       "kolibriInstanceName": kolibriInstanceName,
       "kolibriExtClientValue": kolibriExtClientValue,
       "kolibriExtClientConnection": kolibriExtClientConnection,
       "kolibriExtClientName": kolibriExtClientName,
       "kolibriExtClientTargetPort": kolibriExtClientTargetPort,
       "kolibriGroups": kolibriGroups,
       "kolibriGroup": kolibriGroup,
       "kolibriDispatch": kolibriDispatch,
       "koliDispatch": koliDispatch,
       "kolibriService": kolibriService,
       "koliAudio": koliAudio,
       "koliControl": koliControl,
       "koliConfig": koliConfig,
       "koliWatch": koliWatch,
       "koliDAI": koliDAI,
       "koliArchive": koliArchive,
       "koliAudioLog": koliAudioLog,
       "koliLog": koliLog,
       "koliReportMon": koliReportMon,
       "koliState": koliState,
       "koliLogging": koliLogging,
       "koliVideo": koliVideo,
       "kolibriGateway": kolibriGateway,
       "koliTIG": koliTIG,
       "koliUCGW": koliUCGW,
       "koliWeb": koliWeb,
       "koliATIA": koliATIA,
       "koliCADI": koliCADI,
       "koliSDR": koliSDR,
       "koliPage": koliPage,
       "koliBPI": koliBPI,
       "koliJTS": koliJTS,
       "koliGPS": koliGPS,
       "koliXML": koliXML,
       "koliProcess": koliProcess,
       "koliMail": koliMail,
       "koliMap": koliMap,
       "koliDB": koliDB,
       "kolibriComm": kolibriComm,
       "koliComm": koliComm,
       "koliSIP": koliSIP,
       "koliDAMM": koliDAMM,
       "koliTRBO": koliTRBO,
       "koliDCS": koliDCS,
       "koliTRBOComm": koliTRBOComm,
       "kolibriLink": kolibriLink,
       "koliLinkClient": koliLinkClient,
       "koliLinkServer": koliLinkServer,
       "koliLinkGPSGate": koliLinkGPSGate,
       "kolibriDeployment": kolibriDeployment,
       "koliUpdateServer": koliUpdateServer,
       "koliUpdateAgent": koliUpdateAgent}
)
