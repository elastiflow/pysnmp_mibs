# SNMP MIB module (Hagedorn-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/hagedorn_40822/Hagedorn-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:28:10 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hagedorn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 40822)
)
if mibBuilder.loadTexts:
    hagedorn.setRevisions(
        ("2016-06-21 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TMGGeneralState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("tcsStateUnknown", 0),
          ("tcsStateOk", 1),
          ("tcsStateNok", 2),
          ("tcsStateWOEX", 3),
          ("tcsStateWORE", 4),
          ("tcsStateBLEX", 5),
          ("tcsStateBLID", 6),
          ("tcsStateBLRE", 7),
          ("tcsStateTEEX", 8),
          ("tcsStateSEOU", 9),
          ("tcsStateSENH", 10))
    )



class TMGSessionState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("loginIn", 1),
          ("loginConfirm", 2))
    )



class ComponentState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ok", 1),
          ("nok", 2))
    )



class CrysCallCommType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("p2p", 0),
          ("p2mp", 1))
    )



class CrysCallTalkerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("client", 0),
          ("tetra", 1),
          ("tetraAndClient", 254),
          ("none", 255))
    )



class IPRTChannelState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noGroup", 0),
          ("trying", 1),
          ("selectedGroup", 2))
    )



class IPRTChannelDevice(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("devUnknown", 0),
          ("devTetra", 1),
          ("devIpru", 2),
          ("devPbx", 3),
          ("devDrgw", 4))
    )



class IPRTChannelCommType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commTypeUnknown", 0),
          ("commTypeIndividual", 1),
          ("commTypeGroup", 2))
    )



class IPRTGeneralState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("login", 1),
          ("online", 2),
          ("closing", 3),
          ("error", 4))
    )



class IPRTConnectionsState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ok", 1),
          ("nok", 2))
    )



class IPRTAudioBoxDevice(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("desktop", 1),
          ("handset", 2),
          ("headset", 3),
          ("intern", 4),
          ("line", 5))
    )



class IPRTAudioNoiseGate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )



class TIPRUProcState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("init", 1),
          ("online", 2),
          ("waitToReboot", 3))
    )



class TIPRUAudioState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("online", 1),
          ("fwUpdate", 2))
    )



class TIPRURadioState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("idle", 1),
          ("calling", 2),
          ("ringing", 3),
          ("online", 4),
          ("off", 5),
          ("grantedMe", 6),
          ("grantedOther", 7),
          ("readFolders", 8))
    )



class TIPRUMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("tmo", 1),
          ("dmo", 2),
          ("gateway", 3),
          ("repeater", 4))
    )



class TIPRURSP(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )



class TAudioBoxProcState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("init", 1),
          ("online", 2),
          ("waitToReboot", 3))
    )



class TAudioBoxAudioState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("online", 1),
          ("fwUpdate", 2))
    )



class TRecorderServiceState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("init", -1),
          ("ok", 0),
          ("error", 1))
    )



class TRecorderDatabaseState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("ok", 0),
          ("error", 1))
    )



class TSystemConfigWebServiceState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("error", 1))
    )



class TSystemConfigXmlDocState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("error", 1))
    )



class TSystemConfigDatabaseState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("ok", 0),
          ("error", 1))
    )



class TConnectionState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("error", 1))
    )



class TTimeLimitUnit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hour", 0),
          ("day", 1),
          ("month", 2))
    )



class TTmgProxyServiceState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -2),
          ("error", -1),
          ("ok", 0),
          ("deactivated", 1))
    )



class TGeneralState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -2),
          ("error", -1),
          ("ok", 0))
    )



class TLicenceState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -1),
          ("valid", 0))
    )



class TDrGwClientType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 0),
          ("sip", 1),
          ("soap", 2))
    )



class TClientConnectionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )



class TClientState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("notConnected", -1),
          ("connected", 0))
    )



class ChannelState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noGroup", 0),
          ("trying", 1),
          ("selectedGroup", 2))
    )



class ChannelDevice(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("devUnknown", 0),
          ("devTetra", 1),
          ("devIpru", 2),
          ("devPbx", 3),
          ("devDrgw", 4))
    )



class ChannelCommType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commTypeUnknown", 0),
          ("commTypeIndividual", 1),
          ("commTypeGroup", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Tmg_ObjectIdentity = ObjectIdentity
tmg = _Tmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 1)
)
if mibBuilder.loadTexts:
    tmg.setStatus("current")
_TmgGeneral_ObjectIdentity = ObjectIdentity
tmgGeneral = _TmgGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 1, 1)
)
if mibBuilder.loadTexts:
    tmgGeneral.setStatus("current")
_TmgGenStateCrypto_Type = ComponentState
_TmgGenStateCrypto_Object = MibScalar
tmgGenStateCrypto = _TmgGenStateCrypto_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 1, 1),
    _TmgGenStateCrypto_Type()
)
tmgGenStateCrypto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmgGenStateCrypto.setStatus("current")
_TmgGenStateRATS_Type = ComponentState
_TmgGenStateRATS_Object = MibScalar
tmgGenStateRATS = _TmgGenStateRATS_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 1, 2),
    _TmgGenStateRATS_Type()
)
tmgGenStateRATS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmgGenStateRATS.setStatus("current")
_TmgGenStateE1C_Type = ComponentState
_TmgGenStateE1C_Object = MibScalar
tmgGenStateE1C = _TmgGenStateE1C_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 1, 3),
    _TmgGenStateE1C_Type()
)
tmgGenStateE1C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmgGenStateE1C.setStatus("current")
_TmgSessions_ObjectIdentity = ObjectIdentity
tmgSessions = _TmgSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2)
)
if mibBuilder.loadTexts:
    tmgSessions.setStatus("current")
_TmgSessionsTable_Object = MibTable
tmgSessionsTable = _TmgSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tmgSessionsTable.setStatus("current")
_TmgSessionsTableEntry_Object = MibTableRow
tmgSessionsTableEntry = _TmgSessionsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1)
)
tmgSessionsTableEntry.setIndexNames(
    (0, "Hagedorn-MIB", "tmgSessionsTableIdx"),
)
if mibBuilder.loadTexts:
    tmgSessionsTableEntry.setStatus("current")


class _TmgSessionsTableIdx_Type(Integer32):
    """Custom type tmgSessionsTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmgSessionsTableIdx_Type.__name__ = "Integer32"
_TmgSessionsTableIdx_Object = MibTableColumn
tmgSessionsTableIdx = _TmgSessionsTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 1),
    _TmgSessionsTableIdx_Type()
)
tmgSessionsTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmgSessionsTableIdx.setStatus("current")
_TmgSessionsTableRowStatus_Type = RowStatus
_TmgSessionsTableRowStatus_Object = MibTableColumn
tmgSessionsTableRowStatus = _TmgSessionsTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 2),
    _TmgSessionsTableRowStatus_Type()
)
tmgSessionsTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmgSessionsTableRowStatus.setStatus("current")
_TmgSessionsTableISSI_Type = Integer32
_TmgSessionsTableISSI_Object = MibTableColumn
tmgSessionsTableISSI = _TmgSessionsTableISSI_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 3),
    _TmgSessionsTableISSI_Type()
)
tmgSessionsTableISSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableISSI.setStatus("current")
_TmgSessionsTableState_Type = TMGSessionState
_TmgSessionsTableState_Object = MibTableColumn
tmgSessionsTableState = _TmgSessionsTableState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 4),
    _TmgSessionsTableState_Type()
)
tmgSessionsTableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmgSessionsTableState.setStatus("current")
_TmgSessionsTableInitState_Type = Integer32
_TmgSessionsTableInitState_Object = MibTableColumn
tmgSessionsTableInitState = _TmgSessionsTableInitState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 5),
    _TmgSessionsTableInitState_Type()
)
tmgSessionsTableInitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableInitState.setStatus("current")
_TmgSessionsTableTcpSocketsPort_Type = Integer32
_TmgSessionsTableTcpSocketsPort_Object = MibTableColumn
tmgSessionsTableTcpSocketsPort = _TmgSessionsTableTcpSocketsPort_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 6),
    _TmgSessionsTableTcpSocketsPort_Type()
)
tmgSessionsTableTcpSocketsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableTcpSocketsPort.setStatus("current")


class _TmgSessionsTableTCS_Type(DisplayString):
    """Custom type tmgSessionsTableTCS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgSessionsTableTCS_Type.__name__ = "DisplayString"
_TmgSessionsTableTCS_Object = MibTableColumn
tmgSessionsTableTCS = _TmgSessionsTableTCS_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 7),
    _TmgSessionsTableTCS_Type()
)
tmgSessionsTableTCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableTCS.setStatus("current")
_TmgSessionsTableTcpSocketsPort2_Type = Integer32
_TmgSessionsTableTcpSocketsPort2_Object = MibTableColumn
tmgSessionsTableTcpSocketsPort2 = _TmgSessionsTableTcpSocketsPort2_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 8),
    _TmgSessionsTableTcpSocketsPort2_Type()
)
tmgSessionsTableTcpSocketsPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableTcpSocketsPort2.setStatus("current")


class _TmgSessionsTableTCS2_Type(DisplayString):
    """Custom type tmgSessionsTableTCS2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgSessionsTableTCS2_Type.__name__ = "DisplayString"
_TmgSessionsTableTCS2_Object = MibTableColumn
tmgSessionsTableTCS2 = _TmgSessionsTableTCS2_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 9),
    _TmgSessionsTableTCS2_Type()
)
tmgSessionsTableTCS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableTCS2.setStatus("current")


class _TmgSessionsTableWsUser_Type(DisplayString):
    """Custom type tmgSessionsTableWsUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgSessionsTableWsUser_Type.__name__ = "DisplayString"
_TmgSessionsTableWsUser_Object = MibTableColumn
tmgSessionsTableWsUser = _TmgSessionsTableWsUser_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 10),
    _TmgSessionsTableWsUser_Type()
)
tmgSessionsTableWsUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableWsUser.setStatus("current")


class _TmgSessionsTablePwd_Type(DisplayString):
    """Custom type tmgSessionsTablePwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgSessionsTablePwd_Type.__name__ = "DisplayString"
_TmgSessionsTablePwd_Object = MibTableColumn
tmgSessionsTablePwd = _TmgSessionsTablePwd_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 11),
    _TmgSessionsTablePwd_Type()
)
tmgSessionsTablePwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTablePwd.setStatus("current")
_TmgSessionsTableUseEncryptedLogin_Type = Integer32
_TmgSessionsTableUseEncryptedLogin_Object = MibTableColumn
tmgSessionsTableUseEncryptedLogin = _TmgSessionsTableUseEncryptedLogin_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 12),
    _TmgSessionsTableUseEncryptedLogin_Type()
)
tmgSessionsTableUseEncryptedLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableUseEncryptedLogin.setStatus("current")
_TmgSessionsTableSpeechTimeslot_Type = Integer32
_TmgSessionsTableSpeechTimeslot_Object = MibTableColumn
tmgSessionsTableSpeechTimeslot = _TmgSessionsTableSpeechTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 13),
    _TmgSessionsTableSpeechTimeslot_Type()
)
tmgSessionsTableSpeechTimeslot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableSpeechTimeslot.setStatus("current")
_TmgSessionsTableMonTimeslots_Type = Integer32
_TmgSessionsTableMonTimeslots_Object = MibTableColumn
tmgSessionsTableMonTimeslots = _TmgSessionsTableMonTimeslots_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 14),
    _TmgSessionsTableMonTimeslots_Type()
)
tmgSessionsTableMonTimeslots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableMonTimeslots.setStatus("current")
_TmgSessionsTableE1TrunkState_Type = Integer32
_TmgSessionsTableE1TrunkState_Object = MibTableColumn
tmgSessionsTableE1TrunkState = _TmgSessionsTableE1TrunkState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 15),
    _TmgSessionsTableE1TrunkState_Type()
)
tmgSessionsTableE1TrunkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableE1TrunkState.setStatus("current")
_TmgSessionsTableReadTCSStates_Type = Integer32
_TmgSessionsTableReadTCSStates_Object = MibTableColumn
tmgSessionsTableReadTCSStates = _TmgSessionsTableReadTCSStates_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 16),
    _TmgSessionsTableReadTCSStates_Type()
)
tmgSessionsTableReadTCSStates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableReadTCSStates.setStatus("current")
_TmgSessionsTableTCSStateTCS_Type = TMGGeneralState
_TmgSessionsTableTCSStateTCS_Object = MibTableColumn
tmgSessionsTableTCSStateTCS = _TmgSessionsTableTCSStateTCS_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 17),
    _TmgSessionsTableTCSStateTCS_Type()
)
tmgSessionsTableTCSStateTCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableTCSStateTCS.setStatus("current")
_TmgSessionsTableTCSStateDXT_Type = TMGGeneralState
_TmgSessionsTableTCSStateDXT_Object = MibTableColumn
tmgSessionsTableTCSStateDXT = _TmgSessionsTableTCSStateDXT_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 18),
    _TmgSessionsTableTCSStateDXT_Type()
)
tmgSessionsTableTCSStateDXT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableTCSStateDXT.setStatus("current")
_TmgSessionsTableTCSStateCDDConnection_Type = TMGGeneralState
_TmgSessionsTableTCSStateCDDConnection_Object = MibTableColumn
tmgSessionsTableTCSStateCDDConnection = _TmgSessionsTableTCSStateCDDConnection_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 19),
    _TmgSessionsTableTCSStateCDDConnection_Type()
)
tmgSessionsTableTCSStateCDDConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableTCSStateCDDConnection.setStatus("current")
_TmgSessionsTableTCSStateCDDServer_Type = TMGGeneralState
_TmgSessionsTableTCSStateCDDServer_Object = MibTableColumn
tmgSessionsTableTCSStateCDDServer = _TmgSessionsTableTCSStateCDDServer_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 20),
    _TmgSessionsTableTCSStateCDDServer_Type()
)
tmgSessionsTableTCSStateCDDServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableTCSStateCDDServer.setStatus("current")
_TmgSessionsTableTCSStateTDSC_Type = TMGGeneralState
_TmgSessionsTableTCSStateTDSC_Object = MibTableColumn
tmgSessionsTableTCSStateTDSC = _TmgSessionsTableTCSStateTDSC_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 21),
    _TmgSessionsTableTCSStateTDSC_Type()
)
tmgSessionsTableTCSStateTDSC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableTCSStateTDSC.setStatus("current")
_TmgSessionsTraps_ObjectIdentity = ObjectIdentity
tmgSessionsTraps = _TmgSessionsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 1, 3)
)
if mibBuilder.loadTexts:
    tmgSessionsTraps.setStatus("current")
_TmgClients_ObjectIdentity = ObjectIdentity
tmgClients = _TmgClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 1, 4)
)
if mibBuilder.loadTexts:
    tmgClients.setStatus("current")
_TmgClientsTable_Object = MibTable
tmgClientsTable = _TmgClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tmgClientsTable.setStatus("current")
_TmgClientsTableEntry_Object = MibTableRow
tmgClientsTableEntry = _TmgClientsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 4, 1, 1)
)
tmgClientsTableEntry.setIndexNames(
    (0, "Hagedorn-MIB", "tmgClientsTableIdx"),
)
if mibBuilder.loadTexts:
    tmgClientsTableEntry.setStatus("current")


class _TmgClientsTableIdx_Type(Integer32):
    """Custom type tmgClientsTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmgClientsTableIdx_Type.__name__ = "Integer32"
_TmgClientsTableIdx_Object = MibTableColumn
tmgClientsTableIdx = _TmgClientsTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 4, 1, 1, 1),
    _TmgClientsTableIdx_Type()
)
tmgClientsTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmgClientsTableIdx.setStatus("current")
_TmgClientsTableRowStatus_Type = RowStatus
_TmgClientsTableRowStatus_Object = MibTableColumn
tmgClientsTableRowStatus = _TmgClientsTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 4, 1, 1, 2),
    _TmgClientsTableRowStatus_Type()
)
tmgClientsTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmgClientsTableRowStatus.setStatus("current")


class _TmgClientsTableName_Type(SnmpAdminString):
    """Custom type tmgClientsTableName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgClientsTableName_Type.__name__ = "SnmpAdminString"
_TmgClientsTableName_Object = MibTableColumn
tmgClientsTableName = _TmgClientsTableName_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 4, 1, 1, 3),
    _TmgClientsTableName_Type()
)
tmgClientsTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgClientsTableName.setStatus("current")


class _TmgClientsTableIPPort_Type(DisplayString):
    """Custom type tmgClientsTableIPPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgClientsTableIPPort_Type.__name__ = "DisplayString"
_TmgClientsTableIPPort_Object = MibTableColumn
tmgClientsTableIPPort = _TmgClientsTableIPPort_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 4, 1, 1, 4),
    _TmgClientsTableIPPort_Type()
)
tmgClientsTableIPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgClientsTableIPPort.setStatus("current")


class _TmgClientsTableVersion_Type(DisplayString):
    """Custom type tmgClientsTableVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgClientsTableVersion_Type.__name__ = "DisplayString"
_TmgClientsTableVersion_Object = MibTableColumn
tmgClientsTableVersion = _TmgClientsTableVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 4, 1, 1, 5),
    _TmgClientsTableVersion_Type()
)
tmgClientsTableVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgClientsTableVersion.setStatus("current")
_TmgE1States_ObjectIdentity = ObjectIdentity
tmgE1States = _TmgE1States_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 1, 5)
)
if mibBuilder.loadTexts:
    tmgE1States.setStatus("current")
_TmgE1StatesTable_Object = MibTable
tmgE1StatesTable = _TmgE1StatesTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmgE1StatesTable.setStatus("current")
_TmgE1StatesTableEntry_Object = MibTableRow
tmgE1StatesTableEntry = _TmgE1StatesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 5, 1, 1)
)
tmgE1StatesTableEntry.setIndexNames(
    (0, "Hagedorn-MIB", "tmgE1StatesTableIdx"),
)
if mibBuilder.loadTexts:
    tmgE1StatesTableEntry.setStatus("current")


class _TmgE1StatesTableIdx_Type(Integer32):
    """Custom type tmgE1StatesTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmgE1StatesTableIdx_Type.__name__ = "Integer32"
_TmgE1StatesTableIdx_Object = MibTableColumn
tmgE1StatesTableIdx = _TmgE1StatesTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 5, 1, 1, 1),
    _TmgE1StatesTableIdx_Type()
)
tmgE1StatesTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmgE1StatesTableIdx.setStatus("current")
_TmgE1StatesTableRowStatus_Type = RowStatus
_TmgE1StatesTableRowStatus_Object = MibTableColumn
tmgE1StatesTableRowStatus = _TmgE1StatesTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 5, 1, 1, 2),
    _TmgE1StatesTableRowStatus_Type()
)
tmgE1StatesTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmgE1StatesTableRowStatus.setStatus("current")


class _TmgE1StatesTableName_Type(DisplayString):
    """Custom type tmgE1StatesTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgE1StatesTableName_Type.__name__ = "DisplayString"
_TmgE1StatesTableName_Object = MibTableColumn
tmgE1StatesTableName = _TmgE1StatesTableName_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 5, 1, 1, 3),
    _TmgE1StatesTableName_Type()
)
tmgE1StatesTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgE1StatesTableName.setStatus("current")


class _TmgE1StatesTableState_Type(DisplayString):
    """Custom type tmgE1StatesTableState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgE1StatesTableState_Type.__name__ = "DisplayString"
_TmgE1StatesTableState_Object = MibTableColumn
tmgE1StatesTableState = _TmgE1StatesTableState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 5, 1, 1, 4),
    _TmgE1StatesTableState_Type()
)
tmgE1StatesTableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmgE1StatesTableState.setStatus("current")
_KryptoSrv_ObjectIdentity = ObjectIdentity
kryptoSrv = _KryptoSrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 2)
)
if mibBuilder.loadTexts:
    kryptoSrv.setStatus("current")
_KsGeneral_ObjectIdentity = ObjectIdentity
ksGeneral = _KsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 2, 1)
)
if mibBuilder.loadTexts:
    ksGeneral.setStatus("current")
_KsGenKryxConnected_Type = Integer32
_KsGenKryxConnected_Object = MibScalar
ksGenKryxConnected = _KsGenKryxConnected_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 1, 1),
    _KsGenKryxConnected_Type()
)
ksGenKryxConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ksGenKryxConnected.setStatus("current")


class _KsGenKryxLastStatusCode_Type(OctetString):
    """Custom type ksGenKryxLastStatusCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_KsGenKryxLastStatusCode_Type.__name__ = "OctetString"
_KsGenKryxLastStatusCode_Object = MibScalar
ksGenKryxLastStatusCode = _KsGenKryxLastStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 1, 2),
    _KsGenKryxLastStatusCode_Type()
)
ksGenKryxLastStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ksGenKryxLastStatusCode.setStatus("current")


class _KsGenKryxLastStatusText_Type(SnmpAdminString):
    """Custom type ksGenKryxLastStatusText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KsGenKryxLastStatusText_Type.__name__ = "SnmpAdminString"
_KsGenKryxLastStatusText_Object = MibScalar
ksGenKryxLastStatusText = _KsGenKryxLastStatusText_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 1, 3),
    _KsGenKryxLastStatusText_Type()
)
ksGenKryxLastStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ksGenKryxLastStatusText.setStatus("current")
_KsGeneralTraps_ObjectIdentity = ObjectIdentity
ksGeneralTraps = _KsGeneralTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 2, 2)
)
if mibBuilder.loadTexts:
    ksGeneralTraps.setStatus("current")
_IpRadioTouch_ObjectIdentity = ObjectIdentity
ipRadioTouch = _IpRadioTouch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 3)
)
if mibBuilder.loadTexts:
    ipRadioTouch.setStatus("current")
_IprtGeneral_ObjectIdentity = ObjectIdentity
iprtGeneral = _IprtGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1)
)
if mibBuilder.loadTexts:
    iprtGeneral.setStatus("current")


class _IprtGenUserName_Type(DisplayString):
    """Custom type iprtGenUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprtGenUserName_Type.__name__ = "DisplayString"
_IprtGenUserName_Object = MibScalar
iprtGenUserName = _IprtGenUserName_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 1),
    _IprtGenUserName_Type()
)
iprtGenUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenUserName.setStatus("current")


class _IprtGenVersion_Type(DisplayString):
    """Custom type iprtGenVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprtGenVersion_Type.__name__ = "DisplayString"
_IprtGenVersion_Object = MibScalar
iprtGenVersion = _IprtGenVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 2),
    _IprtGenVersion_Type()
)
iprtGenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenVersion.setStatus("current")
_IprtGenState_Type = IPRTGeneralState
_IprtGenState_Object = MibScalar
iprtGenState = _IprtGenState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 3),
    _IprtGenState_Type()
)
iprtGenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenState.setStatus("current")


class _IprtGenOsUser_Type(DisplayString):
    """Custom type iprtGenOsUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprtGenOsUser_Type.__name__ = "DisplayString"
_IprtGenOsUser_Object = MibScalar
iprtGenOsUser = _IprtGenOsUser_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 4),
    _IprtGenOsUser_Type()
)
iprtGenOsUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenOsUser.setStatus("current")


class _IprtGenRole_Type(DisplayString):
    """Custom type iprtGenRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprtGenRole_Type.__name__ = "DisplayString"
_IprtGenRole_Object = MibScalar
iprtGenRole = _IprtGenRole_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 5),
    _IprtGenRole_Type()
)
iprtGenRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenRole.setStatus("current")
_IprtGenVtlstState_Type = IPRTConnectionsState
_IprtGenVtlstState_Object = MibScalar
iprtGenVtlstState = _IprtGenVtlstState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 6),
    _IprtGenVtlstState_Type()
)
iprtGenVtlstState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenVtlstState.setStatus("current")
_IprtGenRecorderState_Type = IPRTConnectionsState
_IprtGenRecorderState_Object = MibScalar
iprtGenRecorderState = _IprtGenRecorderState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 7),
    _IprtGenRecorderState_Type()
)
iprtGenRecorderState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenRecorderState.setStatus("current")
_IprtGenAudioBoxDevice_Type = IPRTAudioBoxDevice
_IprtGenAudioBoxDevice_Object = MibScalar
iprtGenAudioBoxDevice = _IprtGenAudioBoxDevice_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 8),
    _IprtGenAudioBoxDevice_Type()
)
iprtGenAudioBoxDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenAudioBoxDevice.setStatus("current")


class _IprtGenAudioBoxExtSpeaker1Volume_Type(Integer32):
    """Custom type iprtGenAudioBoxExtSpeaker1Volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IprtGenAudioBoxExtSpeaker1Volume_Type.__name__ = "Integer32"
_IprtGenAudioBoxExtSpeaker1Volume_Object = MibScalar
iprtGenAudioBoxExtSpeaker1Volume = _IprtGenAudioBoxExtSpeaker1Volume_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 9),
    _IprtGenAudioBoxExtSpeaker1Volume_Type()
)
iprtGenAudioBoxExtSpeaker1Volume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenAudioBoxExtSpeaker1Volume.setStatus("current")


class _IprtGenAudioBoxExtSpeaker2Volume_Type(Integer32):
    """Custom type iprtGenAudioBoxExtSpeaker2Volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IprtGenAudioBoxExtSpeaker2Volume_Type.__name__ = "Integer32"
_IprtGenAudioBoxExtSpeaker2Volume_Object = MibScalar
iprtGenAudioBoxExtSpeaker2Volume = _IprtGenAudioBoxExtSpeaker2Volume_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 10),
    _IprtGenAudioBoxExtSpeaker2Volume_Type()
)
iprtGenAudioBoxExtSpeaker2Volume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenAudioBoxExtSpeaker2Volume.setStatus("current")


class _IprtGenAudioBoxExtSpeaker3Volume_Type(Integer32):
    """Custom type iprtGenAudioBoxExtSpeaker3Volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IprtGenAudioBoxExtSpeaker3Volume_Type.__name__ = "Integer32"
_IprtGenAudioBoxExtSpeaker3Volume_Object = MibScalar
iprtGenAudioBoxExtSpeaker3Volume = _IprtGenAudioBoxExtSpeaker3Volume_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 11),
    _IprtGenAudioBoxExtSpeaker3Volume_Type()
)
iprtGenAudioBoxExtSpeaker3Volume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenAudioBoxExtSpeaker3Volume.setStatus("current")


class _IprtGenAudioBoxExtSpeaker4Volume_Type(Integer32):
    """Custom type iprtGenAudioBoxExtSpeaker4Volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IprtGenAudioBoxExtSpeaker4Volume_Type.__name__ = "Integer32"
_IprtGenAudioBoxExtSpeaker4Volume_Object = MibScalar
iprtGenAudioBoxExtSpeaker4Volume = _IprtGenAudioBoxExtSpeaker4Volume_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 12),
    _IprtGenAudioBoxExtSpeaker4Volume_Type()
)
iprtGenAudioBoxExtSpeaker4Volume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenAudioBoxExtSpeaker4Volume.setStatus("current")


class _IprtGenAudioBoxActualSpeakerVolume_Type(Integer32):
    """Custom type iprtGenAudioBoxActualSpeakerVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IprtGenAudioBoxActualSpeakerVolume_Type.__name__ = "Integer32"
_IprtGenAudioBoxActualSpeakerVolume_Object = MibScalar
iprtGenAudioBoxActualSpeakerVolume = _IprtGenAudioBoxActualSpeakerVolume_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 13),
    _IprtGenAudioBoxActualSpeakerVolume_Type()
)
iprtGenAudioBoxActualSpeakerVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenAudioBoxActualSpeakerVolume.setStatus("current")


class _IprtGenAudioBoxMixedSpeakerVolume_Type(Integer32):
    """Custom type iprtGenAudioBoxMixedSpeakerVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IprtGenAudioBoxMixedSpeakerVolume_Type.__name__ = "Integer32"
_IprtGenAudioBoxMixedSpeakerVolume_Object = MibScalar
iprtGenAudioBoxMixedSpeakerVolume = _IprtGenAudioBoxMixedSpeakerVolume_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 14),
    _IprtGenAudioBoxMixedSpeakerVolume_Type()
)
iprtGenAudioBoxMixedSpeakerVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenAudioBoxMixedSpeakerVolume.setStatus("current")


class _IprtGenAudioBoxHeadsetSpeakerVolume_Type(Integer32):
    """Custom type iprtGenAudioBoxHeadsetSpeakerVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IprtGenAudioBoxHeadsetSpeakerVolume_Type.__name__ = "Integer32"
_IprtGenAudioBoxHeadsetSpeakerVolume_Object = MibScalar
iprtGenAudioBoxHeadsetSpeakerVolume = _IprtGenAudioBoxHeadsetSpeakerVolume_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 15),
    _IprtGenAudioBoxHeadsetSpeakerVolume_Type()
)
iprtGenAudioBoxHeadsetSpeakerVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenAudioBoxHeadsetSpeakerVolume.setStatus("current")


class _IprtGenAudioBoxHandsetSpeakerVolume_Type(Integer32):
    """Custom type iprtGenAudioBoxHandsetSpeakerVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IprtGenAudioBoxHandsetSpeakerVolume_Type.__name__ = "Integer32"
_IprtGenAudioBoxHandsetSpeakerVolume_Object = MibScalar
iprtGenAudioBoxHandsetSpeakerVolume = _IprtGenAudioBoxHandsetSpeakerVolume_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 16),
    _IprtGenAudioBoxHandsetSpeakerVolume_Type()
)
iprtGenAudioBoxHandsetSpeakerVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenAudioBoxHandsetSpeakerVolume.setStatus("current")


class _IprtGenAudioBoxLineOutSpeakerVolume_Type(Integer32):
    """Custom type iprtGenAudioBoxLineOutSpeakerVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IprtGenAudioBoxLineOutSpeakerVolume_Type.__name__ = "Integer32"
_IprtGenAudioBoxLineOutSpeakerVolume_Object = MibScalar
iprtGenAudioBoxLineOutSpeakerVolume = _IprtGenAudioBoxLineOutSpeakerVolume_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 17),
    _IprtGenAudioBoxLineOutSpeakerVolume_Type()
)
iprtGenAudioBoxLineOutSpeakerVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprtGenAudioBoxLineOutSpeakerVolume.setStatus("current")
_IprtGeneralTraps_ObjectIdentity = ObjectIdentity
iprtGeneralTraps = _IprtGeneralTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2)
)
if mibBuilder.loadTexts:
    iprtGeneralTraps.setStatus("current")
_IprtChannels_ObjectIdentity = ObjectIdentity
iprtChannels = _IprtChannels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3)
)
if mibBuilder.loadTexts:
    iprtChannels.setStatus("current")
_IprtChannelsTable_Object = MibTable
iprtChannelsTable = _IprtChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1)
)
if mibBuilder.loadTexts:
    iprtChannelsTable.setStatus("current")
_IprtChannelsTableEntry_Object = MibTableRow
iprtChannelsTableEntry = _IprtChannelsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1)
)
iprtChannelsTableEntry.setIndexNames(
    (0, "Hagedorn-MIB", "iprtChannelsTableIdx"),
)
if mibBuilder.loadTexts:
    iprtChannelsTableEntry.setStatus("current")


class _IprtChannelsTableIdx_Type(Integer32):
    """Custom type iprtChannelsTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IprtChannelsTableIdx_Type.__name__ = "Integer32"
_IprtChannelsTableIdx_Object = MibTableColumn
iprtChannelsTableIdx = _IprtChannelsTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1, 1),
    _IprtChannelsTableIdx_Type()
)
iprtChannelsTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iprtChannelsTableIdx.setStatus("current")
_IprtChannelsTableRowStatus_Type = RowStatus
_IprtChannelsTableRowStatus_Object = MibTableColumn
iprtChannelsTableRowStatus = _IprtChannelsTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1, 2),
    _IprtChannelsTableRowStatus_Type()
)
iprtChannelsTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iprtChannelsTableRowStatus.setStatus("current")


class _IprtChannelsTableID_Type(DisplayString):
    """Custom type iprtChannelsTableID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprtChannelsTableID_Type.__name__ = "DisplayString"
_IprtChannelsTableID_Object = MibTableColumn
iprtChannelsTableID = _IprtChannelsTableID_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1, 3),
    _IprtChannelsTableID_Type()
)
iprtChannelsTableID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtChannelsTableID.setStatus("current")
_IprtChannelsTableRegistered_Type = Integer32
_IprtChannelsTableRegistered_Object = MibTableColumn
iprtChannelsTableRegistered = _IprtChannelsTableRegistered_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1, 4),
    _IprtChannelsTableRegistered_Type()
)
iprtChannelsTableRegistered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtChannelsTableRegistered.setStatus("current")
_IprtChannelsTableState_Type = IPRTChannelState
_IprtChannelsTableState_Object = MibTableColumn
iprtChannelsTableState = _IprtChannelsTableState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1, 5),
    _IprtChannelsTableState_Type()
)
iprtChannelsTableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtChannelsTableState.setStatus("current")


class _IprtChannelsTableISSI_Type(DisplayString):
    """Custom type iprtChannelsTableISSI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprtChannelsTableISSI_Type.__name__ = "DisplayString"
_IprtChannelsTableISSI_Object = MibTableColumn
iprtChannelsTableISSI = _IprtChannelsTableISSI_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1, 6),
    _IprtChannelsTableISSI_Type()
)
iprtChannelsTableISSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtChannelsTableISSI.setStatus("current")


class _IprtChannelsTableGSSI_Type(DisplayString):
    """Custom type iprtChannelsTableGSSI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprtChannelsTableGSSI_Type.__name__ = "DisplayString"
_IprtChannelsTableGSSI_Object = MibTableColumn
iprtChannelsTableGSSI = _IprtChannelsTableGSSI_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1, 7),
    _IprtChannelsTableGSSI_Type()
)
iprtChannelsTableGSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtChannelsTableGSSI.setStatus("current")
_IprtChannelsTableDevice_Type = IPRTChannelDevice
_IprtChannelsTableDevice_Object = MibTableColumn
iprtChannelsTableDevice = _IprtChannelsTableDevice_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1, 8),
    _IprtChannelsTableDevice_Type()
)
iprtChannelsTableDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtChannelsTableDevice.setStatus("current")
_IprtChannelsTableCommType_Type = IPRTChannelCommType
_IprtChannelsTableCommType_Object = MibTableColumn
iprtChannelsTableCommType = _IprtChannelsTableCommType_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1, 9),
    _IprtChannelsTableCommType_Type()
)
iprtChannelsTableCommType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtChannelsTableCommType.setStatus("current")
_IprtChannelsTraps_ObjectIdentity = ObjectIdentity
iprtChannelsTraps = _IprtChannelsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 3, 4)
)
if mibBuilder.loadTexts:
    iprtChannelsTraps.setStatus("current")
_IprtAudio_ObjectIdentity = ObjectIdentity
iprtAudio = _IprtAudio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 3, 5)
)
if mibBuilder.loadTexts:
    iprtAudio.setStatus("current")
_IprtAudioTable_Object = MibTable
iprtAudioTable = _IprtAudioTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 5, 1)
)
if mibBuilder.loadTexts:
    iprtAudioTable.setStatus("current")
_IprtAudioTableEntry_Object = MibTableRow
iprtAudioTableEntry = _IprtAudioTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 5, 1, 1)
)
iprtAudioTableEntry.setIndexNames(
    (0, "Hagedorn-MIB", "iprtAudioTableIdx"),
)
if mibBuilder.loadTexts:
    iprtAudioTableEntry.setStatus("current")


class _IprtAudioTableIdx_Type(Integer32):
    """Custom type iprtAudioTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IprtAudioTableIdx_Type.__name__ = "Integer32"
_IprtAudioTableIdx_Object = MibTableColumn
iprtAudioTableIdx = _IprtAudioTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 5, 1, 1, 1),
    _IprtAudioTableIdx_Type()
)
iprtAudioTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iprtAudioTableIdx.setStatus("current")
_IprtAudioTableRowStatus_Type = RowStatus
_IprtAudioTableRowStatus_Object = MibTableColumn
iprtAudioTableRowStatus = _IprtAudioTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 5, 1, 1, 2),
    _IprtAudioTableRowStatus_Type()
)
iprtAudioTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iprtAudioTableRowStatus.setStatus("current")


class _IprtAudioTableID_Type(DisplayString):
    """Custom type iprtAudioTableID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprtAudioTableID_Type.__name__ = "DisplayString"
_IprtAudioTableID_Object = MibTableColumn
iprtAudioTableID = _IprtAudioTableID_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 5, 1, 1, 3),
    _IprtAudioTableID_Type()
)
iprtAudioTableID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtAudioTableID.setStatus("current")


class _IprtAudioTableSpeakerName_Type(DisplayString):
    """Custom type iprtAudioTableSpeakerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprtAudioTableSpeakerName_Type.__name__ = "DisplayString"
_IprtAudioTableSpeakerName_Object = MibTableColumn
iprtAudioTableSpeakerName = _IprtAudioTableSpeakerName_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 5, 1, 1, 4),
    _IprtAudioTableSpeakerName_Type()
)
iprtAudioTableSpeakerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtAudioTableSpeakerName.setStatus("current")
_IprtAudioTableSpeakerVolume_Type = Integer32
_IprtAudioTableSpeakerVolume_Object = MibTableColumn
iprtAudioTableSpeakerVolume = _IprtAudioTableSpeakerVolume_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 5, 1, 1, 5),
    _IprtAudioTableSpeakerVolume_Type()
)
iprtAudioTableSpeakerVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtAudioTableSpeakerVolume.setStatus("current")


class _IprtAudioTableMicrophoneName_Type(DisplayString):
    """Custom type iprtAudioTableMicrophoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprtAudioTableMicrophoneName_Type.__name__ = "DisplayString"
_IprtAudioTableMicrophoneName_Object = MibTableColumn
iprtAudioTableMicrophoneName = _IprtAudioTableMicrophoneName_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 5, 1, 1, 6),
    _IprtAudioTableMicrophoneName_Type()
)
iprtAudioTableMicrophoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtAudioTableMicrophoneName.setStatus("current")
_IprtAudioTableMicrophoneVolume_Type = Integer32
_IprtAudioTableMicrophoneVolume_Object = MibTableColumn
iprtAudioTableMicrophoneVolume = _IprtAudioTableMicrophoneVolume_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 5, 1, 1, 7),
    _IprtAudioTableMicrophoneVolume_Type()
)
iprtAudioTableMicrophoneVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtAudioTableMicrophoneVolume.setStatus("current")
_IprtAudioTableNoiseGate_Type = IPRTAudioNoiseGate
_IprtAudioTableNoiseGate_Object = MibTableColumn
iprtAudioTableNoiseGate = _IprtAudioTableNoiseGate_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 5, 1, 1, 8),
    _IprtAudioTableNoiseGate_Type()
)
iprtAudioTableNoiseGate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtAudioTableNoiseGate.setStatus("current")
_IprtAudioTableNoiseGateTreshold_Type = Integer32
_IprtAudioTableNoiseGateTreshold_Object = MibTableColumn
iprtAudioTableNoiseGateTreshold = _IprtAudioTableNoiseGateTreshold_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 5, 1, 1, 9),
    _IprtAudioTableNoiseGateTreshold_Type()
)
iprtAudioTableNoiseGateTreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtAudioTableNoiseGateTreshold.setStatus("current")
_IprtAudioTableNoiseGateAttackTime_Type = Integer32
_IprtAudioTableNoiseGateAttackTime_Object = MibTableColumn
iprtAudioTableNoiseGateAttackTime = _IprtAudioTableNoiseGateAttackTime_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 5, 1, 1, 10),
    _IprtAudioTableNoiseGateAttackTime_Type()
)
iprtAudioTableNoiseGateAttackTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtAudioTableNoiseGateAttackTime.setStatus("current")
_IprtAudioTableNoiseGateReleaseTime_Type = Integer32
_IprtAudioTableNoiseGateReleaseTime_Object = MibTableColumn
iprtAudioTableNoiseGateReleaseTime = _IprtAudioTableNoiseGateReleaseTime_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 5, 1, 1, 11),
    _IprtAudioTableNoiseGateReleaseTime_Type()
)
iprtAudioTableNoiseGateReleaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtAudioTableNoiseGateReleaseTime.setStatus("current")
_IprtAudioTableNoiseGateHoldTime_Type = Integer32
_IprtAudioTableNoiseGateHoldTime_Object = MibTableColumn
iprtAudioTableNoiseGateHoldTime = _IprtAudioTableNoiseGateHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 5, 1, 1, 12),
    _IprtAudioTableNoiseGateHoldTime_Type()
)
iprtAudioTableNoiseGateHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprtAudioTableNoiseGateHoldTime.setStatus("current")
_IprtAudioTraps_ObjectIdentity = ObjectIdentity
iprtAudioTraps = _IprtAudioTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 3, 6)
)
if mibBuilder.loadTexts:
    iprtAudioTraps.setStatus("current")
_Crys_ObjectIdentity = ObjectIdentity
crys = _Crys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 4)
)
if mibBuilder.loadTexts:
    crys.setStatus("current")
_CrysGeneralTraps_ObjectIdentity = ObjectIdentity
crysGeneralTraps = _CrysGeneralTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 4, 0)
)
if mibBuilder.loadTexts:
    crysGeneralTraps.setStatus("current")
_CrysGeneral_ObjectIdentity = ObjectIdentity
crysGeneral = _CrysGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1)
)
if mibBuilder.loadTexts:
    crysGeneral.setStatus("current")
_CrysGenTmg_ObjectIdentity = ObjectIdentity
crysGenTmg = _CrysGenTmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 1)
)
if mibBuilder.loadTexts:
    crysGenTmg.setStatus("current")


class _CrysGenTmgListenAddress_Type(DisplayString):
    """Custom type crysGenTmgListenAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CrysGenTmgListenAddress_Type.__name__ = "DisplayString"
_CrysGenTmgListenAddress_Object = MibScalar
crysGenTmgListenAddress = _CrysGenTmgListenAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 1, 1),
    _CrysGenTmgListenAddress_Type()
)
crysGenTmgListenAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crysGenTmgListenAddress.setStatus("current")
_CrysGenTmgListenerState_Type = Integer32
_CrysGenTmgListenerState_Object = MibScalar
crysGenTmgListenerState = _CrysGenTmgListenerState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 1, 2),
    _CrysGenTmgListenerState_Type()
)
crysGenTmgListenerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crysGenTmgListenerState.setStatus("current")


class _CrysGenTmgSocketAddress_Type(DisplayString):
    """Custom type crysGenTmgSocketAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CrysGenTmgSocketAddress_Type.__name__ = "DisplayString"
_CrysGenTmgSocketAddress_Object = MibScalar
crysGenTmgSocketAddress = _CrysGenTmgSocketAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 1, 3),
    _CrysGenTmgSocketAddress_Type()
)
crysGenTmgSocketAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crysGenTmgSocketAddress.setStatus("current")
_CrysGenTmgSocketState_Type = Integer32
_CrysGenTmgSocketState_Object = MibScalar
crysGenTmgSocketState = _CrysGenTmgSocketState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 1, 4),
    _CrysGenTmgSocketState_Type()
)
crysGenTmgSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crysGenTmgSocketState.setStatus("current")
_CrysGenE1s_ObjectIdentity = ObjectIdentity
crysGenE1s = _CrysGenE1s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 2)
)
if mibBuilder.loadTexts:
    crysGenE1s.setStatus("current")


class _CrysGenE1sListenSocketAddress_Type(DisplayString):
    """Custom type crysGenE1sListenSocketAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CrysGenE1sListenSocketAddress_Type.__name__ = "DisplayString"
_CrysGenE1sListenSocketAddress_Object = MibScalar
crysGenE1sListenSocketAddress = _CrysGenE1sListenSocketAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 2, 1),
    _CrysGenE1sListenSocketAddress_Type()
)
crysGenE1sListenSocketAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crysGenE1sListenSocketAddress.setStatus("current")
_CrysGenE1sListenSocketState_Type = Integer32
_CrysGenE1sListenSocketState_Object = MibScalar
crysGenE1sListenSocketState = _CrysGenE1sListenSocketState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 2, 2),
    _CrysGenE1sListenSocketState_Type()
)
crysGenE1sListenSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crysGenE1sListenSocketState.setStatus("current")


class _CrysGenE1sSendSocketAddress_Type(DisplayString):
    """Custom type crysGenE1sSendSocketAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CrysGenE1sSendSocketAddress_Type.__name__ = "DisplayString"
_CrysGenE1sSendSocketAddress_Object = MibScalar
crysGenE1sSendSocketAddress = _CrysGenE1sSendSocketAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 2, 3),
    _CrysGenE1sSendSocketAddress_Type()
)
crysGenE1sSendSocketAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crysGenE1sSendSocketAddress.setStatus("current")


class _CrysGenE1sSendToAddress_Type(DisplayString):
    """Custom type crysGenE1sSendToAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CrysGenE1sSendToAddress_Type.__name__ = "DisplayString"
_CrysGenE1sSendToAddress_Object = MibScalar
crysGenE1sSendToAddress = _CrysGenE1sSendToAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 2, 4),
    _CrysGenE1sSendToAddress_Type()
)
crysGenE1sSendToAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crysGenE1sSendToAddress.setStatus("current")
_CrysGenE1sSendSocketState_Type = Integer32
_CrysGenE1sSendSocketState_Object = MibScalar
crysGenE1sSendSocketState = _CrysGenE1sSendSocketState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 2, 5),
    _CrysGenE1sSendSocketState_Type()
)
crysGenE1sSendSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crysGenE1sSendSocketState.setStatus("current")
_CrysGenRats_ObjectIdentity = ObjectIdentity
crysGenRats = _CrysGenRats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 3)
)
if mibBuilder.loadTexts:
    crysGenRats.setStatus("current")


class _CrysGenRatsListenSocketAddress_Type(DisplayString):
    """Custom type crysGenRatsListenSocketAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CrysGenRatsListenSocketAddress_Type.__name__ = "DisplayString"
_CrysGenRatsListenSocketAddress_Object = MibScalar
crysGenRatsListenSocketAddress = _CrysGenRatsListenSocketAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 3, 1),
    _CrysGenRatsListenSocketAddress_Type()
)
crysGenRatsListenSocketAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crysGenRatsListenSocketAddress.setStatus("current")
_CrysGenRatsListenSocketState_Type = Integer32
_CrysGenRatsListenSocketState_Object = MibScalar
crysGenRatsListenSocketState = _CrysGenRatsListenSocketState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 3, 2),
    _CrysGenRatsListenSocketState_Type()
)
crysGenRatsListenSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crysGenRatsListenSocketState.setStatus("current")


class _CrysGenRatsSendSocketAddress_Type(DisplayString):
    """Custom type crysGenRatsSendSocketAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CrysGenRatsSendSocketAddress_Type.__name__ = "DisplayString"
_CrysGenRatsSendSocketAddress_Object = MibScalar
crysGenRatsSendSocketAddress = _CrysGenRatsSendSocketAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 3, 3),
    _CrysGenRatsSendSocketAddress_Type()
)
crysGenRatsSendSocketAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crysGenRatsSendSocketAddress.setStatus("current")


class _CrysGenRatsSendToAddress_Type(DisplayString):
    """Custom type crysGenRatsSendToAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CrysGenRatsSendToAddress_Type.__name__ = "DisplayString"
_CrysGenRatsSendToAddress_Object = MibScalar
crysGenRatsSendToAddress = _CrysGenRatsSendToAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 3, 4),
    _CrysGenRatsSendToAddress_Type()
)
crysGenRatsSendToAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crysGenRatsSendToAddress.setStatus("current")
_CrysGenRatsSendSocketState_Type = Integer32
_CrysGenRatsSendSocketState_Object = MibScalar
crysGenRatsSendSocketState = _CrysGenRatsSendSocketState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 1, 3, 5),
    _CrysGenRatsSendSocketState_Type()
)
crysGenRatsSendSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crysGenRatsSendSocketState.setStatus("current")
_CrysMkkDaemons_ObjectIdentity = ObjectIdentity
crysMkkDaemons = _CrysMkkDaemons_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 4, 2)
)
if mibBuilder.loadTexts:
    crysMkkDaemons.setStatus("current")
_CrysMkkDaemonsTable_Object = MibTable
crysMkkDaemonsTable = _CrysMkkDaemonsTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 2, 1)
)
if mibBuilder.loadTexts:
    crysMkkDaemonsTable.setStatus("current")
_CrysMkkDaemonsTableEntry_Object = MibTableRow
crysMkkDaemonsTableEntry = _CrysMkkDaemonsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 2, 1, 1)
)
crysMkkDaemonsTableEntry.setIndexNames(
    (0, "Hagedorn-MIB", "crysMkkDaemonsTableIdx"),
)
if mibBuilder.loadTexts:
    crysMkkDaemonsTableEntry.setStatus("current")


class _CrysMkkDaemonsTableIdx_Type(Integer32):
    """Custom type crysMkkDaemonsTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CrysMkkDaemonsTableIdx_Type.__name__ = "Integer32"
_CrysMkkDaemonsTableIdx_Object = MibTableColumn
crysMkkDaemonsTableIdx = _CrysMkkDaemonsTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 2, 1, 1, 1),
    _CrysMkkDaemonsTableIdx_Type()
)
crysMkkDaemonsTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysMkkDaemonsTableIdx.setStatus("current")
_CrysMkkDaemonsTableRowStatus_Type = RowStatus
_CrysMkkDaemonsTableRowStatus_Object = MibTableColumn
crysMkkDaemonsTableRowStatus = _CrysMkkDaemonsTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 2, 1, 1, 2),
    _CrysMkkDaemonsTableRowStatus_Type()
)
crysMkkDaemonsTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crysMkkDaemonsTableRowStatus.setStatus("current")


class _CrysMkkDaemonsTableMkkDaemonNr_Type(Integer32):
    """Custom type crysMkkDaemonsTableMkkDaemonNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CrysMkkDaemonsTableMkkDaemonNr_Type.__name__ = "Integer32"
_CrysMkkDaemonsTableMkkDaemonNr_Object = MibTableColumn
crysMkkDaemonsTableMkkDaemonNr = _CrysMkkDaemonsTableMkkDaemonNr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 2, 1, 1, 3),
    _CrysMkkDaemonsTableMkkDaemonNr_Type()
)
crysMkkDaemonsTableMkkDaemonNr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysMkkDaemonsTableMkkDaemonNr.setStatus("current")


class _CrysMkkDaemonsTableAddress_Type(DisplayString):
    """Custom type crysMkkDaemonsTableAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CrysMkkDaemonsTableAddress_Type.__name__ = "DisplayString"
_CrysMkkDaemonsTableAddress_Object = MibTableColumn
crysMkkDaemonsTableAddress = _CrysMkkDaemonsTableAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 2, 1, 1, 4),
    _CrysMkkDaemonsTableAddress_Type()
)
crysMkkDaemonsTableAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysMkkDaemonsTableAddress.setStatus("current")


class _CrysMkkDaemonsTableConnStatus_Type(Integer32):
    """Custom type crysMkkDaemonsTableConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CrysMkkDaemonsTableConnStatus_Type.__name__ = "Integer32"
_CrysMkkDaemonsTableConnStatus_Object = MibTableColumn
crysMkkDaemonsTableConnStatus = _CrysMkkDaemonsTableConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 2, 1, 1, 5),
    _CrysMkkDaemonsTableConnStatus_Type()
)
crysMkkDaemonsTableConnStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysMkkDaemonsTableConnStatus.setStatus("current")


class _CrysMkkDaemonsTableVersion_Type(DisplayString):
    """Custom type crysMkkDaemonsTableVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CrysMkkDaemonsTableVersion_Type.__name__ = "DisplayString"
_CrysMkkDaemonsTableVersion_Object = MibTableColumn
crysMkkDaemonsTableVersion = _CrysMkkDaemonsTableVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 2, 1, 1, 6),
    _CrysMkkDaemonsTableVersion_Type()
)
crysMkkDaemonsTableVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysMkkDaemonsTableVersion.setStatus("current")


class _CrysMkkDaemonsTableDriverVersion_Type(DisplayString):
    """Custom type crysMkkDaemonsTableDriverVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CrysMkkDaemonsTableDriverVersion_Type.__name__ = "DisplayString"
_CrysMkkDaemonsTableDriverVersion_Object = MibTableColumn
crysMkkDaemonsTableDriverVersion = _CrysMkkDaemonsTableDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 2, 1, 1, 7),
    _CrysMkkDaemonsTableDriverVersion_Type()
)
crysMkkDaemonsTableDriverVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysMkkDaemonsTableDriverVersion.setStatus("current")


class _CrysMkkDaemonsTableDriverError_Type(OctetString):
    """Custom type crysMkkDaemonsTableDriverError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_CrysMkkDaemonsTableDriverError_Type.__name__ = "OctetString"
_CrysMkkDaemonsTableDriverError_Object = MibTableColumn
crysMkkDaemonsTableDriverError = _CrysMkkDaemonsTableDriverError_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 2, 1, 1, 8),
    _CrysMkkDaemonsTableDriverError_Type()
)
crysMkkDaemonsTableDriverError.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysMkkDaemonsTableDriverError.setStatus("current")
_CrysMkkCards_ObjectIdentity = ObjectIdentity
crysMkkCards = _CrysMkkCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 4, 3)
)
if mibBuilder.loadTexts:
    crysMkkCards.setStatus("current")
_CrysMkkCardsTable_Object = MibTable
crysMkkCardsTable = _CrysMkkCardsTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 3, 1)
)
if mibBuilder.loadTexts:
    crysMkkCardsTable.setStatus("current")
_CrysMkkCardsTableEntry_Object = MibTableRow
crysMkkCardsTableEntry = _CrysMkkCardsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 3, 1, 1)
)
crysMkkCardsTableEntry.setIndexNames(
    (0, "Hagedorn-MIB", "crysMkkCardsTableIdx"),
)
if mibBuilder.loadTexts:
    crysMkkCardsTableEntry.setStatus("current")


class _CrysMkkCardsTableIdx_Type(Integer32):
    """Custom type crysMkkCardsTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CrysMkkCardsTableIdx_Type.__name__ = "Integer32"
_CrysMkkCardsTableIdx_Object = MibTableColumn
crysMkkCardsTableIdx = _CrysMkkCardsTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 3, 1, 1, 1),
    _CrysMkkCardsTableIdx_Type()
)
crysMkkCardsTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysMkkCardsTableIdx.setStatus("current")
_CrysMkkCardsTableRowStatus_Type = RowStatus
_CrysMkkCardsTableRowStatus_Object = MibTableColumn
crysMkkCardsTableRowStatus = _CrysMkkCardsTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 3, 1, 1, 2),
    _CrysMkkCardsTableRowStatus_Type()
)
crysMkkCardsTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crysMkkCardsTableRowStatus.setStatus("current")


class _CrysMkkCardsTableCardNr_Type(Integer32):
    """Custom type crysMkkCardsTableCardNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CrysMkkCardsTableCardNr_Type.__name__ = "Integer32"
_CrysMkkCardsTableCardNr_Object = MibTableColumn
crysMkkCardsTableCardNr = _CrysMkkCardsTableCardNr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 3, 1, 1, 3),
    _CrysMkkCardsTableCardNr_Type()
)
crysMkkCardsTableCardNr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysMkkCardsTableCardNr.setStatus("current")


class _CrysMkkCardsTableMkkDaemonNr_Type(Integer32):
    """Custom type crysMkkCardsTableMkkDaemonNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CrysMkkCardsTableMkkDaemonNr_Type.__name__ = "Integer32"
_CrysMkkCardsTableMkkDaemonNr_Object = MibTableColumn
crysMkkCardsTableMkkDaemonNr = _CrysMkkCardsTableMkkDaemonNr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 3, 1, 1, 4),
    _CrysMkkCardsTableMkkDaemonNr_Type()
)
crysMkkCardsTableMkkDaemonNr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysMkkCardsTableMkkDaemonNr.setStatus("current")


class _CrysMkkCardsTableVersion_Type(DisplayString):
    """Custom type crysMkkCardsTableVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CrysMkkCardsTableVersion_Type.__name__ = "DisplayString"
_CrysMkkCardsTableVersion_Object = MibTableColumn
crysMkkCardsTableVersion = _CrysMkkCardsTableVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 3, 1, 1, 5),
    _CrysMkkCardsTableVersion_Type()
)
crysMkkCardsTableVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysMkkCardsTableVersion.setStatus("current")


class _CrysMkkCardsTableHwID_Type(DisplayString):
    """Custom type crysMkkCardsTableHwID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CrysMkkCardsTableHwID_Type.__name__ = "DisplayString"
_CrysMkkCardsTableHwID_Object = MibTableColumn
crysMkkCardsTableHwID = _CrysMkkCardsTableHwID_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 3, 1, 1, 6),
    _CrysMkkCardsTableHwID_Type()
)
crysMkkCardsTableHwID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysMkkCardsTableHwID.setStatus("current")


class _CrysMkkCardsTableSimcardCount_Type(Integer32):
    """Custom type crysMkkCardsTableSimcardCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CrysMkkCardsTableSimcardCount_Type.__name__ = "Integer32"
_CrysMkkCardsTableSimcardCount_Object = MibTableColumn
crysMkkCardsTableSimcardCount = _CrysMkkCardsTableSimcardCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 3, 1, 1, 7),
    _CrysMkkCardsTableSimcardCount_Type()
)
crysMkkCardsTableSimcardCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysMkkCardsTableSimcardCount.setStatus("current")


class _CrysMkkCardsTableSimcardLogicalStartNr_Type(Integer32):
    """Custom type crysMkkCardsTableSimcardLogicalStartNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CrysMkkCardsTableSimcardLogicalStartNr_Type.__name__ = "Integer32"
_CrysMkkCardsTableSimcardLogicalStartNr_Object = MibTableColumn
crysMkkCardsTableSimcardLogicalStartNr = _CrysMkkCardsTableSimcardLogicalStartNr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 3, 1, 1, 8),
    _CrysMkkCardsTableSimcardLogicalStartNr_Type()
)
crysMkkCardsTableSimcardLogicalStartNr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysMkkCardsTableSimcardLogicalStartNr.setStatus("current")


class _CrysMkkCardsTableSimcardLogicalEndNr_Type(Integer32):
    """Custom type crysMkkCardsTableSimcardLogicalEndNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CrysMkkCardsTableSimcardLogicalEndNr_Type.__name__ = "Integer32"
_CrysMkkCardsTableSimcardLogicalEndNr_Object = MibTableColumn
crysMkkCardsTableSimcardLogicalEndNr = _CrysMkkCardsTableSimcardLogicalEndNr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 3, 1, 1, 9),
    _CrysMkkCardsTableSimcardLogicalEndNr_Type()
)
crysMkkCardsTableSimcardLogicalEndNr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysMkkCardsTableSimcardLogicalEndNr.setStatus("current")


class _CrysMkkCardsTableError_Type(OctetString):
    """Custom type crysMkkCardsTableError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_CrysMkkCardsTableError_Type.__name__ = "OctetString"
_CrysMkkCardsTableError_Object = MibTableColumn
crysMkkCardsTableError = _CrysMkkCardsTableError_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 3, 1, 1, 10),
    _CrysMkkCardsTableError_Type()
)
crysMkkCardsTableError.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysMkkCardsTableError.setStatus("current")
_CrysSimCards_ObjectIdentity = ObjectIdentity
crysSimCards = _CrysSimCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 4, 4)
)
if mibBuilder.loadTexts:
    crysSimCards.setStatus("current")
_CrysSimCardsTable_Object = MibTable
crysSimCardsTable = _CrysSimCardsTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 4, 1)
)
if mibBuilder.loadTexts:
    crysSimCardsTable.setStatus("current")
_CrysSimCardsTableEntry_Object = MibTableRow
crysSimCardsTableEntry = _CrysSimCardsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 4, 1, 1)
)
crysSimCardsTableEntry.setIndexNames(
    (0, "Hagedorn-MIB", "crysSimCardsTableIdx"),
)
if mibBuilder.loadTexts:
    crysSimCardsTableEntry.setStatus("current")


class _CrysSimCardsTableIdx_Type(Integer32):
    """Custom type crysSimCardsTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CrysSimCardsTableIdx_Type.__name__ = "Integer32"
_CrysSimCardsTableIdx_Object = MibTableColumn
crysSimCardsTableIdx = _CrysSimCardsTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 4, 1, 1, 1),
    _CrysSimCardsTableIdx_Type()
)
crysSimCardsTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysSimCardsTableIdx.setStatus("current")
_CrysSimCardsTableRowStatus_Type = RowStatus
_CrysSimCardsTableRowStatus_Object = MibTableColumn
crysSimCardsTableRowStatus = _CrysSimCardsTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 4, 1, 1, 2),
    _CrysSimCardsTableRowStatus_Type()
)
crysSimCardsTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crysSimCardsTableRowStatus.setStatus("current")
_CrysSimCardsTableCardNr_Type = Integer32
_CrysSimCardsTableCardNr_Object = MibTableColumn
crysSimCardsTableCardNr = _CrysSimCardsTableCardNr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 4, 1, 1, 3),
    _CrysSimCardsTableCardNr_Type()
)
crysSimCardsTableCardNr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crysSimCardsTableCardNr.setStatus("current")
_CrysSimCardsTableMkkDaemonNr_Type = Integer32
_CrysSimCardsTableMkkDaemonNr_Object = MibTableColumn
crysSimCardsTableMkkDaemonNr = _CrysSimCardsTableMkkDaemonNr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 4, 1, 1, 4),
    _CrysSimCardsTableMkkDaemonNr_Type()
)
crysSimCardsTableMkkDaemonNr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crysSimCardsTableMkkDaemonNr.setStatus("current")


class _CrysSimCardsTableHwId_Type(OctetString):
    """Custom type crysSimCardsTableHwId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_CrysSimCardsTableHwId_Type.__name__ = "OctetString"
_CrysSimCardsTableHwId_Object = MibTableColumn
crysSimCardsTableHwId = _CrysSimCardsTableHwId_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 4, 1, 1, 5),
    _CrysSimCardsTableHwId_Type()
)
crysSimCardsTableHwId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crysSimCardsTableHwId.setStatus("current")


class _CrysSimCardsTableSubId_Type(DisplayString):
    """Custom type crysSimCardsTableSubId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CrysSimCardsTableSubId_Type.__name__ = "DisplayString"
_CrysSimCardsTableSubId_Object = MibTableColumn
crysSimCardsTableSubId = _CrysSimCardsTableSubId_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 4, 1, 1, 6),
    _CrysSimCardsTableSubId_Type()
)
crysSimCardsTableSubId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crysSimCardsTableSubId.setStatus("current")


class _CrysSimCardsTableHwOpta_Type(DisplayString):
    """Custom type crysSimCardsTableHwOpta based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_CrysSimCardsTableHwOpta_Type.__name__ = "DisplayString"
_CrysSimCardsTableHwOpta_Object = MibTableColumn
crysSimCardsTableHwOpta = _CrysSimCardsTableHwOpta_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 4, 1, 1, 7),
    _CrysSimCardsTableHwOpta_Type()
)
crysSimCardsTableHwOpta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crysSimCardsTableHwOpta.setStatus("current")


class _CrysSimCardsTableStatus_Type(OctetString):
    """Custom type crysSimCardsTableStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_CrysSimCardsTableStatus_Type.__name__ = "OctetString"
_CrysSimCardsTableStatus_Object = MibTableColumn
crysSimCardsTableStatus = _CrysSimCardsTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 4, 1, 1, 8),
    _CrysSimCardsTableStatus_Type()
)
crysSimCardsTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crysSimCardsTableStatus.setStatus("current")


class _CrysSimCardsTableLastSW_Type(OctetString):
    """Custom type crysSimCardsTableLastSW based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_CrysSimCardsTableLastSW_Type.__name__ = "OctetString"
_CrysSimCardsTableLastSW_Object = MibTableColumn
crysSimCardsTableLastSW = _CrysSimCardsTableLastSW_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 4, 1, 1, 9),
    _CrysSimCardsTableLastSW_Type()
)
crysSimCardsTableLastSW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crysSimCardsTableLastSW.setStatus("current")
_CrysCalls_ObjectIdentity = ObjectIdentity
crysCalls = _CrysCalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5)
)
if mibBuilder.loadTexts:
    crysCalls.setStatus("current")
_CrysCallsTable_Object = MibTable
crysCallsTable = _CrysCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1)
)
if mibBuilder.loadTexts:
    crysCallsTable.setStatus("current")
_CrysCallsTableEntry_Object = MibTableRow
crysCallsTableEntry = _CrysCallsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1)
)
crysCallsTableEntry.setIndexNames(
    (0, "Hagedorn-MIB", "crysCallsTableIdx"),
)
if mibBuilder.loadTexts:
    crysCallsTableEntry.setStatus("current")


class _CrysCallsTableIdx_Type(Integer32):
    """Custom type crysCallsTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CrysCallsTableIdx_Type.__name__ = "Integer32"
_CrysCallsTableIdx_Object = MibTableColumn
crysCallsTableIdx = _CrysCallsTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 1),
    _CrysCallsTableIdx_Type()
)
crysCallsTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableIdx.setStatus("current")
_CrysCallsTableRowStatus_Type = RowStatus
_CrysCallsTableRowStatus_Object = MibTableColumn
crysCallsTableRowStatus = _CrysCallsTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 2),
    _CrysCallsTableRowStatus_Type()
)
crysCallsTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crysCallsTableRowStatus.setStatus("current")


class _CrysCallsTableSsrcFromE1_Type(Integer32):
    """Custom type crysCallsTableSsrcFromE1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_CrysCallsTableSsrcFromE1_Type.__name__ = "Integer32"
_CrysCallsTableSsrcFromE1_Object = MibTableColumn
crysCallsTableSsrcFromE1 = _CrysCallsTableSsrcFromE1_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 3),
    _CrysCallsTableSsrcFromE1_Type()
)
crysCallsTableSsrcFromE1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableSsrcFromE1.setStatus("current")


class _CrysCallsTableMkkDaemonNr_Type(Integer32):
    """Custom type crysCallsTableMkkDaemonNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CrysCallsTableMkkDaemonNr_Type.__name__ = "Integer32"
_CrysCallsTableMkkDaemonNr_Object = MibTableColumn
crysCallsTableMkkDaemonNr = _CrysCallsTableMkkDaemonNr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 4),
    _CrysCallsTableMkkDaemonNr_Type()
)
crysCallsTableMkkDaemonNr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableMkkDaemonNr.setStatus("current")


class _CrysCallsTableMkkSimCardNr_Type(Integer32):
    """Custom type crysCallsTableMkkSimCardNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CrysCallsTableMkkSimCardNr_Type.__name__ = "Integer32"
_CrysCallsTableMkkSimCardNr_Object = MibTableColumn
crysCallsTableMkkSimCardNr = _CrysCallsTableMkkSimCardNr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 5),
    _CrysCallsTableMkkSimCardNr_Type()
)
crysCallsTableMkkSimCardNr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableMkkSimCardNr.setStatus("current")
_CrysCallsTableCommType_Type = CrysCallCommType
_CrysCallsTableCommType_Object = MibTableColumn
crysCallsTableCommType = _CrysCallsTableCommType_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 6),
    _CrysCallsTableCommType_Type()
)
crysCallsTableCommType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableCommType.setStatus("current")


class _CrysCallsTableDuplex_Type(Integer32):
    """Custom type crysCallsTableDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CrysCallsTableDuplex_Type.__name__ = "Integer32"
_CrysCallsTableDuplex_Object = MibTableColumn
crysCallsTableDuplex = _CrysCallsTableDuplex_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 7),
    _CrysCallsTableDuplex_Type()
)
crysCallsTableDuplex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableDuplex.setStatus("current")


class _CrysCallsTableE2ee_Type(Integer32):
    """Custom type crysCallsTableE2ee based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CrysCallsTableE2ee_Type.__name__ = "Integer32"
_CrysCallsTableE2ee_Object = MibTableColumn
crysCallsTableE2ee = _CrysCallsTableE2ee_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 8),
    _CrysCallsTableE2ee_Type()
)
crysCallsTableE2ee.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableE2ee.setStatus("current")


class _CrysCallsTableCallerITSI_Type(DisplayString):
    """Custom type crysCallsTableCallerITSI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CrysCallsTableCallerITSI_Type.__name__ = "DisplayString"
_CrysCallsTableCallerITSI_Object = MibTableColumn
crysCallsTableCallerITSI = _CrysCallsTableCallerITSI_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 9),
    _CrysCallsTableCallerITSI_Type()
)
crysCallsTableCallerITSI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableCallerITSI.setStatus("current")


class _CrysCallsTableCallerOpta_Type(DisplayString):
    """Custom type crysCallsTableCallerOpta based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CrysCallsTableCallerOpta_Type.__name__ = "DisplayString"
_CrysCallsTableCallerOpta_Object = MibTableColumn
crysCallsTableCallerOpta = _CrysCallsTableCallerOpta_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 10),
    _CrysCallsTableCallerOpta_Type()
)
crysCallsTableCallerOpta.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableCallerOpta.setStatus("current")


class _CrysCallsTableCalleeTSI_Type(DisplayString):
    """Custom type crysCallsTableCalleeTSI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CrysCallsTableCalleeTSI_Type.__name__ = "DisplayString"
_CrysCallsTableCalleeTSI_Object = MibTableColumn
crysCallsTableCalleeTSI = _CrysCallsTableCalleeTSI_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 11),
    _CrysCallsTableCalleeTSI_Type()
)
crysCallsTableCalleeTSI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableCalleeTSI.setStatus("current")


class _CrysCallsTableCalleeOpta_Type(DisplayString):
    """Custom type crysCallsTableCalleeOpta based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CrysCallsTableCalleeOpta_Type.__name__ = "DisplayString"
_CrysCallsTableCalleeOpta_Object = MibTableColumn
crysCallsTableCalleeOpta = _CrysCallsTableCalleeOpta_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 12),
    _CrysCallsTableCalleeOpta_Type()
)
crysCallsTableCalleeOpta.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableCalleeOpta.setStatus("current")
_CrysCallsTableTalkerType_Type = CrysCallTalkerType
_CrysCallsTableTalkerType_Object = MibTableColumn
crysCallsTableTalkerType = _CrysCallsTableTalkerType_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 13),
    _CrysCallsTableTalkerType_Type()
)
crysCallsTableTalkerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableTalkerType.setStatus("current")


class _CrysCallsTableTalkerITSI_Type(DisplayString):
    """Custom type crysCallsTableTalkerITSI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CrysCallsTableTalkerITSI_Type.__name__ = "DisplayString"
_CrysCallsTableTalkerITSI_Object = MibTableColumn
crysCallsTableTalkerITSI = _CrysCallsTableTalkerITSI_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 14),
    _CrysCallsTableTalkerITSI_Type()
)
crysCallsTableTalkerITSI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableTalkerITSI.setStatus("current")


class _CrysCallsTableTalkerOpta_Type(DisplayString):
    """Custom type crysCallsTableTalkerOpta based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CrysCallsTableTalkerOpta_Type.__name__ = "DisplayString"
_CrysCallsTableTalkerOpta_Object = MibTableColumn
crysCallsTableTalkerOpta = _CrysCallsTableTalkerOpta_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 15),
    _CrysCallsTableTalkerOpta_Type()
)
crysCallsTableTalkerOpta.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableTalkerOpta.setStatus("current")


class _CrysCallsTableStartTime_Type(DisplayString):
    """Custom type crysCallsTableStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CrysCallsTableStartTime_Type.__name__ = "DisplayString"
_CrysCallsTableStartTime_Object = MibTableColumn
crysCallsTableStartTime = _CrysCallsTableStartTime_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 16),
    _CrysCallsTableStartTime_Type()
)
crysCallsTableStartTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableStartTime.setStatus("current")


class _CrysCallsTableLastActivityTime_Type(DisplayString):
    """Custom type crysCallsTableLastActivityTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CrysCallsTableLastActivityTime_Type.__name__ = "DisplayString"
_CrysCallsTableLastActivityTime_Object = MibTableColumn
crysCallsTableLastActivityTime = _CrysCallsTableLastActivityTime_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 17),
    _CrysCallsTableLastActivityTime_Type()
)
crysCallsTableLastActivityTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableLastActivityTime.setStatus("current")


class _CrysCallsTableSimCardLastSW_Type(OctetString):
    """Custom type crysCallsTableSimCardLastSW based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_CrysCallsTableSimCardLastSW_Type.__name__ = "OctetString"
_CrysCallsTableSimCardLastSW_Object = MibTableColumn
crysCallsTableSimCardLastSW = _CrysCallsTableSimCardLastSW_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 18),
    _CrysCallsTableSimCardLastSW_Type()
)
crysCallsTableSimCardLastSW.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableSimCardLastSW.setStatus("current")


class _CrysCallsTableError_Type(Integer32):
    """Custom type crysCallsTableError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CrysCallsTableError_Type.__name__ = "Integer32"
_CrysCallsTableError_Object = MibTableColumn
crysCallsTableError = _CrysCallsTableError_Object(
    (1, 3, 6, 1, 4, 1, 40822, 4, 5, 1, 1, 19),
    _CrysCallsTableError_Type()
)
crysCallsTableError.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crysCallsTableError.setStatus("current")
_Rats_ObjectIdentity = ObjectIdentity
rats = _Rats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 5)
)
if mibBuilder.loadTexts:
    rats.setStatus("current")
_RatsGeneralTraps_ObjectIdentity = ObjectIdentity
ratsGeneralTraps = _RatsGeneralTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 5, 0)
)
if mibBuilder.loadTexts:
    ratsGeneralTraps.setStatus("current")
_RatsGeneral_ObjectIdentity = ObjectIdentity
ratsGeneral = _RatsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1)
)
if mibBuilder.loadTexts:
    ratsGeneral.setStatus("current")
_RatsGenTmg_ObjectIdentity = ObjectIdentity
ratsGenTmg = _RatsGenTmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 1)
)
if mibBuilder.loadTexts:
    ratsGenTmg.setStatus("current")


class _RatsGenTmgListenAddress_Type(DisplayString):
    """Custom type ratsGenTmgListenAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RatsGenTmgListenAddress_Type.__name__ = "DisplayString"
_RatsGenTmgListenAddress_Object = MibScalar
ratsGenTmgListenAddress = _RatsGenTmgListenAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 1, 1),
    _RatsGenTmgListenAddress_Type()
)
ratsGenTmgListenAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenTmgListenAddress.setStatus("current")
_RatsGenTmgListenerState_Type = Integer32
_RatsGenTmgListenerState_Object = MibScalar
ratsGenTmgListenerState = _RatsGenTmgListenerState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 1, 2),
    _RatsGenTmgListenerState_Type()
)
ratsGenTmgListenerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenTmgListenerState.setStatus("current")


class _RatsGenTmgSocketAddress_Type(DisplayString):
    """Custom type ratsGenTmgSocketAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RatsGenTmgSocketAddress_Type.__name__ = "DisplayString"
_RatsGenTmgSocketAddress_Object = MibScalar
ratsGenTmgSocketAddress = _RatsGenTmgSocketAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 1, 3),
    _RatsGenTmgSocketAddress_Type()
)
ratsGenTmgSocketAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenTmgSocketAddress.setStatus("current")
_RatsGenTmgSocketState_Type = Integer32
_RatsGenTmgSocketState_Object = MibScalar
ratsGenTmgSocketState = _RatsGenTmgSocketState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 1, 4),
    _RatsGenTmgSocketState_Type()
)
ratsGenTmgSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenTmgSocketState.setStatus("current")
_RatsGenE1s_ObjectIdentity = ObjectIdentity
ratsGenE1s = _RatsGenE1s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 2)
)
if mibBuilder.loadTexts:
    ratsGenE1s.setStatus("current")


class _RatsGenE1sListenSocketAddress_Type(DisplayString):
    """Custom type ratsGenE1sListenSocketAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RatsGenE1sListenSocketAddress_Type.__name__ = "DisplayString"
_RatsGenE1sListenSocketAddress_Object = MibScalar
ratsGenE1sListenSocketAddress = _RatsGenE1sListenSocketAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 2, 1),
    _RatsGenE1sListenSocketAddress_Type()
)
ratsGenE1sListenSocketAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenE1sListenSocketAddress.setStatus("current")
_RatsGenE1sListenSocketState_Type = Integer32
_RatsGenE1sListenSocketState_Object = MibScalar
ratsGenE1sListenSocketState = _RatsGenE1sListenSocketState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 2, 2),
    _RatsGenE1sListenSocketState_Type()
)
ratsGenE1sListenSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenE1sListenSocketState.setStatus("current")


class _RatsGenE1sSendSocketAddress_Type(DisplayString):
    """Custom type ratsGenE1sSendSocketAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RatsGenE1sSendSocketAddress_Type.__name__ = "DisplayString"
_RatsGenE1sSendSocketAddress_Object = MibScalar
ratsGenE1sSendSocketAddress = _RatsGenE1sSendSocketAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 2, 3),
    _RatsGenE1sSendSocketAddress_Type()
)
ratsGenE1sSendSocketAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenE1sSendSocketAddress.setStatus("current")


class _RatsGenE1sSendToAddress_Type(DisplayString):
    """Custom type ratsGenE1sSendToAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RatsGenE1sSendToAddress_Type.__name__ = "DisplayString"
_RatsGenE1sSendToAddress_Object = MibScalar
ratsGenE1sSendToAddress = _RatsGenE1sSendToAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 2, 4),
    _RatsGenE1sSendToAddress_Type()
)
ratsGenE1sSendToAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenE1sSendToAddress.setStatus("current")
_RatsGenE1sSendSocketState_Type = Integer32
_RatsGenE1sSendSocketState_Object = MibScalar
ratsGenE1sSendSocketState = _RatsGenE1sSendSocketState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 2, 5),
    _RatsGenE1sSendSocketState_Type()
)
ratsGenE1sSendSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenE1sSendSocketState.setStatus("current")
_RatsGenCrys_ObjectIdentity = ObjectIdentity
ratsGenCrys = _RatsGenCrys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 3)
)
if mibBuilder.loadTexts:
    ratsGenCrys.setStatus("current")


class _RatsGenCrysListenSocketAddress_Type(DisplayString):
    """Custom type ratsGenCrysListenSocketAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RatsGenCrysListenSocketAddress_Type.__name__ = "DisplayString"
_RatsGenCrysListenSocketAddress_Object = MibScalar
ratsGenCrysListenSocketAddress = _RatsGenCrysListenSocketAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 3, 1),
    _RatsGenCrysListenSocketAddress_Type()
)
ratsGenCrysListenSocketAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenCrysListenSocketAddress.setStatus("current")
_RatsGenCrysListenSocketState_Type = Integer32
_RatsGenCrysListenSocketState_Object = MibScalar
ratsGenCrysListenSocketState = _RatsGenCrysListenSocketState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 3, 2),
    _RatsGenCrysListenSocketState_Type()
)
ratsGenCrysListenSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenCrysListenSocketState.setStatus("current")


class _RatsGenCrysSendSocketAddress_Type(DisplayString):
    """Custom type ratsGenCrysSendSocketAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RatsGenCrysSendSocketAddress_Type.__name__ = "DisplayString"
_RatsGenCrysSendSocketAddress_Object = MibScalar
ratsGenCrysSendSocketAddress = _RatsGenCrysSendSocketAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 3, 3),
    _RatsGenCrysSendSocketAddress_Type()
)
ratsGenCrysSendSocketAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenCrysSendSocketAddress.setStatus("current")


class _RatsGenCrysSendToAddress_Type(DisplayString):
    """Custom type ratsGenCrysSendToAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RatsGenCrysSendToAddress_Type.__name__ = "DisplayString"
_RatsGenCrysSendToAddress_Object = MibScalar
ratsGenCrysSendToAddress = _RatsGenCrysSendToAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 3, 4),
    _RatsGenCrysSendToAddress_Type()
)
ratsGenCrysSendToAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenCrysSendToAddress.setStatus("current")
_RatsGenCrysSendSocketState_Type = Integer32
_RatsGenCrysSendSocketState_Object = MibScalar
ratsGenCrysSendSocketState = _RatsGenCrysSendSocketState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 3, 5),
    _RatsGenCrysSendSocketState_Type()
)
ratsGenCrysSendSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenCrysSendSocketState.setStatus("current")
_RatsGenStatus_ObjectIdentity = ObjectIdentity
ratsGenStatus = _RatsGenStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 4)
)
if mibBuilder.loadTexts:
    ratsGenStatus.setStatus("current")
_RatsGenStatusConfig_Type = Integer32
_RatsGenStatusConfig_Object = MibScalar
ratsGenStatusConfig = _RatsGenStatusConfig_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 4, 1),
    _RatsGenStatusConfig_Type()
)
ratsGenStatusConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenStatusConfig.setStatus("current")
_RatsGenStatusGroupsCount_Type = Integer32
_RatsGenStatusGroupsCount_Object = MibScalar
ratsGenStatusGroupsCount = _RatsGenStatusGroupsCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 4, 2),
    _RatsGenStatusGroupsCount_Type()
)
ratsGenStatusGroupsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenStatusGroupsCount.setStatus("current")
_RatsGenStatusMembersCount_Type = Integer32
_RatsGenStatusMembersCount_Object = MibScalar
ratsGenStatusMembersCount = _RatsGenStatusMembersCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 5, 1, 4, 3),
    _RatsGenStatusMembersCount_Type()
)
ratsGenStatusMembersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsGenStatusMembersCount.setStatus("current")
_E1s_ObjectIdentity = ObjectIdentity
e1s = _E1s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 6)
)
if mibBuilder.loadTexts:
    e1s.setStatus("current")
_E1sGeneralTraps_ObjectIdentity = ObjectIdentity
e1sGeneralTraps = _E1sGeneralTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 6, 0)
)
if mibBuilder.loadTexts:
    e1sGeneralTraps.setStatus("current")
_E1sGeneral_ObjectIdentity = ObjectIdentity
e1sGeneral = _E1sGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 6, 1)
)
if mibBuilder.loadTexts:
    e1sGeneral.setStatus("current")
_E1sGenTmg_ObjectIdentity = ObjectIdentity
e1sGenTmg = _E1sGenTmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 6, 1, 1)
)
if mibBuilder.loadTexts:
    e1sGenTmg.setStatus("current")


class _E1sGenTmgListenAddress_Type(DisplayString):
    """Custom type e1sGenTmgListenAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_E1sGenTmgListenAddress_Type.__name__ = "DisplayString"
_E1sGenTmgListenAddress_Object = MibScalar
e1sGenTmgListenAddress = _E1sGenTmgListenAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 1, 1, 1),
    _E1sGenTmgListenAddress_Type()
)
e1sGenTmgListenAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1sGenTmgListenAddress.setStatus("current")
_E1sGenTmgListenerState_Type = Integer32
_E1sGenTmgListenerState_Object = MibScalar
e1sGenTmgListenerState = _E1sGenTmgListenerState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 1, 1, 2),
    _E1sGenTmgListenerState_Type()
)
e1sGenTmgListenerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1sGenTmgListenerState.setStatus("current")


class _E1sGenTmgSocketAddress_Type(DisplayString):
    """Custom type e1sGenTmgSocketAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_E1sGenTmgSocketAddress_Type.__name__ = "DisplayString"
_E1sGenTmgSocketAddress_Object = MibScalar
e1sGenTmgSocketAddress = _E1sGenTmgSocketAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 1, 1, 3),
    _E1sGenTmgSocketAddress_Type()
)
e1sGenTmgSocketAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1sGenTmgSocketAddress.setStatus("current")
_E1sGenTmgSocketState_Type = Integer32
_E1sGenTmgSocketState_Object = MibScalar
e1sGenTmgSocketState = _E1sGenTmgSocketState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 1, 1, 4),
    _E1sGenTmgSocketState_Type()
)
e1sGenTmgSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1sGenTmgSocketState.setStatus("current")
_E1sGenComm_ObjectIdentity = ObjectIdentity
e1sGenComm = _E1sGenComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 6, 1, 2)
)
if mibBuilder.loadTexts:
    e1sGenComm.setStatus("current")


class _E1sGenCommListenSocketAddress_Type(DisplayString):
    """Custom type e1sGenCommListenSocketAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_E1sGenCommListenSocketAddress_Type.__name__ = "DisplayString"
_E1sGenCommListenSocketAddress_Object = MibScalar
e1sGenCommListenSocketAddress = _E1sGenCommListenSocketAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 1, 2, 1),
    _E1sGenCommListenSocketAddress_Type()
)
e1sGenCommListenSocketAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1sGenCommListenSocketAddress.setStatus("current")
_E1sGenCommListenSocketState_Type = Integer32
_E1sGenCommListenSocketState_Object = MibScalar
e1sGenCommListenSocketState = _E1sGenCommListenSocketState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 1, 2, 2),
    _E1sGenCommListenSocketState_Type()
)
e1sGenCommListenSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1sGenCommListenSocketState.setStatus("current")


class _E1sGenCommSendSocketAddress_Type(DisplayString):
    """Custom type e1sGenCommSendSocketAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_E1sGenCommSendSocketAddress_Type.__name__ = "DisplayString"
_E1sGenCommSendSocketAddress_Object = MibScalar
e1sGenCommSendSocketAddress = _E1sGenCommSendSocketAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 1, 2, 3),
    _E1sGenCommSendSocketAddress_Type()
)
e1sGenCommSendSocketAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1sGenCommSendSocketAddress.setStatus("current")


class _E1sGenCommSendToAddress_Type(DisplayString):
    """Custom type e1sGenCommSendToAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_E1sGenCommSendToAddress_Type.__name__ = "DisplayString"
_E1sGenCommSendToAddress_Object = MibScalar
e1sGenCommSendToAddress = _E1sGenCommSendToAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 1, 2, 4),
    _E1sGenCommSendToAddress_Type()
)
e1sGenCommSendToAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1sGenCommSendToAddress.setStatus("current")
_E1sGenCommSendSocketState_Type = Integer32
_E1sGenCommSendSocketState_Object = MibScalar
e1sGenCommSendSocketState = _E1sGenCommSendSocketState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 1, 2, 5),
    _E1sGenCommSendSocketState_Type()
)
e1sGenCommSendSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1sGenCommSendSocketState.setStatus("current")
_E1sPorts_ObjectIdentity = ObjectIdentity
e1sPorts = _E1sPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2)
)
if mibBuilder.loadTexts:
    e1sPorts.setStatus("current")
_E1sPortsTable_Object = MibTable
e1sPortsTable = _E1sPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1)
)
if mibBuilder.loadTexts:
    e1sPortsTable.setStatus("current")
_E1sPortsTableEntry_Object = MibTableRow
e1sPortsTableEntry = _E1sPortsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1)
)
e1sPortsTableEntry.setIndexNames(
    (0, "Hagedorn-MIB", "e1sPortsTableIdx"),
)
if mibBuilder.loadTexts:
    e1sPortsTableEntry.setStatus("current")


class _E1sPortsTableIdx_Type(Integer32):
    """Custom type e1sPortsTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_E1sPortsTableIdx_Type.__name__ = "Integer32"
_E1sPortsTableIdx_Object = MibTableColumn
e1sPortsTableIdx = _E1sPortsTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 1),
    _E1sPortsTableIdx_Type()
)
e1sPortsTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e1sPortsTableIdx.setStatus("current")
_E1sPortsTableRowStatus_Type = RowStatus
_E1sPortsTableRowStatus_Object = MibTableColumn
e1sPortsTableRowStatus = _E1sPortsTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 2),
    _E1sPortsTableRowStatus_Type()
)
e1sPortsTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e1sPortsTableRowStatus.setStatus("current")
_E1sPortsTablePortNr_Type = Integer32
_E1sPortsTablePortNr_Object = MibTableColumn
e1sPortsTablePortNr = _E1sPortsTablePortNr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 3),
    _E1sPortsTablePortNr_Type()
)
e1sPortsTablePortNr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTablePortNr.setStatus("current")
_E1sPortsTableStatus_Type = Integer32
_E1sPortsTableStatus_Object = MibTableColumn
e1sPortsTableStatus = _E1sPortsTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 4),
    _E1sPortsTableStatus_Type()
)
e1sPortsTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableStatus.setStatus("current")
_E1sPortsTableAlarm_Type = Integer32
_E1sPortsTableAlarm_Object = MibTableColumn
e1sPortsTableAlarm = _E1sPortsTableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 5),
    _E1sPortsTableAlarm_Type()
)
e1sPortsTableAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableAlarm.setStatus("current")
_E1sPortsTableAIS_Type = Integer32
_E1sPortsTableAIS_Object = MibTableColumn
e1sPortsTableAIS = _E1sPortsTableAIS_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 6),
    _E1sPortsTableAIS_Type()
)
e1sPortsTableAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableAIS.setStatus("current")
_E1sPortsTableALOS_Type = Integer32
_E1sPortsTableALOS_Object = MibTableColumn
e1sPortsTableALOS = _E1sPortsTableALOS_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 7),
    _E1sPortsTableALOS_Type()
)
e1sPortsTableALOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableALOS.setStatus("current")
_E1sPortsTableLCV_Type = Integer32
_E1sPortsTableLCV_Object = MibTableColumn
e1sPortsTableLCV = _E1sPortsTableLCV_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 8),
    _E1sPortsTableLCV_Type()
)
e1sPortsTableLCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableLCV.setStatus("current")
_E1sPortsTableLIULOS_Type = Integer32
_E1sPortsTableLIULOS_Object = MibTableColumn
e1sPortsTableLIULOS = _E1sPortsTableLIULOS_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 9),
    _E1sPortsTableLIULOS_Type()
)
e1sPortsTableLIULOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableLIULOS.setStatus("current")
_E1sPortsTableLIUOC_Type = Integer32
_E1sPortsTableLIUOC_Object = MibTableColumn
e1sPortsTableLIUOC = _E1sPortsTableLIUOC_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 10),
    _E1sPortsTableLIUOC_Type()
)
e1sPortsTableLIUOC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableLIUOC.setStatus("current")
_E1sPortsTableLIUSC_Type = Integer32
_E1sPortsTableLIUSC_Object = MibTableColumn
e1sPortsTableLIUSC = _E1sPortsTableLIUSC_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 11),
    _E1sPortsTableLIUSC_Type()
)
e1sPortsTableLIUSC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableLIUSC.setStatus("current")
_E1sPortsTableLOF_Type = Integer32
_E1sPortsTableLOF_Object = MibTableColumn
e1sPortsTableLOF = _E1sPortsTableLOF_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 12),
    _E1sPortsTableLOF_Type()
)
e1sPortsTableLOF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableLOF.setStatus("current")
_E1sPortsTableLOS_Type = Integer32
_E1sPortsTableLOS_Object = MibTableColumn
e1sPortsTableLOS = _E1sPortsTableLOS_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 13),
    _E1sPortsTableLOS_Type()
)
e1sPortsTableLOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableLOS.setStatus("current")
_E1sPortsTableRAI_Type = Integer32
_E1sPortsTableRAI_Object = MibTableColumn
e1sPortsTableRAI = _E1sPortsTableRAI_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 14),
    _E1sPortsTableRAI_Type()
)
e1sPortsTableRAI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableRAI.setStatus("current")
_E1sPortsTableRED_Type = Integer32
_E1sPortsTableRED_Object = MibTableColumn
e1sPortsTableRED = _E1sPortsTableRED_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 15),
    _E1sPortsTableRED_Type()
)
e1sPortsTableRED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableRED.setStatus("current")
_E1sPortsTableBITErr_Type = Integer32
_E1sPortsTableBITErr_Object = MibTableColumn
e1sPortsTableBITErr = _E1sPortsTableBITErr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 16),
    _E1sPortsTableBITErr_Type()
)
e1sPortsTableBITErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableBITErr.setStatus("current")
_E1sPortsTableCRC4Err_Type = Integer32
_E1sPortsTableCRC4Err_Object = MibTableColumn
e1sPortsTableCRC4Err = _E1sPortsTableCRC4Err_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 17),
    _E1sPortsTableCRC4Err_Type()
)
e1sPortsTableCRC4Err.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableCRC4Err.setStatus("current")
_E1sPortsTableFASErr_Type = Integer32
_E1sPortsTableFASErr_Object = MibTableColumn
e1sPortsTableFASErr = _E1sPortsTableFASErr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 18),
    _E1sPortsTableFASErr_Type()
)
e1sPortsTableFASErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableFASErr.setStatus("current")
_E1sPortsTableFEBErr_Type = Integer32
_E1sPortsTableFEBErr_Object = MibTableColumn
e1sPortsTableFEBErr = _E1sPortsTableFEBErr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 19),
    _E1sPortsTableFEBErr_Type()
)
e1sPortsTableFEBErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableFEBErr.setStatus("current")
_E1sPortsTableFERErr_Type = Integer32
_E1sPortsTableFERErr_Object = MibTableColumn
e1sPortsTableFERErr = _E1sPortsTableFERErr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 20),
    _E1sPortsTableFERErr_Type()
)
e1sPortsTableFERErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableFERErr.setStatus("current")
_E1sPortsTableOOFErr_Type = Integer32
_E1sPortsTableOOFErr_Object = MibTableColumn
e1sPortsTableOOFErr = _E1sPortsTableOOFErr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 6, 2, 1, 1, 21),
    _E1sPortsTableOOFErr_Type()
)
e1sPortsTableOOFErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1sPortsTableOOFErr.setStatus("current")
_IpRadioUnit_ObjectIdentity = ObjectIdentity
ipRadioUnit = _IpRadioUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 7)
)
if mibBuilder.loadTexts:
    ipRadioUnit.setStatus("current")
_IpruProcA_ObjectIdentity = ObjectIdentity
ipruProcA = _IpruProcA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 7, 1)
)
if mibBuilder.loadTexts:
    ipruProcA.setStatus("current")
_IpruProcAProcState_Type = TIPRUProcState
_IpruProcAProcState_Object = MibScalar
ipruProcAProcState = _IpruProcAProcState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 7, 1, 1),
    _IpruProcAProcState_Type()
)
ipruProcAProcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipruProcAProcState.setStatus("current")
_IpruProcAAudioState_Type = TIPRUAudioState
_IpruProcAAudioState_Object = MibScalar
ipruProcAAudioState = _IpruProcAAudioState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 7, 1, 2),
    _IpruProcAAudioState_Type()
)
ipruProcAAudioState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipruProcAAudioState.setStatus("current")
_IpruProcARadioState_Type = TIPRURadioState
_IpruProcARadioState_Object = MibScalar
ipruProcARadioState = _IpruProcARadioState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 7, 1, 3),
    _IpruProcARadioState_Type()
)
ipruProcARadioState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipruProcARadioState.setStatus("current")
_IpruProcAMode_Type = TIPRUMode
_IpruProcAMode_Object = MibScalar
ipruProcAMode = _IpruProcAMode_Object(
    (1, 3, 6, 1, 4, 1, 40822, 7, 1, 4),
    _IpruProcAMode_Type()
)
ipruProcAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipruProcAMode.setStatus("current")


class _IpruProcAActGroup_Type(DisplayString):
    """Custom type ipruProcAActGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpruProcAActGroup_Type.__name__ = "DisplayString"
_IpruProcAActGroup_Object = MibScalar
ipruProcAActGroup = _IpruProcAActGroup_Object(
    (1, 3, 6, 1, 4, 1, 40822, 7, 1, 5),
    _IpruProcAActGroup_Type()
)
ipruProcAActGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipruProcAActGroup.setStatus("current")
_IpruProcARSP_Type = TIPRURSP
_IpruProcARSP_Object = MibScalar
ipruProcARSP = _IpruProcARSP_Object(
    (1, 3, 6, 1, 4, 1, 40822, 7, 1, 6),
    _IpruProcARSP_Type()
)
ipruProcARSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipruProcARSP.setStatus("current")
_IpruProcB_ObjectIdentity = ObjectIdentity
ipruProcB = _IpruProcB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 7, 2)
)
if mibBuilder.loadTexts:
    ipruProcB.setStatus("current")
_IpruProcBProcState_Type = TIPRUProcState
_IpruProcBProcState_Object = MibScalar
ipruProcBProcState = _IpruProcBProcState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 7, 2, 1),
    _IpruProcBProcState_Type()
)
ipruProcBProcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipruProcBProcState.setStatus("current")
_IpruProcBAudioState_Type = TIPRUAudioState
_IpruProcBAudioState_Object = MibScalar
ipruProcBAudioState = _IpruProcBAudioState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 7, 2, 2),
    _IpruProcBAudioState_Type()
)
ipruProcBAudioState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipruProcBAudioState.setStatus("current")
_IpruProcBRadioState_Type = TIPRURadioState
_IpruProcBRadioState_Object = MibScalar
ipruProcBRadioState = _IpruProcBRadioState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 7, 2, 3),
    _IpruProcBRadioState_Type()
)
ipruProcBRadioState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipruProcBRadioState.setStatus("current")
_IpruProcBMode_Type = TIPRUMode
_IpruProcBMode_Object = MibScalar
ipruProcBMode = _IpruProcBMode_Object(
    (1, 3, 6, 1, 4, 1, 40822, 7, 2, 4),
    _IpruProcBMode_Type()
)
ipruProcBMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipruProcBMode.setStatus("current")


class _IpruProcBActGroup_Type(DisplayString):
    """Custom type ipruProcBActGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpruProcBActGroup_Type.__name__ = "DisplayString"
_IpruProcBActGroup_Object = MibScalar
ipruProcBActGroup = _IpruProcBActGroup_Object(
    (1, 3, 6, 1, 4, 1, 40822, 7, 2, 5),
    _IpruProcBActGroup_Type()
)
ipruProcBActGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipruProcBActGroup.setStatus("current")
_IpruProcBRSP_Type = TIPRURSP
_IpruProcBRSP_Object = MibScalar
ipruProcBRSP = _IpruProcBRSP_Object(
    (1, 3, 6, 1, 4, 1, 40822, 7, 2, 6),
    _IpruProcBRSP_Type()
)
ipruProcBRSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipruProcBRSP.setStatus("current")
_AudioBox_ObjectIdentity = ObjectIdentity
audioBox = _AudioBox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 8)
)
if mibBuilder.loadTexts:
    audioBox.setStatus("current")
_AudioBoxProcState_Type = TAudioBoxProcState
_AudioBoxProcState_Object = MibScalar
audioBoxProcState = _AudioBoxProcState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 8, 1),
    _AudioBoxProcState_Type()
)
audioBoxProcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioBoxProcState.setStatus("current")
_AudioBoxAudioState_Type = TAudioBoxAudioState
_AudioBoxAudioState_Object = MibScalar
audioBoxAudioState = _AudioBoxAudioState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 8, 2),
    _AudioBoxAudioState_Type()
)
audioBoxAudioState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioBoxAudioState.setStatus("current")
_Recorder_ObjectIdentity = ObjectIdentity
recorder = _Recorder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 9)
)
if mibBuilder.loadTexts:
    recorder.setStatus("current")
_RecorderGeneral_ObjectIdentity = ObjectIdentity
recorderGeneral = _RecorderGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 9, 1)
)
if mibBuilder.loadTexts:
    recorderGeneral.setStatus("current")


class _RecorderGenVersion_Type(DisplayString):
    """Custom type recorderGenVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RecorderGenVersion_Type.__name__ = "DisplayString"
_RecorderGenVersion_Object = MibScalar
recorderGenVersion = _RecorderGenVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 9, 1, 1),
    _RecorderGenVersion_Type()
)
recorderGenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recorderGenVersion.setStatus("current")
_RecorderGenServiceState_Type = TRecorderServiceState
_RecorderGenServiceState_Object = MibScalar
recorderGenServiceState = _RecorderGenServiceState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 9, 1, 2),
    _RecorderGenServiceState_Type()
)
recorderGenServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recorderGenServiceState.setStatus("current")
_RecorderGenGatewaysConnected_Type = Integer32
_RecorderGenGatewaysConnected_Object = MibScalar
recorderGenGatewaysConnected = _RecorderGenGatewaysConnected_Object(
    (1, 3, 6, 1, 4, 1, 40822, 9, 1, 3),
    _RecorderGenGatewaysConnected_Type()
)
recorderGenGatewaysConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recorderGenGatewaysConnected.setStatus("current")
_RecorderGenDatabaseState_Type = TRecorderDatabaseState
_RecorderGenDatabaseState_Object = MibScalar
recorderGenDatabaseState = _RecorderGenDatabaseState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 9, 1, 4),
    _RecorderGenDatabaseState_Type()
)
recorderGenDatabaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recorderGenDatabaseState.setStatus("current")
_RecorderGenCallCount_Type = Integer32
_RecorderGenCallCount_Object = MibScalar
recorderGenCallCount = _RecorderGenCallCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 9, 1, 5),
    _RecorderGenCallCount_Type()
)
recorderGenCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recorderGenCallCount.setStatus("current")
_RecorderGenSdsCount_Type = Integer32
_RecorderGenSdsCount_Object = MibScalar
recorderGenSdsCount = _RecorderGenSdsCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 9, 1, 6),
    _RecorderGenSdsCount_Type()
)
recorderGenSdsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recorderGenSdsCount.setStatus("current")
_RecorderGenStatusCount_Type = Integer32
_RecorderGenStatusCount_Object = MibScalar
recorderGenStatusCount = _RecorderGenStatusCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 9, 1, 7),
    _RecorderGenStatusCount_Type()
)
recorderGenStatusCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recorderGenStatusCount.setStatus("current")
_RecorderGenFreeSpace_Type = Integer32
_RecorderGenFreeSpace_Object = MibScalar
recorderGenFreeSpace = _RecorderGenFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 40822, 9, 1, 8),
    _RecorderGenFreeSpace_Type()
)
recorderGenFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recorderGenFreeSpace.setStatus("current")
_Systemconfig_ObjectIdentity = ObjectIdentity
systemconfig = _Systemconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 10)
)
if mibBuilder.loadTexts:
    systemconfig.setStatus("current")
_SystemconfigGeneral_ObjectIdentity = ObjectIdentity
systemconfigGeneral = _SystemconfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 10, 1)
)
if mibBuilder.loadTexts:
    systemconfigGeneral.setStatus("current")


class _SystemconfigGenVersion_Type(DisplayString):
    """Custom type systemconfigGenVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemconfigGenVersion_Type.__name__ = "DisplayString"
_SystemconfigGenVersion_Object = MibScalar
systemconfigGenVersion = _SystemconfigGenVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 10, 1, 1),
    _SystemconfigGenVersion_Type()
)
systemconfigGenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemconfigGenVersion.setStatus("current")
_SystemconfigGenWebServiceState_Type = TSystemConfigWebServiceState
_SystemconfigGenWebServiceState_Object = MibScalar
systemconfigGenWebServiceState = _SystemconfigGenWebServiceState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 10, 1, 2),
    _SystemconfigGenWebServiceState_Type()
)
systemconfigGenWebServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemconfigGenWebServiceState.setStatus("current")
_SystemconfigGenXmlDocState_Type = TSystemConfigXmlDocState
_SystemconfigGenXmlDocState_Object = MibScalar
systemconfigGenXmlDocState = _SystemconfigGenXmlDocState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 10, 1, 3),
    _SystemconfigGenXmlDocState_Type()
)
systemconfigGenXmlDocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemconfigGenXmlDocState.setStatus("current")
_SystemconfigGenDatabaseState_Type = TSystemConfigDatabaseState
_SystemconfigGenDatabaseState_Object = MibScalar
systemconfigGenDatabaseState = _SystemconfigGenDatabaseState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 10, 1, 4),
    _SystemconfigGenDatabaseState_Type()
)
systemconfigGenDatabaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemconfigGenDatabaseState.setStatus("current")
_SystemconfigGenPhonebookItemCount_Type = Integer32
_SystemconfigGenPhonebookItemCount_Object = MibScalar
systemconfigGenPhonebookItemCount = _SystemconfigGenPhonebookItemCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 10, 1, 5),
    _SystemconfigGenPhonebookItemCount_Type()
)
systemconfigGenPhonebookItemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemconfigGenPhonebookItemCount.setStatus("current")
_SystemconfigGenAnalogChannelCount_Type = Integer32
_SystemconfigGenAnalogChannelCount_Object = MibScalar
systemconfigGenAnalogChannelCount = _SystemconfigGenAnalogChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 10, 1, 6),
    _SystemconfigGenAnalogChannelCount_Type()
)
systemconfigGenAnalogChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemconfigGenAnalogChannelCount.setStatus("current")
_SystemconfigGenAnalogRadioCount_Type = Integer32
_SystemconfigGenAnalogRadioCount_Object = MibScalar
systemconfigGenAnalogRadioCount = _SystemconfigGenAnalogRadioCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 10, 1, 7),
    _SystemconfigGenAnalogRadioCount_Type()
)
systemconfigGenAnalogRadioCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemconfigGenAnalogRadioCount.setStatus("current")
_SystemconfigGenTetraGroupCount_Type = Integer32
_SystemconfigGenTetraGroupCount_Object = MibScalar
systemconfigGenTetraGroupCount = _SystemconfigGenTetraGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 10, 1, 8),
    _SystemconfigGenTetraGroupCount_Type()
)
systemconfigGenTetraGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemconfigGenTetraGroupCount.setStatus("current")
_SystemconfigGenTetraRadioCount_Type = Integer32
_SystemconfigGenTetraRadioCount_Object = MibScalar
systemconfigGenTetraRadioCount = _SystemconfigGenTetraRadioCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 10, 1, 9),
    _SystemconfigGenTetraRadioCount_Type()
)
systemconfigGenTetraRadioCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemconfigGenTetraRadioCount.setStatus("current")
_SystemconfigGenTetraApplicationCount_Type = Integer32
_SystemconfigGenTetraApplicationCount_Object = MibScalar
systemconfigGenTetraApplicationCount = _SystemconfigGenTetraApplicationCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 10, 1, 10),
    _SystemconfigGenTetraApplicationCount_Type()
)
systemconfigGenTetraApplicationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemconfigGenTetraApplicationCount.setStatus("current")
_Logrotate_ObjectIdentity = ObjectIdentity
logrotate = _Logrotate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 11)
)
if mibBuilder.loadTexts:
    logrotate.setStatus("current")
_LogrotateGeneral_ObjectIdentity = ObjectIdentity
logrotateGeneral = _LogrotateGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 11, 1)
)
if mibBuilder.loadTexts:
    logrotateGeneral.setStatus("current")


class _LogrotateGenVersion_Type(DisplayString):
    """Custom type logrotateGenVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LogrotateGenVersion_Type.__name__ = "DisplayString"
_LogrotateGenVersion_Object = MibScalar
logrotateGenVersion = _LogrotateGenVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 11, 1, 1),
    _LogrotateGenVersion_Type()
)
logrotateGenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logrotateGenVersion.setStatus("current")


class _LogrotateGenTimeStamp_Type(DisplayString):
    """Custom type logrotateGenTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LogrotateGenTimeStamp_Type.__name__ = "DisplayString"
_LogrotateGenTimeStamp_Object = MibScalar
logrotateGenTimeStamp = _LogrotateGenTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 40822, 11, 1, 2),
    _LogrotateGenTimeStamp_Type()
)
logrotateGenTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logrotateGenTimeStamp.setStatus("current")


class _LogrotateGenNewestFile_Type(DisplayString):
    """Custom type logrotateGenNewestFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LogrotateGenNewestFile_Type.__name__ = "DisplayString"
_LogrotateGenNewestFile_Object = MibScalar
logrotateGenNewestFile = _LogrotateGenNewestFile_Object(
    (1, 3, 6, 1, 4, 1, 40822, 11, 1, 3),
    _LogrotateGenNewestFile_Type()
)
logrotateGenNewestFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logrotateGenNewestFile.setStatus("current")


class _LogrotateGenOldestFile_Type(DisplayString):
    """Custom type logrotateGenOldestFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LogrotateGenOldestFile_Type.__name__ = "DisplayString"
_LogrotateGenOldestFile_Object = MibScalar
logrotateGenOldestFile = _LogrotateGenOldestFile_Object(
    (1, 3, 6, 1, 4, 1, 40822, 11, 1, 4),
    _LogrotateGenOldestFile_Type()
)
logrotateGenOldestFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logrotateGenOldestFile.setStatus("current")
_Dbmaintenance_ObjectIdentity = ObjectIdentity
dbmaintenance = _Dbmaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 12)
)
if mibBuilder.loadTexts:
    dbmaintenance.setStatus("current")
_DbmaintenanceGeneral_ObjectIdentity = ObjectIdentity
dbmaintenanceGeneral = _DbmaintenanceGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 12, 1)
)
if mibBuilder.loadTexts:
    dbmaintenanceGeneral.setStatus("current")


class _DbmaintenanceGenVersion_Type(DisplayString):
    """Custom type dbmaintenanceGenVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DbmaintenanceGenVersion_Type.__name__ = "DisplayString"
_DbmaintenanceGenVersion_Object = MibScalar
dbmaintenanceGenVersion = _DbmaintenanceGenVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 1, 1),
    _DbmaintenanceGenVersion_Type()
)
dbmaintenanceGenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceGenVersion.setStatus("current")


class _DbmaintenanceGenBeginTimeStamp_Type(DisplayString):
    """Custom type dbmaintenanceGenBeginTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DbmaintenanceGenBeginTimeStamp_Type.__name__ = "DisplayString"
_DbmaintenanceGenBeginTimeStamp_Object = MibScalar
dbmaintenanceGenBeginTimeStamp = _DbmaintenanceGenBeginTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 1, 2),
    _DbmaintenanceGenBeginTimeStamp_Type()
)
dbmaintenanceGenBeginTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceGenBeginTimeStamp.setStatus("current")


class _DbmaintenanceGenEndTimeStamp_Type(DisplayString):
    """Custom type dbmaintenanceGenEndTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DbmaintenanceGenEndTimeStamp_Type.__name__ = "DisplayString"
_DbmaintenanceGenEndTimeStamp_Object = MibScalar
dbmaintenanceGenEndTimeStamp = _DbmaintenanceGenEndTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 1, 3),
    _DbmaintenanceGenEndTimeStamp_Type()
)
dbmaintenanceGenEndTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceGenEndTimeStamp.setStatus("current")


class _DbmaintenanceGenDBNode_Type(DisplayString):
    """Custom type dbmaintenanceGenDBNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DbmaintenanceGenDBNode_Type.__name__ = "DisplayString"
_DbmaintenanceGenDBNode_Object = MibScalar
dbmaintenanceGenDBNode = _DbmaintenanceGenDBNode_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 1, 4),
    _DbmaintenanceGenDBNode_Type()
)
dbmaintenanceGenDBNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceGenDBNode.setStatus("current")


class _DbmaintenanceGenDBName_Type(DisplayString):
    """Custom type dbmaintenanceGenDBName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DbmaintenanceGenDBName_Type.__name__ = "DisplayString"
_DbmaintenanceGenDBName_Object = MibScalar
dbmaintenanceGenDBName = _DbmaintenanceGenDBName_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 1, 5),
    _DbmaintenanceGenDBName_Type()
)
dbmaintenanceGenDBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceGenDBName.setStatus("current")
_DbmaintenanceGenDBConnectionState_Type = TConnectionState
_DbmaintenanceGenDBConnectionState_Object = MibScalar
dbmaintenanceGenDBConnectionState = _DbmaintenanceGenDBConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 1, 6),
    _DbmaintenanceGenDBConnectionState_Type()
)
dbmaintenanceGenDBConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceGenDBConnectionState.setStatus("current")


class _DbmaintenanceGenDbConnectionStateTStamp_Type(DisplayString):
    """Custom type dbmaintenanceGenDbConnectionStateTStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DbmaintenanceGenDbConnectionStateTStamp_Type.__name__ = "DisplayString"
_DbmaintenanceGenDbConnectionStateTStamp_Object = MibScalar
dbmaintenanceGenDbConnectionStateTStamp = _DbmaintenanceGenDbConnectionStateTStamp_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 1, 7),
    _DbmaintenanceGenDbConnectionStateTStamp_Type()
)
dbmaintenanceGenDbConnectionStateTStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceGenDbConnectionStateTStamp.setStatus("current")
_DbmaintenanceGenForceTime_Type = Integer32
_DbmaintenanceGenForceTime_Object = MibScalar
dbmaintenanceGenForceTime = _DbmaintenanceGenForceTime_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 1, 8),
    _DbmaintenanceGenForceTime_Type()
)
dbmaintenanceGenForceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceGenForceTime.setStatus("current")
_DbmaintenanceGenMaintenaceInterval_Type = Integer32
_DbmaintenanceGenMaintenaceInterval_Object = MibScalar
dbmaintenanceGenMaintenaceInterval = _DbmaintenanceGenMaintenaceInterval_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 1, 9),
    _DbmaintenanceGenMaintenaceInterval_Type()
)
dbmaintenanceGenMaintenaceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceGenMaintenaceInterval.setStatus("current")
_DbmaintenanceGenCheckInterval_Type = Integer32
_DbmaintenanceGenCheckInterval_Object = MibScalar
dbmaintenanceGenCheckInterval = _DbmaintenanceGenCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 1, 10),
    _DbmaintenanceGenCheckInterval_Type()
)
dbmaintenanceGenCheckInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceGenCheckInterval.setStatus("current")
_DbmaintenanceCall_ObjectIdentity = ObjectIdentity
dbmaintenanceCall = _DbmaintenanceCall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 12, 2)
)
if mibBuilder.loadTexts:
    dbmaintenanceCall.setStatus("current")
_DbmaintenanceCallIsTimeLimit_Type = Integer32
_DbmaintenanceCallIsTimeLimit_Object = MibScalar
dbmaintenanceCallIsTimeLimit = _DbmaintenanceCallIsTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 2, 1),
    _DbmaintenanceCallIsTimeLimit_Type()
)
dbmaintenanceCallIsTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceCallIsTimeLimit.setStatus("current")
_DbmaintenanceCallTimeLimitVal_Type = Integer32
_DbmaintenanceCallTimeLimitVal_Object = MibScalar
dbmaintenanceCallTimeLimitVal = _DbmaintenanceCallTimeLimitVal_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 2, 2),
    _DbmaintenanceCallTimeLimitVal_Type()
)
dbmaintenanceCallTimeLimitVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceCallTimeLimitVal.setStatus("current")
_DbmaintenanceCallTimeLimitUnit_Type = TTimeLimitUnit
_DbmaintenanceCallTimeLimitUnit_Object = MibScalar
dbmaintenanceCallTimeLimitUnit = _DbmaintenanceCallTimeLimitUnit_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 2, 3),
    _DbmaintenanceCallTimeLimitUnit_Type()
)
dbmaintenanceCallTimeLimitUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceCallTimeLimitUnit.setStatus("current")


class _DbmaintenanceCallSimplexSQLStmt_Type(DisplayString):
    """Custom type dbmaintenanceCallSimplexSQLStmt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DbmaintenanceCallSimplexSQLStmt_Type.__name__ = "DisplayString"
_DbmaintenanceCallSimplexSQLStmt_Object = MibScalar
dbmaintenanceCallSimplexSQLStmt = _DbmaintenanceCallSimplexSQLStmt_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 2, 4),
    _DbmaintenanceCallSimplexSQLStmt_Type()
)
dbmaintenanceCallSimplexSQLStmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceCallSimplexSQLStmt.setStatus("current")
_DbmaintenanceCallSimplexSQLResCount_Type = Integer32
_DbmaintenanceCallSimplexSQLResCount_Object = MibScalar
dbmaintenanceCallSimplexSQLResCount = _DbmaintenanceCallSimplexSQLResCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 2, 5),
    _DbmaintenanceCallSimplexSQLResCount_Type()
)
dbmaintenanceCallSimplexSQLResCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceCallSimplexSQLResCount.setStatus("current")


class _DbmaintenanceCallDuplexSQLStmt_Type(DisplayString):
    """Custom type dbmaintenanceCallDuplexSQLStmt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DbmaintenanceCallDuplexSQLStmt_Type.__name__ = "DisplayString"
_DbmaintenanceCallDuplexSQLStmt_Object = MibScalar
dbmaintenanceCallDuplexSQLStmt = _DbmaintenanceCallDuplexSQLStmt_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 2, 6),
    _DbmaintenanceCallDuplexSQLStmt_Type()
)
dbmaintenanceCallDuplexSQLStmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceCallDuplexSQLStmt.setStatus("current")
_DbmaintenanceCallDuplexSQLResCount_Type = Integer32
_DbmaintenanceCallDuplexSQLResCount_Object = MibScalar
dbmaintenanceCallDuplexSQLResCount = _DbmaintenanceCallDuplexSQLResCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 2, 7),
    _DbmaintenanceCallDuplexSQLResCount_Type()
)
dbmaintenanceCallDuplexSQLResCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceCallDuplexSQLResCount.setStatus("current")
_DbmaintenanceCallAudioIsTimeLimit_Type = Integer32
_DbmaintenanceCallAudioIsTimeLimit_Object = MibScalar
dbmaintenanceCallAudioIsTimeLimit = _DbmaintenanceCallAudioIsTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 2, 8),
    _DbmaintenanceCallAudioIsTimeLimit_Type()
)
dbmaintenanceCallAudioIsTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceCallAudioIsTimeLimit.setStatus("current")
_DbmaintenanceCallAudioTimeLimitVal_Type = Integer32
_DbmaintenanceCallAudioTimeLimitVal_Object = MibScalar
dbmaintenanceCallAudioTimeLimitVal = _DbmaintenanceCallAudioTimeLimitVal_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 2, 9),
    _DbmaintenanceCallAudioTimeLimitVal_Type()
)
dbmaintenanceCallAudioTimeLimitVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceCallAudioTimeLimitVal.setStatus("current")
_DbmaintenanceCallAudioTimeLimitUnit_Type = Integer32
_DbmaintenanceCallAudioTimeLimitUnit_Object = MibScalar
dbmaintenanceCallAudioTimeLimitUnit = _DbmaintenanceCallAudioTimeLimitUnit_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 2, 10),
    _DbmaintenanceCallAudioTimeLimitUnit_Type()
)
dbmaintenanceCallAudioTimeLimitUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceCallAudioTimeLimitUnit.setStatus("current")
_DbmaintenanceSDS_ObjectIdentity = ObjectIdentity
dbmaintenanceSDS = _DbmaintenanceSDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 12, 3)
)
if mibBuilder.loadTexts:
    dbmaintenanceSDS.setStatus("current")
_DbmaintenanceSDSIsTimeLimit_Type = Integer32
_DbmaintenanceSDSIsTimeLimit_Object = MibScalar
dbmaintenanceSDSIsTimeLimit = _DbmaintenanceSDSIsTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 3, 1),
    _DbmaintenanceSDSIsTimeLimit_Type()
)
dbmaintenanceSDSIsTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceSDSIsTimeLimit.setStatus("current")
_DbmaintenanceSDSTimeLimitVal_Type = Integer32
_DbmaintenanceSDSTimeLimitVal_Object = MibScalar
dbmaintenanceSDSTimeLimitVal = _DbmaintenanceSDSTimeLimitVal_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 3, 2),
    _DbmaintenanceSDSTimeLimitVal_Type()
)
dbmaintenanceSDSTimeLimitVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceSDSTimeLimitVal.setStatus("current")
_DbmaintenanceSDSTimeLimitUnit_Type = TTimeLimitUnit
_DbmaintenanceSDSTimeLimitUnit_Object = MibScalar
dbmaintenanceSDSTimeLimitUnit = _DbmaintenanceSDSTimeLimitUnit_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 3, 3),
    _DbmaintenanceSDSTimeLimitUnit_Type()
)
dbmaintenanceSDSTimeLimitUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceSDSTimeLimitUnit.setStatus("current")


class _DbmaintenanceSDSSQLStmt_Type(DisplayString):
    """Custom type dbmaintenanceSDSSQLStmt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DbmaintenanceSDSSQLStmt_Type.__name__ = "DisplayString"
_DbmaintenanceSDSSQLStmt_Object = MibScalar
dbmaintenanceSDSSQLStmt = _DbmaintenanceSDSSQLStmt_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 3, 4),
    _DbmaintenanceSDSSQLStmt_Type()
)
dbmaintenanceSDSSQLStmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceSDSSQLStmt.setStatus("current")
_DbmaintenanceSDSSQLResCount_Type = Integer32
_DbmaintenanceSDSSQLResCount_Object = MibScalar
dbmaintenanceSDSSQLResCount = _DbmaintenanceSDSSQLResCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 3, 5),
    _DbmaintenanceSDSSQLResCount_Type()
)
dbmaintenanceSDSSQLResCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceSDSSQLResCount.setStatus("current")
_DbmaintenanceStatus_ObjectIdentity = ObjectIdentity
dbmaintenanceStatus = _DbmaintenanceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 12, 4)
)
if mibBuilder.loadTexts:
    dbmaintenanceStatus.setStatus("current")
_DbmaintenanceStatusIsTimeLimit_Type = Integer32
_DbmaintenanceStatusIsTimeLimit_Object = MibScalar
dbmaintenanceStatusIsTimeLimit = _DbmaintenanceStatusIsTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 4, 1),
    _DbmaintenanceStatusIsTimeLimit_Type()
)
dbmaintenanceStatusIsTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceStatusIsTimeLimit.setStatus("current")
_DbmaintenanceStatusTimeLimitVal_Type = Integer32
_DbmaintenanceStatusTimeLimitVal_Object = MibScalar
dbmaintenanceStatusTimeLimitVal = _DbmaintenanceStatusTimeLimitVal_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 4, 2),
    _DbmaintenanceStatusTimeLimitVal_Type()
)
dbmaintenanceStatusTimeLimitVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceStatusTimeLimitVal.setStatus("current")
_DbmaintenanceStatusTimeLimitUnit_Type = TTimeLimitUnit
_DbmaintenanceStatusTimeLimitUnit_Object = MibScalar
dbmaintenanceStatusTimeLimitUnit = _DbmaintenanceStatusTimeLimitUnit_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 4, 3),
    _DbmaintenanceStatusTimeLimitUnit_Type()
)
dbmaintenanceStatusTimeLimitUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceStatusTimeLimitUnit.setStatus("current")


class _DbmaintenanceStatusSQLStmt_Type(DisplayString):
    """Custom type dbmaintenanceStatusSQLStmt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DbmaintenanceStatusSQLStmt_Type.__name__ = "DisplayString"
_DbmaintenanceStatusSQLStmt_Object = MibScalar
dbmaintenanceStatusSQLStmt = _DbmaintenanceStatusSQLStmt_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 4, 4),
    _DbmaintenanceStatusSQLStmt_Type()
)
dbmaintenanceStatusSQLStmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceStatusSQLStmt.setStatus("current")
_DbmaintenanceStatusSQLResCount_Type = Integer32
_DbmaintenanceStatusSQLResCount_Object = MibScalar
dbmaintenanceStatusSQLResCount = _DbmaintenanceStatusSQLResCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 12, 4, 5),
    _DbmaintenanceStatusSQLResCount_Type()
)
dbmaintenanceStatusSQLResCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbmaintenanceStatusSQLResCount.setStatus("current")
_DbWatchdog_ObjectIdentity = ObjectIdentity
dbWatchdog = _DbWatchdog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 13)
)
if mibBuilder.loadTexts:
    dbWatchdog.setStatus("current")
_DbWatchdogGeneral_ObjectIdentity = ObjectIdentity
dbWatchdogGeneral = _DbWatchdogGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 13, 1)
)
if mibBuilder.loadTexts:
    dbWatchdogGeneral.setStatus("current")


class _DbWatchdogGenVersion_Type(DisplayString):
    """Custom type dbWatchdogGenVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DbWatchdogGenVersion_Type.__name__ = "DisplayString"
_DbWatchdogGenVersion_Object = MibScalar
dbWatchdogGenVersion = _DbWatchdogGenVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 13, 1, 1),
    _DbWatchdogGenVersion_Type()
)
dbWatchdogGenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbWatchdogGenVersion.setStatus("current")


class _DbWatchdogGenTimeStamp_Type(DisplayString):
    """Custom type dbWatchdogGenTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DbWatchdogGenTimeStamp_Type.__name__ = "DisplayString"
_DbWatchdogGenTimeStamp_Object = MibScalar
dbWatchdogGenTimeStamp = _DbWatchdogGenTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 40822, 13, 1, 2),
    _DbWatchdogGenTimeStamp_Type()
)
dbWatchdogGenTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbWatchdogGenTimeStamp.setStatus("current")


class _DbWatchdogGenName_Type(DisplayString):
    """Custom type dbWatchdogGenName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DbWatchdogGenName_Type.__name__ = "DisplayString"
_DbWatchdogGenName_Object = MibScalar
dbWatchdogGenName = _DbWatchdogGenName_Object(
    (1, 3, 6, 1, 4, 1, 40822, 13, 1, 3),
    _DbWatchdogGenName_Type()
)
dbWatchdogGenName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbWatchdogGenName.setStatus("current")


class _DbWatchdogGenNode_Type(DisplayString):
    """Custom type dbWatchdogGenNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DbWatchdogGenNode_Type.__name__ = "DisplayString"
_DbWatchdogGenNode_Object = MibScalar
dbWatchdogGenNode = _DbWatchdogGenNode_Object(
    (1, 3, 6, 1, 4, 1, 40822, 13, 1, 4),
    _DbWatchdogGenNode_Type()
)
dbWatchdogGenNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbWatchdogGenNode.setStatus("current")


class _DbWatchdogGenEngine_Type(DisplayString):
    """Custom type dbWatchdogGenEngine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DbWatchdogGenEngine_Type.__name__ = "DisplayString"
_DbWatchdogGenEngine_Object = MibScalar
dbWatchdogGenEngine = _DbWatchdogGenEngine_Object(
    (1, 3, 6, 1, 4, 1, 40822, 13, 1, 5),
    _DbWatchdogGenEngine_Type()
)
dbWatchdogGenEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbWatchdogGenEngine.setStatus("current")
_DbWatchdogGenConnectionState_Type = TConnectionState
_DbWatchdogGenConnectionState_Object = MibScalar
dbWatchdogGenConnectionState = _DbWatchdogGenConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 13, 1, 6),
    _DbWatchdogGenConnectionState_Type()
)
dbWatchdogGenConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbWatchdogGenConnectionState.setStatus("current")
_TmgProxy_ObjectIdentity = ObjectIdentity
tmgProxy = _TmgProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 14)
)
if mibBuilder.loadTexts:
    tmgProxy.setStatus("current")
_TmgProxyGeneral_ObjectIdentity = ObjectIdentity
tmgProxyGeneral = _TmgProxyGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 14, 1)
)
if mibBuilder.loadTexts:
    tmgProxyGeneral.setStatus("current")


class _TmgProxyGenVersion_Type(DisplayString):
    """Custom type tmgProxyGenVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgProxyGenVersion_Type.__name__ = "DisplayString"
_TmgProxyGenVersion_Object = MibScalar
tmgProxyGenVersion = _TmgProxyGenVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 1, 1),
    _TmgProxyGenVersion_Type()
)
tmgProxyGenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmgProxyGenVersion.setStatus("current")
_TmgProxyGenServiceState_Type = TTmgProxyServiceState
_TmgProxyGenServiceState_Object = MibScalar
tmgProxyGenServiceState = _TmgProxyGenServiceState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 1, 2),
    _TmgProxyGenServiceState_Type()
)
tmgProxyGenServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmgProxyGenServiceState.setStatus("current")
_TmgProxyGenRATSState_Type = TGeneralState
_TmgProxyGenRATSState_Object = MibScalar
tmgProxyGenRATSState = _TmgProxyGenRATSState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 1, 3),
    _TmgProxyGenRATSState_Type()
)
tmgProxyGenRATSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmgProxyGenRATSState.setStatus("current")
_TmgProxyGenLicenceState_Type = TLicenceState
_TmgProxyGenLicenceState_Object = MibScalar
tmgProxyGenLicenceState = _TmgProxyGenLicenceState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 1, 4),
    _TmgProxyGenLicenceState_Type()
)
tmgProxyGenLicenceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmgProxyGenLicenceState.setStatus("current")
_TmgProxyDrGwClients_ObjectIdentity = ObjectIdentity
tmgProxyDrGwClients = _TmgProxyDrGwClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 14, 2)
)
if mibBuilder.loadTexts:
    tmgProxyDrGwClients.setStatus("current")
_TmgProxyDrGwClientsTable_Object = MibTable
tmgProxyDrGwClientsTable = _TmgProxyDrGwClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 2, 1)
)
if mibBuilder.loadTexts:
    tmgProxyDrGwClientsTable.setStatus("current")
_TmgProxyDrGwClientsTableEntry_Object = MibTableRow
tmgProxyDrGwClientsTableEntry = _TmgProxyDrGwClientsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 2, 1, 1)
)
tmgProxyDrGwClientsTableEntry.setIndexNames(
    (0, "Hagedorn-MIB", "tmgProxyDrGwClientsTableIdx"),
)
if mibBuilder.loadTexts:
    tmgProxyDrGwClientsTableEntry.setStatus("current")


class _TmgProxyDrGwClientsTableIdx_Type(Integer32):
    """Custom type tmgProxyDrGwClientsTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmgProxyDrGwClientsTableIdx_Type.__name__ = "Integer32"
_TmgProxyDrGwClientsTableIdx_Object = MibTableColumn
tmgProxyDrGwClientsTableIdx = _TmgProxyDrGwClientsTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 2, 1, 1, 1),
    _TmgProxyDrGwClientsTableIdx_Type()
)
tmgProxyDrGwClientsTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmgProxyDrGwClientsTableIdx.setStatus("current")
_TmgProxyDrGwClientsTableRowStatus_Type = RowStatus
_TmgProxyDrGwClientsTableRowStatus_Object = MibTableColumn
tmgProxyDrGwClientsTableRowStatus = _TmgProxyDrGwClientsTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 2, 1, 1, 2),
    _TmgProxyDrGwClientsTableRowStatus_Type()
)
tmgProxyDrGwClientsTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmgProxyDrGwClientsTableRowStatus.setStatus("current")


class _TmgProxyDrGwClientsTableName_Type(DisplayString):
    """Custom type tmgProxyDrGwClientsTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgProxyDrGwClientsTableName_Type.__name__ = "DisplayString"
_TmgProxyDrGwClientsTableName_Object = MibTableColumn
tmgProxyDrGwClientsTableName = _TmgProxyDrGwClientsTableName_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 2, 1, 1, 3),
    _TmgProxyDrGwClientsTableName_Type()
)
tmgProxyDrGwClientsTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgProxyDrGwClientsTableName.setStatus("current")


class _TmgProxyDrGwClientsTableDescription_Type(DisplayString):
    """Custom type tmgProxyDrGwClientsTableDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgProxyDrGwClientsTableDescription_Type.__name__ = "DisplayString"
_TmgProxyDrGwClientsTableDescription_Object = MibTableColumn
tmgProxyDrGwClientsTableDescription = _TmgProxyDrGwClientsTableDescription_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 2, 1, 1, 4),
    _TmgProxyDrGwClientsTableDescription_Type()
)
tmgProxyDrGwClientsTableDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgProxyDrGwClientsTableDescription.setStatus("current")
_TmgProxyDrGwClientsTableType_Type = TDrGwClientType
_TmgProxyDrGwClientsTableType_Object = MibTableColumn
tmgProxyDrGwClientsTableType = _TmgProxyDrGwClientsTableType_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 2, 1, 1, 5),
    _TmgProxyDrGwClientsTableType_Type()
)
tmgProxyDrGwClientsTableType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgProxyDrGwClientsTableType.setStatus("current")
_TmgProxyDrGwClientsTableSipState_Type = TGeneralState
_TmgProxyDrGwClientsTableSipState_Object = MibTableColumn
tmgProxyDrGwClientsTableSipState = _TmgProxyDrGwClientsTableSipState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 2, 1, 1, 6),
    _TmgProxyDrGwClientsTableSipState_Type()
)
tmgProxyDrGwClientsTableSipState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgProxyDrGwClientsTableSipState.setStatus("current")
_TmgProxyDrGwClientsTableSoapState_Type = TGeneralState
_TmgProxyDrGwClientsTableSoapState_Object = MibTableColumn
tmgProxyDrGwClientsTableSoapState = _TmgProxyDrGwClientsTableSoapState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 2, 1, 1, 7),
    _TmgProxyDrGwClientsTableSoapState_Type()
)
tmgProxyDrGwClientsTableSoapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgProxyDrGwClientsTableSoapState.setStatus("current")
_TmgProxyClients_ObjectIdentity = ObjectIdentity
tmgProxyClients = _TmgProxyClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 14, 3)
)
if mibBuilder.loadTexts:
    tmgProxyClients.setStatus("current")
_TmgProxyClientsTable_Object = MibTable
tmgProxyClientsTable = _TmgProxyClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 3, 1)
)
if mibBuilder.loadTexts:
    tmgProxyClientsTable.setStatus("current")
_TmgProxyClientsTableEntry_Object = MibTableRow
tmgProxyClientsTableEntry = _TmgProxyClientsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 3, 1, 1)
)
tmgProxyClientsTableEntry.setIndexNames(
    (0, "Hagedorn-MIB", "tmgProxyClientsTableIdx"),
)
if mibBuilder.loadTexts:
    tmgProxyClientsTableEntry.setStatus("current")


class _TmgProxyClientsTableIdx_Type(Integer32):
    """Custom type tmgProxyClientsTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmgProxyClientsTableIdx_Type.__name__ = "Integer32"
_TmgProxyClientsTableIdx_Object = MibTableColumn
tmgProxyClientsTableIdx = _TmgProxyClientsTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 3, 1, 1, 1),
    _TmgProxyClientsTableIdx_Type()
)
tmgProxyClientsTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmgProxyClientsTableIdx.setStatus("current")
_TmgProxyClientsTableRowStatus_Type = RowStatus
_TmgProxyClientsTableRowStatus_Object = MibTableColumn
tmgProxyClientsTableRowStatus = _TmgProxyClientsTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 3, 1, 1, 2),
    _TmgProxyClientsTableRowStatus_Type()
)
tmgProxyClientsTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmgProxyClientsTableRowStatus.setStatus("current")


class _TmgProxyClientsTableName_Type(SnmpAdminString):
    """Custom type tmgProxyClientsTableName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgProxyClientsTableName_Type.__name__ = "SnmpAdminString"
_TmgProxyClientsTableName_Object = MibTableColumn
tmgProxyClientsTableName = _TmgProxyClientsTableName_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 3, 1, 1, 3),
    _TmgProxyClientsTableName_Type()
)
tmgProxyClientsTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgProxyClientsTableName.setStatus("current")


class _TmgProxyClientsTableVersion_Type(DisplayString):
    """Custom type tmgProxyClientsTableVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgProxyClientsTableVersion_Type.__name__ = "DisplayString"
_TmgProxyClientsTableVersion_Object = MibTableColumn
tmgProxyClientsTableVersion = _TmgProxyClientsTableVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 3, 1, 1, 4),
    _TmgProxyClientsTableVersion_Type()
)
tmgProxyClientsTableVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgProxyClientsTableVersion.setStatus("current")
_TmgProxyClientsTableConnectionType_Type = TClientConnectionType
_TmgProxyClientsTableConnectionType_Object = MibTableColumn
tmgProxyClientsTableConnectionType = _TmgProxyClientsTableConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 3, 1, 1, 5),
    _TmgProxyClientsTableConnectionType_Type()
)
tmgProxyClientsTableConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgProxyClientsTableConnectionType.setStatus("current")


class _TmgProxyClientsTableSipIpPort_Type(DisplayString):
    """Custom type tmgProxyClientsTableSipIpPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgProxyClientsTableSipIpPort_Type.__name__ = "DisplayString"
_TmgProxyClientsTableSipIpPort_Object = MibTableColumn
tmgProxyClientsTableSipIpPort = _TmgProxyClientsTableSipIpPort_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 3, 1, 1, 6),
    _TmgProxyClientsTableSipIpPort_Type()
)
tmgProxyClientsTableSipIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgProxyClientsTableSipIpPort.setStatus("current")


class _TmgProxyClientsTableSipDrGwVersion_Type(DisplayString):
    """Custom type tmgProxyClientsTableSipDrGwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgProxyClientsTableSipDrGwVersion_Type.__name__ = "DisplayString"
_TmgProxyClientsTableSipDrGwVersion_Object = MibTableColumn
tmgProxyClientsTableSipDrGwVersion = _TmgProxyClientsTableSipDrGwVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 3, 1, 1, 7),
    _TmgProxyClientsTableSipDrGwVersion_Type()
)
tmgProxyClientsTableSipDrGwVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgProxyClientsTableSipDrGwVersion.setStatus("current")
_TmgProxyClientsTableSipState_Type = TClientState
_TmgProxyClientsTableSipState_Object = MibTableColumn
tmgProxyClientsTableSipState = _TmgProxyClientsTableSipState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 3, 1, 1, 8),
    _TmgProxyClientsTableSipState_Type()
)
tmgProxyClientsTableSipState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgProxyClientsTableSipState.setStatus("current")


class _TmgProxyClientsTableSoapIpPort_Type(DisplayString):
    """Custom type tmgProxyClientsTableSoapIpPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgProxyClientsTableSoapIpPort_Type.__name__ = "DisplayString"
_TmgProxyClientsTableSoapIpPort_Object = MibTableColumn
tmgProxyClientsTableSoapIpPort = _TmgProxyClientsTableSoapIpPort_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 3, 1, 1, 9),
    _TmgProxyClientsTableSoapIpPort_Type()
)
tmgProxyClientsTableSoapIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgProxyClientsTableSoapIpPort.setStatus("current")


class _TmgProxyClientsTableSoapDrGwVersion_Type(DisplayString):
    """Custom type tmgProxyClientsTableSoapDrGwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgProxyClientsTableSoapDrGwVersion_Type.__name__ = "DisplayString"
_TmgProxyClientsTableSoapDrGwVersion_Object = MibTableColumn
tmgProxyClientsTableSoapDrGwVersion = _TmgProxyClientsTableSoapDrGwVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 3, 1, 1, 10),
    _TmgProxyClientsTableSoapDrGwVersion_Type()
)
tmgProxyClientsTableSoapDrGwVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgProxyClientsTableSoapDrGwVersion.setStatus("current")
_TmgProxyClientsTableSoapState_Type = TClientState
_TmgProxyClientsTableSoapState_Object = MibTableColumn
tmgProxyClientsTableSoapState = _TmgProxyClientsTableSoapState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 3, 1, 1, 11),
    _TmgProxyClientsTableSoapState_Type()
)
tmgProxyClientsTableSoapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgProxyClientsTableSoapState.setStatus("current")
_TmgProxyClientsTableGroupDialogCount_Type = Integer32
_TmgProxyClientsTableGroupDialogCount_Object = MibTableColumn
tmgProxyClientsTableGroupDialogCount = _TmgProxyClientsTableGroupDialogCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 3, 1, 1, 12),
    _TmgProxyClientsTableGroupDialogCount_Type()
)
tmgProxyClientsTableGroupDialogCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgProxyClientsTableGroupDialogCount.setStatus("current")
_TmgProxyClientsTableIndividualDialogCount_Type = Integer32
_TmgProxyClientsTableIndividualDialogCount_Object = MibTableColumn
tmgProxyClientsTableIndividualDialogCount = _TmgProxyClientsTableIndividualDialogCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 14, 3, 1, 1, 13),
    _TmgProxyClientsTableIndividualDialogCount_Type()
)
tmgProxyClientsTableIndividualDialogCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgProxyClientsTableIndividualDialogCount.setStatus("current")
_RatsProxy_ObjectIdentity = ObjectIdentity
ratsProxy = _RatsProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 15)
)
if mibBuilder.loadTexts:
    ratsProxy.setStatus("current")
_RatsProxyGeneral_ObjectIdentity = ObjectIdentity
ratsProxyGeneral = _RatsProxyGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 15, 1)
)
if mibBuilder.loadTexts:
    ratsProxyGeneral.setStatus("current")


class _RatsProxyGenVersion_Type(DisplayString):
    """Custom type ratsProxyGenVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RatsProxyGenVersion_Type.__name__ = "DisplayString"
_RatsProxyGenVersion_Object = MibScalar
ratsProxyGenVersion = _RatsProxyGenVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 15, 1, 1),
    _RatsProxyGenVersion_Type()
)
ratsProxyGenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsProxyGenVersion.setStatus("current")


class _RatsProxyGenTmgListenAddress_Type(DisplayString):
    """Custom type ratsProxyGenTmgListenAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RatsProxyGenTmgListenAddress_Type.__name__ = "DisplayString"
_RatsProxyGenTmgListenAddress_Object = MibScalar
ratsProxyGenTmgListenAddress = _RatsProxyGenTmgListenAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 15, 1, 2),
    _RatsProxyGenTmgListenAddress_Type()
)
ratsProxyGenTmgListenAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsProxyGenTmgListenAddress.setStatus("current")
_RatsProxyGenTmgListenerState_Type = Integer32
_RatsProxyGenTmgListenerState_Object = MibScalar
ratsProxyGenTmgListenerState = _RatsProxyGenTmgListenerState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 15, 1, 3),
    _RatsProxyGenTmgListenerState_Type()
)
ratsProxyGenTmgListenerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsProxyGenTmgListenerState.setStatus("current")


class _RatsProxyGenTmgSocketAddress_Type(DisplayString):
    """Custom type ratsProxyGenTmgSocketAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RatsProxyGenTmgSocketAddress_Type.__name__ = "DisplayString"
_RatsProxyGenTmgSocketAddress_Object = MibScalar
ratsProxyGenTmgSocketAddress = _RatsProxyGenTmgSocketAddress_Object(
    (1, 3, 6, 1, 4, 1, 40822, 15, 1, 4),
    _RatsProxyGenTmgSocketAddress_Type()
)
ratsProxyGenTmgSocketAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsProxyGenTmgSocketAddress.setStatus("current")
_RatsProxyGenTmgSocketState_Type = Integer32
_RatsProxyGenTmgSocketState_Object = MibScalar
ratsProxyGenTmgSocketState = _RatsProxyGenTmgSocketState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 15, 1, 5),
    _RatsProxyGenTmgSocketState_Type()
)
ratsProxyGenTmgSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsProxyGenTmgSocketState.setStatus("current")
_RatsProxyGenStatusConfig_Type = Integer32
_RatsProxyGenStatusConfig_Object = MibScalar
ratsProxyGenStatusConfig = _RatsProxyGenStatusConfig_Object(
    (1, 3, 6, 1, 4, 1, 40822, 15, 1, 6),
    _RatsProxyGenStatusConfig_Type()
)
ratsProxyGenStatusConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsProxyGenStatusConfig.setStatus("current")
_RatsProxyGenStatusGroupsCount_Type = Integer32
_RatsProxyGenStatusGroupsCount_Object = MibScalar
ratsProxyGenStatusGroupsCount = _RatsProxyGenStatusGroupsCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 15, 1, 7),
    _RatsProxyGenStatusGroupsCount_Type()
)
ratsProxyGenStatusGroupsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsProxyGenStatusGroupsCount.setStatus("current")
_RatsProxyGenStatusMembersCount_Type = Integer32
_RatsProxyGenStatusMembersCount_Object = MibScalar
ratsProxyGenStatusMembersCount = _RatsProxyGenStatusMembersCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 15, 1, 8),
    _RatsProxyGenStatusMembersCount_Type()
)
ratsProxyGenStatusMembersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratsProxyGenStatusMembersCount.setStatus("current")
_MaintenanceSrv_ObjectIdentity = ObjectIdentity
maintenanceSrv = _MaintenanceSrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 16)
)
if mibBuilder.loadTexts:
    maintenanceSrv.setStatus("current")
_MaintenanceSrvGeneral_ObjectIdentity = ObjectIdentity
maintenanceSrvGeneral = _MaintenanceSrvGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 16, 1)
)
if mibBuilder.loadTexts:
    maintenanceSrvGeneral.setStatus("current")


class _MaintenanceSrvGenVersion_Type(DisplayString):
    """Custom type maintenanceSrvGenVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MaintenanceSrvGenVersion_Type.__name__ = "DisplayString"
_MaintenanceSrvGenVersion_Object = MibScalar
maintenanceSrvGenVersion = _MaintenanceSrvGenVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 16, 1, 1),
    _MaintenanceSrvGenVersion_Type()
)
maintenanceSrvGenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenanceSrvGenVersion.setStatus("current")
_MaintenanceSrvGenInterval_Type = Integer32
_MaintenanceSrvGenInterval_Object = MibScalar
maintenanceSrvGenInterval = _MaintenanceSrvGenInterval_Object(
    (1, 3, 6, 1, 4, 1, 40822, 16, 1, 2),
    _MaintenanceSrvGenInterval_Type()
)
maintenanceSrvGenInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenanceSrvGenInterval.setStatus("current")
_MaintenanceSrvGenLowDiskSpace_Type = Integer32
_MaintenanceSrvGenLowDiskSpace_Object = MibScalar
maintenanceSrvGenLowDiskSpace = _MaintenanceSrvGenLowDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 40822, 16, 1, 3),
    _MaintenanceSrvGenLowDiskSpace_Type()
)
maintenanceSrvGenLowDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenanceSrvGenLowDiskSpace.setStatus("current")


class _MaintenanceSrvGenRootDir_Type(DisplayString):
    """Custom type maintenanceSrvGenRootDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MaintenanceSrvGenRootDir_Type.__name__ = "DisplayString"
_MaintenanceSrvGenRootDir_Object = MibScalar
maintenanceSrvGenRootDir = _MaintenanceSrvGenRootDir_Object(
    (1, 3, 6, 1, 4, 1, 40822, 16, 1, 4),
    _MaintenanceSrvGenRootDir_Type()
)
maintenanceSrvGenRootDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenanceSrvGenRootDir.setStatus("current")


class _MaintenanceSrvGenFileMask_Type(DisplayString):
    """Custom type maintenanceSrvGenFileMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MaintenanceSrvGenFileMask_Type.__name__ = "DisplayString"
_MaintenanceSrvGenFileMask_Object = MibScalar
maintenanceSrvGenFileMask = _MaintenanceSrvGenFileMask_Object(
    (1, 3, 6, 1, 4, 1, 40822, 16, 1, 5),
    _MaintenanceSrvGenFileMask_Type()
)
maintenanceSrvGenFileMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenanceSrvGenFileMask.setStatus("current")


class _MaintenanceSrvGenExcludeMask_Type(DisplayString):
    """Custom type maintenanceSrvGenExcludeMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MaintenanceSrvGenExcludeMask_Type.__name__ = "DisplayString"
_MaintenanceSrvGenExcludeMask_Object = MibScalar
maintenanceSrvGenExcludeMask = _MaintenanceSrvGenExcludeMask_Object(
    (1, 3, 6, 1, 4, 1, 40822, 16, 1, 6),
    _MaintenanceSrvGenExcludeMask_Type()
)
maintenanceSrvGenExcludeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenanceSrvGenExcludeMask.setStatus("current")
_MaintenanceSrvGenValidDays_Type = Integer32
_MaintenanceSrvGenValidDays_Object = MibScalar
maintenanceSrvGenValidDays = _MaintenanceSrvGenValidDays_Object(
    (1, 3, 6, 1, 4, 1, 40822, 16, 1, 7),
    _MaintenanceSrvGenValidDays_Type()
)
maintenanceSrvGenValidDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenanceSrvGenValidDays.setStatus("current")
_MaintenanceSrvGenValidMins_Type = Integer32
_MaintenanceSrvGenValidMins_Object = MibScalar
maintenanceSrvGenValidMins = _MaintenanceSrvGenValidMins_Object(
    (1, 3, 6, 1, 4, 1, 40822, 16, 1, 8),
    _MaintenanceSrvGenValidMins_Type()
)
maintenanceSrvGenValidMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenanceSrvGenValidMins.setStatus("current")
_MaintenanceSrvGenDoLog_Type = Integer32
_MaintenanceSrvGenDoLog_Object = MibScalar
maintenanceSrvGenDoLog = _MaintenanceSrvGenDoLog_Object(
    (1, 3, 6, 1, 4, 1, 40822, 16, 1, 9),
    _MaintenanceSrvGenDoLog_Type()
)
maintenanceSrvGenDoLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenanceSrvGenDoLog.setStatus("current")


class _MaintenanceSrvGenCheckAtTime_Type(DisplayString):
    """Custom type maintenanceSrvGenCheckAtTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MaintenanceSrvGenCheckAtTime_Type.__name__ = "DisplayString"
_MaintenanceSrvGenCheckAtTime_Object = MibScalar
maintenanceSrvGenCheckAtTime = _MaintenanceSrvGenCheckAtTime_Object(
    (1, 3, 6, 1, 4, 1, 40822, 16, 1, 10),
    _MaintenanceSrvGenCheckAtTime_Type()
)
maintenanceSrvGenCheckAtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenanceSrvGenCheckAtTime.setStatus("current")
_MaintenanceSrvGenZipEnabled_Type = Integer32
_MaintenanceSrvGenZipEnabled_Object = MibScalar
maintenanceSrvGenZipEnabled = _MaintenanceSrvGenZipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 40822, 16, 1, 11),
    _MaintenanceSrvGenZipEnabled_Type()
)
maintenanceSrvGenZipEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenanceSrvGenZipEnabled.setStatus("current")


class _MaintenanceSrvGenZipDestDir_Type(DisplayString):
    """Custom type maintenanceSrvGenZipDestDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MaintenanceSrvGenZipDestDir_Type.__name__ = "DisplayString"
_MaintenanceSrvGenZipDestDir_Object = MibScalar
maintenanceSrvGenZipDestDir = _MaintenanceSrvGenZipDestDir_Object(
    (1, 3, 6, 1, 4, 1, 40822, 16, 1, 12),
    _MaintenanceSrvGenZipDestDir_Type()
)
maintenanceSrvGenZipDestDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenanceSrvGenZipDestDir.setStatus("current")
_MaintenanceSrvGenZipValidDays_Type = Integer32
_MaintenanceSrvGenZipValidDays_Object = MibScalar
maintenanceSrvGenZipValidDays = _MaintenanceSrvGenZipValidDays_Object(
    (1, 3, 6, 1, 4, 1, 40822, 16, 1, 13),
    _MaintenanceSrvGenZipValidDays_Type()
)
maintenanceSrvGenZipValidDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenanceSrvGenZipValidDays.setStatus("current")
_DfPhonebook_ObjectIdentity = ObjectIdentity
dfPhonebook = _DfPhonebook_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 17)
)
if mibBuilder.loadTexts:
    dfPhonebook.setStatus("current")
_DfPhonebookGeneral_ObjectIdentity = ObjectIdentity
dfPhonebookGeneral = _DfPhonebookGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 17, 1)
)
if mibBuilder.loadTexts:
    dfPhonebookGeneral.setStatus("current")


class _DfPhonebookGenVersion_Type(DisplayString):
    """Custom type dfPhonebookGenVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DfPhonebookGenVersion_Type.__name__ = "DisplayString"
_DfPhonebookGenVersion_Object = MibScalar
dfPhonebookGenVersion = _DfPhonebookGenVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 17, 1, 1),
    _DfPhonebookGenVersion_Type()
)
dfPhonebookGenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPhonebookGenVersion.setStatus("current")


class _DfPhonebookGenDBHost_Type(DisplayString):
    """Custom type dfPhonebookGenDBHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DfPhonebookGenDBHost_Type.__name__ = "DisplayString"
_DfPhonebookGenDBHost_Object = MibScalar
dfPhonebookGenDBHost = _DfPhonebookGenDBHost_Object(
    (1, 3, 6, 1, 4, 1, 40822, 17, 1, 2),
    _DfPhonebookGenDBHost_Type()
)
dfPhonebookGenDBHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPhonebookGenDBHost.setStatus("current")


class _DfPhonebookGenDBName_Type(DisplayString):
    """Custom type dfPhonebookGenDBName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DfPhonebookGenDBName_Type.__name__ = "DisplayString"
_DfPhonebookGenDBName_Object = MibScalar
dfPhonebookGenDBName = _DfPhonebookGenDBName_Object(
    (1, 3, 6, 1, 4, 1, 40822, 17, 1, 3),
    _DfPhonebookGenDBName_Type()
)
dfPhonebookGenDBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPhonebookGenDBName.setStatus("current")


class _DfPhonebookGenDBTable_Type(DisplayString):
    """Custom type dfPhonebookGenDBTable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DfPhonebookGenDBTable_Type.__name__ = "DisplayString"
_DfPhonebookGenDBTable_Object = MibScalar
dfPhonebookGenDBTable = _DfPhonebookGenDBTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 17, 1, 4),
    _DfPhonebookGenDBTable_Type()
)
dfPhonebookGenDBTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPhonebookGenDBTable.setStatus("current")
_DfPhonebookGenDBConnectionState_Type = TConnectionState
_DfPhonebookGenDBConnectionState_Object = MibScalar
dfPhonebookGenDBConnectionState = _DfPhonebookGenDBConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 17, 1, 5),
    _DfPhonebookGenDBConnectionState_Type()
)
dfPhonebookGenDBConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPhonebookGenDBConnectionState.setStatus("current")


class _DfPhonebookGenDBConnectionStateReason_Type(DisplayString):
    """Custom type dfPhonebookGenDBConnectionStateReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DfPhonebookGenDBConnectionStateReason_Type.__name__ = "DisplayString"
_DfPhonebookGenDBConnectionStateReason_Object = MibScalar
dfPhonebookGenDBConnectionStateReason = _DfPhonebookGenDBConnectionStateReason_Object(
    (1, 3, 6, 1, 4, 1, 40822, 17, 1, 6),
    _DfPhonebookGenDBConnectionStateReason_Type()
)
dfPhonebookGenDBConnectionStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPhonebookGenDBConnectionStateReason.setStatus("current")


class _DfPhonebookGenWSUri_Type(DisplayString):
    """Custom type dfPhonebookGenWSUri based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DfPhonebookGenWSUri_Type.__name__ = "DisplayString"
_DfPhonebookGenWSUri_Object = MibScalar
dfPhonebookGenWSUri = _DfPhonebookGenWSUri_Object(
    (1, 3, 6, 1, 4, 1, 40822, 17, 1, 7),
    _DfPhonebookGenWSUri_Type()
)
dfPhonebookGenWSUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPhonebookGenWSUri.setStatus("current")


class _DfPhonebookGenWSUser_Type(DisplayString):
    """Custom type dfPhonebookGenWSUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DfPhonebookGenWSUser_Type.__name__ = "DisplayString"
_DfPhonebookGenWSUser_Object = MibScalar
dfPhonebookGenWSUser = _DfPhonebookGenWSUser_Object(
    (1, 3, 6, 1, 4, 1, 40822, 17, 1, 8),
    _DfPhonebookGenWSUser_Type()
)
dfPhonebookGenWSUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPhonebookGenWSUser.setStatus("current")
_DfPhonebookGenWSConnectionState_Type = TConnectionState
_DfPhonebookGenWSConnectionState_Object = MibScalar
dfPhonebookGenWSConnectionState = _DfPhonebookGenWSConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 17, 1, 9),
    _DfPhonebookGenWSConnectionState_Type()
)
dfPhonebookGenWSConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPhonebookGenWSConnectionState.setStatus("current")


class _DfPhonebookGenWSConnectionStateReason_Type(DisplayString):
    """Custom type dfPhonebookGenWSConnectionStateReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DfPhonebookGenWSConnectionStateReason_Type.__name__ = "DisplayString"
_DfPhonebookGenWSConnectionStateReason_Object = MibScalar
dfPhonebookGenWSConnectionStateReason = _DfPhonebookGenWSConnectionStateReason_Object(
    (1, 3, 6, 1, 4, 1, 40822, 17, 1, 10),
    _DfPhonebookGenWSConnectionStateReason_Type()
)
dfPhonebookGenWSConnectionStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPhonebookGenWSConnectionStateReason.setStatus("current")


class _DfPhonebookGenXMLTetra_Type(DisplayString):
    """Custom type dfPhonebookGenXMLTetra based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DfPhonebookGenXMLTetra_Type.__name__ = "DisplayString"
_DfPhonebookGenXMLTetra_Object = MibScalar
dfPhonebookGenXMLTetra = _DfPhonebookGenXMLTetra_Object(
    (1, 3, 6, 1, 4, 1, 40822, 17, 1, 11),
    _DfPhonebookGenXMLTetra_Type()
)
dfPhonebookGenXMLTetra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPhonebookGenXMLTetra.setStatus("current")


class _DfPhonebookGenXMLTetraGroup_Type(DisplayString):
    """Custom type dfPhonebookGenXMLTetraGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DfPhonebookGenXMLTetraGroup_Type.__name__ = "DisplayString"
_DfPhonebookGenXMLTetraGroup_Object = MibScalar
dfPhonebookGenXMLTetraGroup = _DfPhonebookGenXMLTetraGroup_Object(
    (1, 3, 6, 1, 4, 1, 40822, 17, 1, 12),
    _DfPhonebookGenXMLTetraGroup_Type()
)
dfPhonebookGenXMLTetraGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPhonebookGenXMLTetraGroup.setStatus("current")


class _DfPhonebookGenXMLInfo_Type(DisplayString):
    """Custom type dfPhonebookGenXMLInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DfPhonebookGenXMLInfo_Type.__name__ = "DisplayString"
_DfPhonebookGenXMLInfo_Object = MibScalar
dfPhonebookGenXMLInfo = _DfPhonebookGenXMLInfo_Object(
    (1, 3, 6, 1, 4, 1, 40822, 17, 1, 13),
    _DfPhonebookGenXMLInfo_Type()
)
dfPhonebookGenXMLInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPhonebookGenXMLInfo.setStatus("current")


class _DfPhonebookGenFolderDF_Type(SnmpAdminString):
    """Custom type dfPhonebookGenFolderDF based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DfPhonebookGenFolderDF_Type.__name__ = "SnmpAdminString"
_DfPhonebookGenFolderDF_Object = MibScalar
dfPhonebookGenFolderDF = _DfPhonebookGenFolderDF_Object(
    (1, 3, 6, 1, 4, 1, 40822, 17, 1, 14),
    _DfPhonebookGenFolderDF_Type()
)
dfPhonebookGenFolderDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPhonebookGenFolderDF.setStatus("current")


class _DfPhonebookGenFolderWeb_Type(SnmpAdminString):
    """Custom type dfPhonebookGenFolderWeb based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DfPhonebookGenFolderWeb_Type.__name__ = "SnmpAdminString"
_DfPhonebookGenFolderWeb_Object = MibScalar
dfPhonebookGenFolderWeb = _DfPhonebookGenFolderWeb_Object(
    (1, 3, 6, 1, 4, 1, 40822, 17, 1, 15),
    _DfPhonebookGenFolderWeb_Type()
)
dfPhonebookGenFolderWeb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPhonebookGenFolderWeb.setStatus("current")
_SipRecGateway_ObjectIdentity = ObjectIdentity
sipRecGateway = _SipRecGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 18)
)
if mibBuilder.loadTexts:
    sipRecGateway.setStatus("current")
_SipRecGatewayGeneral_ObjectIdentity = ObjectIdentity
sipRecGatewayGeneral = _SipRecGatewayGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 18, 1)
)
if mibBuilder.loadTexts:
    sipRecGatewayGeneral.setStatus("current")


class _SipRecGatewayGenVersion_Type(DisplayString):
    """Custom type sipRecGatewayGenVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipRecGatewayGenVersion_Type.__name__ = "DisplayString"
_SipRecGatewayGenVersion_Object = MibScalar
sipRecGatewayGenVersion = _SipRecGatewayGenVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 1, 1),
    _SipRecGatewayGenVersion_Type()
)
sipRecGatewayGenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRecGatewayGenVersion.setStatus("current")


class _SipRecGatewayGenSipIdentity_Type(DisplayString):
    """Custom type sipRecGatewayGenSipIdentity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipRecGatewayGenSipIdentity_Type.__name__ = "DisplayString"
_SipRecGatewayGenSipIdentity_Object = MibScalar
sipRecGatewayGenSipIdentity = _SipRecGatewayGenSipIdentity_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 1, 2),
    _SipRecGatewayGenSipIdentity_Type()
)
sipRecGatewayGenSipIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRecGatewayGenSipIdentity.setStatus("current")


class _SipRecGatewayGenSipLocalIp_Type(DisplayString):
    """Custom type sipRecGatewayGenSipLocalIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipRecGatewayGenSipLocalIp_Type.__name__ = "DisplayString"
_SipRecGatewayGenSipLocalIp_Object = MibScalar
sipRecGatewayGenSipLocalIp = _SipRecGatewayGenSipLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 1, 3),
    _SipRecGatewayGenSipLocalIp_Type()
)
sipRecGatewayGenSipLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRecGatewayGenSipLocalIp.setStatus("current")
_SipRecGatewayGenSipLocalPort_Type = Integer32
_SipRecGatewayGenSipLocalPort_Object = MibScalar
sipRecGatewayGenSipLocalPort = _SipRecGatewayGenSipLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 1, 4),
    _SipRecGatewayGenSipLocalPort_Type()
)
sipRecGatewayGenSipLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRecGatewayGenSipLocalPort.setStatus("current")
_SipRecGatewayGenSipTransTimeout_Type = Integer32
_SipRecGatewayGenSipTransTimeout_Object = MibScalar
sipRecGatewayGenSipTransTimeout = _SipRecGatewayGenSipTransTimeout_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 1, 5),
    _SipRecGatewayGenSipTransTimeout_Type()
)
sipRecGatewayGenSipTransTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRecGatewayGenSipTransTimeout.setStatus("current")
_SipRecGatewayGenSipTransRetryCount_Type = Integer32
_SipRecGatewayGenSipTransRetryCount_Object = MibScalar
sipRecGatewayGenSipTransRetryCount = _SipRecGatewayGenSipTransRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 1, 6),
    _SipRecGatewayGenSipTransRetryCount_Type()
)
sipRecGatewayGenSipTransRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRecGatewayGenSipTransRetryCount.setStatus("current")
_SipRecGatewayGenSipDialogDestroyTimeout_Type = Integer32
_SipRecGatewayGenSipDialogDestroyTimeout_Object = MibScalar
sipRecGatewayGenSipDialogDestroyTimeout = _SipRecGatewayGenSipDialogDestroyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 1, 7),
    _SipRecGatewayGenSipDialogDestroyTimeout_Type()
)
sipRecGatewayGenSipDialogDestroyTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRecGatewayGenSipDialogDestroyTimeout.setStatus("current")


class _SipRecGatewayGenRecIp_Type(DisplayString):
    """Custom type sipRecGatewayGenRecIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipRecGatewayGenRecIp_Type.__name__ = "DisplayString"
_SipRecGatewayGenRecIp_Object = MibScalar
sipRecGatewayGenRecIp = _SipRecGatewayGenRecIp_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 1, 8),
    _SipRecGatewayGenRecIp_Type()
)
sipRecGatewayGenRecIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRecGatewayGenRecIp.setStatus("current")
_SipRecGatewayGenRecPort_Type = Integer32
_SipRecGatewayGenRecPort_Object = MibScalar
sipRecGatewayGenRecPort = _SipRecGatewayGenRecPort_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 1, 9),
    _SipRecGatewayGenRecPort_Type()
)
sipRecGatewayGenRecPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRecGatewayGenRecPort.setStatus("current")
_SipRecGatewayGenRecUseSendBuffer_Type = Integer32
_SipRecGatewayGenRecUseSendBuffer_Object = MibScalar
sipRecGatewayGenRecUseSendBuffer = _SipRecGatewayGenRecUseSendBuffer_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 1, 10),
    _SipRecGatewayGenRecUseSendBuffer_Type()
)
sipRecGatewayGenRecUseSendBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRecGatewayGenRecUseSendBuffer.setStatus("current")
_SipRecGatewayGenDevAutoDiscovery_Type = Integer32
_SipRecGatewayGenDevAutoDiscovery_Object = MibScalar
sipRecGatewayGenDevAutoDiscovery = _SipRecGatewayGenDevAutoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 1, 11),
    _SipRecGatewayGenDevAutoDiscovery_Type()
)
sipRecGatewayGenDevAutoDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRecGatewayGenDevAutoDiscovery.setStatus("current")


class _SipRecGatewayGenDevAcceptedUserAgent_Type(DisplayString):
    """Custom type sipRecGatewayGenDevAcceptedUserAgent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipRecGatewayGenDevAcceptedUserAgent_Type.__name__ = "DisplayString"
_SipRecGatewayGenDevAcceptedUserAgent_Object = MibScalar
sipRecGatewayGenDevAcceptedUserAgent = _SipRecGatewayGenDevAcceptedUserAgent_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 1, 12),
    _SipRecGatewayGenDevAcceptedUserAgent_Type()
)
sipRecGatewayGenDevAcceptedUserAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRecGatewayGenDevAcceptedUserAgent.setStatus("current")


class _SipRecGatewayGenDevBroadcastIp_Type(DisplayString):
    """Custom type sipRecGatewayGenDevBroadcastIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipRecGatewayGenDevBroadcastIp_Type.__name__ = "DisplayString"
_SipRecGatewayGenDevBroadcastIp_Object = MibScalar
sipRecGatewayGenDevBroadcastIp = _SipRecGatewayGenDevBroadcastIp_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 1, 13),
    _SipRecGatewayGenDevBroadcastIp_Type()
)
sipRecGatewayGenDevBroadcastIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRecGatewayGenDevBroadcastIp.setStatus("current")
_SipRecGatewayGenDevBroadcastPort_Type = Integer32
_SipRecGatewayGenDevBroadcastPort_Object = MibScalar
sipRecGatewayGenDevBroadcastPort = _SipRecGatewayGenDevBroadcastPort_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 1, 14),
    _SipRecGatewayGenDevBroadcastPort_Type()
)
sipRecGatewayGenDevBroadcastPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRecGatewayGenDevBroadcastPort.setStatus("current")
_SipRecGatewayGenDevRecIndCall_Type = Integer32
_SipRecGatewayGenDevRecIndCall_Object = MibScalar
sipRecGatewayGenDevRecIndCall = _SipRecGatewayGenDevRecIndCall_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 1, 15),
    _SipRecGatewayGenDevRecIndCall_Type()
)
sipRecGatewayGenDevRecIndCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRecGatewayGenDevRecIndCall.setStatus("current")
_SipRecGatewayDev_ObjectIdentity = ObjectIdentity
sipRecGatewayDev = _SipRecGatewayDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 18, 2)
)
if mibBuilder.loadTexts:
    sipRecGatewayDev.setStatus("current")
_SipRecGatewayDevTable_Object = MibTable
sipRecGatewayDevTable = _SipRecGatewayDevTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 2, 1)
)
if mibBuilder.loadTexts:
    sipRecGatewayDevTable.setStatus("current")
_SipRecGatewayTableEntry_Object = MibTableRow
sipRecGatewayTableEntry = _SipRecGatewayTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 2, 1, 1)
)
sipRecGatewayTableEntry.setIndexNames(
    (0, "Hagedorn-MIB", "sipRecGatewayTableIdx"),
)
if mibBuilder.loadTexts:
    sipRecGatewayTableEntry.setStatus("current")


class _SipRecGatewayTableIdx_Type(Integer32):
    """Custom type sipRecGatewayTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SipRecGatewayTableIdx_Type.__name__ = "Integer32"
_SipRecGatewayTableIdx_Object = MibTableColumn
sipRecGatewayTableIdx = _SipRecGatewayTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 2, 1, 1, 1),
    _SipRecGatewayTableIdx_Type()
)
sipRecGatewayTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipRecGatewayTableIdx.setStatus("current")
_SipRecGatewayTableRowStatus_Type = RowStatus
_SipRecGatewayTableRowStatus_Object = MibTableColumn
sipRecGatewayTableRowStatus = _SipRecGatewayTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 2, 1, 1, 2),
    _SipRecGatewayTableRowStatus_Type()
)
sipRecGatewayTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipRecGatewayTableRowStatus.setStatus("current")


class _SipRecGatewayTableDescription_Type(DisplayString):
    """Custom type sipRecGatewayTableDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipRecGatewayTableDescription_Type.__name__ = "DisplayString"
_SipRecGatewayTableDescription_Object = MibTableColumn
sipRecGatewayTableDescription = _SipRecGatewayTableDescription_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 2, 1, 1, 3),
    _SipRecGatewayTableDescription_Type()
)
sipRecGatewayTableDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRecGatewayTableDescription.setStatus("current")
_SipRecGatewayTableType_Type = Integer32
_SipRecGatewayTableType_Object = MibTableColumn
sipRecGatewayTableType = _SipRecGatewayTableType_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 2, 1, 1, 4),
    _SipRecGatewayTableType_Type()
)
sipRecGatewayTableType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRecGatewayTableType.setStatus("current")


class _SipRecGatewayTableRemoteIP_Type(DisplayString):
    """Custom type sipRecGatewayTableRemoteIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipRecGatewayTableRemoteIP_Type.__name__ = "DisplayString"
_SipRecGatewayTableRemoteIP_Object = MibTableColumn
sipRecGatewayTableRemoteIP = _SipRecGatewayTableRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 2, 1, 1, 5),
    _SipRecGatewayTableRemoteIP_Type()
)
sipRecGatewayTableRemoteIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRecGatewayTableRemoteIP.setStatus("current")
_SipRecGatewayTableRemotePort_Type = Integer32
_SipRecGatewayTableRemotePort_Object = MibTableColumn
sipRecGatewayTableRemotePort = _SipRecGatewayTableRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 2, 1, 1, 6),
    _SipRecGatewayTableRemotePort_Type()
)
sipRecGatewayTableRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRecGatewayTableRemotePort.setStatus("current")


class _SipRecGatewayTableMulticastIP_Type(DisplayString):
    """Custom type sipRecGatewayTableMulticastIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipRecGatewayTableMulticastIP_Type.__name__ = "DisplayString"
_SipRecGatewayTableMulticastIP_Object = MibTableColumn
sipRecGatewayTableMulticastIP = _SipRecGatewayTableMulticastIP_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 2, 1, 1, 7),
    _SipRecGatewayTableMulticastIP_Type()
)
sipRecGatewayTableMulticastIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRecGatewayTableMulticastIP.setStatus("current")
_SipRecGatewayTableMulticastPort_Type = Integer32
_SipRecGatewayTableMulticastPort_Object = MibTableColumn
sipRecGatewayTableMulticastPort = _SipRecGatewayTableMulticastPort_Object(
    (1, 3, 6, 1, 4, 1, 40822, 18, 2, 1, 1, 8),
    _SipRecGatewayTableMulticastPort_Type()
)
sipRecGatewayTableMulticastPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRecGatewayTableMulticastPort.setStatus("current")
_IpRadioPhone_ObjectIdentity = ObjectIdentity
ipRadioPhone = _IpRadioPhone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 19)
)
if mibBuilder.loadTexts:
    ipRadioPhone.setStatus("current")
_IprpGeneral_ObjectIdentity = ObjectIdentity
iprpGeneral = _IprpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 19, 1)
)
if mibBuilder.loadTexts:
    iprpGeneral.setStatus("current")


class _IprpGenSwVersion_Type(DisplayString):
    """Custom type iprpGenSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprpGenSwVersion_Type.__name__ = "DisplayString"
_IprpGenSwVersion_Object = MibScalar
iprpGenSwVersion = _IprpGenSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 1, 1),
    _IprpGenSwVersion_Type()
)
iprpGenSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprpGenSwVersion.setStatus("current")


class _IprpGenHwFwVersion_Type(DisplayString):
    """Custom type iprpGenHwFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprpGenHwFwVersion_Type.__name__ = "DisplayString"
_IprpGenHwFwVersion_Object = MibScalar
iprpGenHwFwVersion = _IprpGenHwFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 1, 2),
    _IprpGenHwFwVersion_Type()
)
iprpGenHwFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprpGenHwFwVersion.setStatus("current")


class _IprpGenAudioFwVersion_Type(DisplayString):
    """Custom type iprpGenAudioFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprpGenAudioFwVersion_Type.__name__ = "DisplayString"
_IprpGenAudioFwVersion_Object = MibScalar
iprpGenAudioFwVersion = _IprpGenAudioFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 1, 3),
    _IprpGenAudioFwVersion_Type()
)
iprpGenAudioFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprpGenAudioFwVersion.setStatus("current")


class _IprpGenSwBundleVersion_Type(DisplayString):
    """Custom type iprpGenSwBundleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprpGenSwBundleVersion_Type.__name__ = "DisplayString"
_IprpGenSwBundleVersion_Object = MibScalar
iprpGenSwBundleVersion = _IprpGenSwBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 1, 4),
    _IprpGenSwBundleVersion_Type()
)
iprpGenSwBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprpGenSwBundleVersion.setStatus("current")


class _IprpGenSerialNr_Type(DisplayString):
    """Custom type iprpGenSerialNr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprpGenSerialNr_Type.__name__ = "DisplayString"
_IprpGenSerialNr_Object = MibScalar
iprpGenSerialNr = _IprpGenSerialNr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 1, 5),
    _IprpGenSerialNr_Type()
)
iprpGenSerialNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprpGenSerialNr.setStatus("current")


class _IprpGenOsScriptsVersion_Type(DisplayString):
    """Custom type iprpGenOsScriptsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprpGenOsScriptsVersion_Type.__name__ = "DisplayString"
_IprpGenOsScriptsVersion_Object = MibScalar
iprpGenOsScriptsVersion = _IprpGenOsScriptsVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 1, 6),
    _IprpGenOsScriptsVersion_Type()
)
iprpGenOsScriptsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprpGenOsScriptsVersion.setStatus("current")
_IprpWorkplace_ObjectIdentity = ObjectIdentity
iprpWorkplace = _IprpWorkplace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 19, 2)
)
if mibBuilder.loadTexts:
    iprpWorkplace.setStatus("current")


class _IprpWorkplaceName_Type(DisplayString):
    """Custom type iprpWorkplaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprpWorkplaceName_Type.__name__ = "DisplayString"
_IprpWorkplaceName_Object = MibScalar
iprpWorkplaceName = _IprpWorkplaceName_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 2, 1),
    _IprpWorkplaceName_Type()
)
iprpWorkplaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprpWorkplaceName.setStatus("current")


class _IprpWorkplaceOpta_Type(DisplayString):
    """Custom type iprpWorkplaceOpta based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprpWorkplaceOpta_Type.__name__ = "DisplayString"
_IprpWorkplaceOpta_Object = MibScalar
iprpWorkplaceOpta = _IprpWorkplaceOpta_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 2, 2),
    _IprpWorkplaceOpta_Type()
)
iprpWorkplaceOpta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprpWorkplaceOpta.setStatus("current")
_IprpChannels_ObjectIdentity = ObjectIdentity
iprpChannels = _IprpChannels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 19, 3)
)
if mibBuilder.loadTexts:
    iprpChannels.setStatus("current")
_IprpChannelsTable_Object = MibTable
iprpChannelsTable = _IprpChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 3, 1)
)
if mibBuilder.loadTexts:
    iprpChannelsTable.setStatus("current")
_IprpChannelsTableEntry_Object = MibTableRow
iprpChannelsTableEntry = _IprpChannelsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 3, 1, 1)
)
iprpChannelsTableEntry.setIndexNames(
    (0, "Hagedorn-MIB", "iprpChannelsTableIdx"),
)
if mibBuilder.loadTexts:
    iprpChannelsTableEntry.setStatus("current")


class _IprpChannelsTableIdx_Type(Integer32):
    """Custom type iprpChannelsTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IprpChannelsTableIdx_Type.__name__ = "Integer32"
_IprpChannelsTableIdx_Object = MibTableColumn
iprpChannelsTableIdx = _IprpChannelsTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 3, 1, 1, 1),
    _IprpChannelsTableIdx_Type()
)
iprpChannelsTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iprpChannelsTableIdx.setStatus("current")
_IprpChannelsTableRowStatus_Type = RowStatus
_IprpChannelsTableRowStatus_Object = MibTableColumn
iprpChannelsTableRowStatus = _IprpChannelsTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 3, 1, 1, 2),
    _IprpChannelsTableRowStatus_Type()
)
iprpChannelsTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iprpChannelsTableRowStatus.setStatus("current")


class _IprpChannelsTableID_Type(DisplayString):
    """Custom type iprpChannelsTableID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprpChannelsTableID_Type.__name__ = "DisplayString"
_IprpChannelsTableID_Object = MibTableColumn
iprpChannelsTableID = _IprpChannelsTableID_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 3, 1, 1, 3),
    _IprpChannelsTableID_Type()
)
iprpChannelsTableID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprpChannelsTableID.setStatus("current")
_IprpChannelsTableRegistered_Type = Integer32
_IprpChannelsTableRegistered_Object = MibTableColumn
iprpChannelsTableRegistered = _IprpChannelsTableRegistered_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 3, 1, 1, 4),
    _IprpChannelsTableRegistered_Type()
)
iprpChannelsTableRegistered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprpChannelsTableRegistered.setStatus("current")
_IprpChannelsTableState_Type = ChannelState
_IprpChannelsTableState_Object = MibTableColumn
iprpChannelsTableState = _IprpChannelsTableState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 3, 1, 1, 5),
    _IprpChannelsTableState_Type()
)
iprpChannelsTableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprpChannelsTableState.setStatus("current")


class _IprpChannelsTableISSI_Type(DisplayString):
    """Custom type iprpChannelsTableISSI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprpChannelsTableISSI_Type.__name__ = "DisplayString"
_IprpChannelsTableISSI_Object = MibTableColumn
iprpChannelsTableISSI = _IprpChannelsTableISSI_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 3, 1, 1, 6),
    _IprpChannelsTableISSI_Type()
)
iprpChannelsTableISSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprpChannelsTableISSI.setStatus("current")


class _IprpChannelsTableGSSI_Type(DisplayString):
    """Custom type iprpChannelsTableGSSI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprpChannelsTableGSSI_Type.__name__ = "DisplayString"
_IprpChannelsTableGSSI_Object = MibTableColumn
iprpChannelsTableGSSI = _IprpChannelsTableGSSI_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 3, 1, 1, 7),
    _IprpChannelsTableGSSI_Type()
)
iprpChannelsTableGSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprpChannelsTableGSSI.setStatus("current")
_IprpChannelsTableDevice_Type = ChannelDevice
_IprpChannelsTableDevice_Object = MibTableColumn
iprpChannelsTableDevice = _IprpChannelsTableDevice_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 3, 1, 1, 8),
    _IprpChannelsTableDevice_Type()
)
iprpChannelsTableDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprpChannelsTableDevice.setStatus("current")
_IprpChannelsTableCommType_Type = ChannelCommType
_IprpChannelsTableCommType_Object = MibTableColumn
iprpChannelsTableCommType = _IprpChannelsTableCommType_Object(
    (1, 3, 6, 1, 4, 1, 40822, 19, 3, 1, 1, 9),
    _IprpChannelsTableCommType_Type()
)
iprpChannelsTableCommType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprpChannelsTableCommType.setStatus("current")
_TttGateway_ObjectIdentity = ObjectIdentity
tttGateway = _TttGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 20)
)
if mibBuilder.loadTexts:
    tttGateway.setStatus("current")
_TttGatewayStates_ObjectIdentity = ObjectIdentity
tttGatewayStates = _TttGatewayStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 20, 1)
)
if mibBuilder.loadTexts:
    tttGatewayStates.setStatus("current")
_TttGatewayStatesTable_Object = MibTable
tttGatewayStatesTable = _TttGatewayStatesTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 20, 1, 1)
)
if mibBuilder.loadTexts:
    tttGatewayStatesTable.setStatus("current")
_TttGatewayStatesTableEntry_Object = MibTableRow
tttGatewayStatesTableEntry = _TttGatewayStatesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 20, 1, 1, 1)
)
tttGatewayStatesTableEntry.setIndexNames(
    (0, "Hagedorn-MIB", "tttGatewayStatesTableIdx"),
)
if mibBuilder.loadTexts:
    tttGatewayStatesTableEntry.setStatus("current")


class _TttGatewayStatesTableIdx_Type(Integer32):
    """Custom type tttGatewayStatesTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TttGatewayStatesTableIdx_Type.__name__ = "Integer32"
_TttGatewayStatesTableIdx_Object = MibTableColumn
tttGatewayStatesTableIdx = _TttGatewayStatesTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 20, 1, 1, 1, 1),
    _TttGatewayStatesTableIdx_Type()
)
tttGatewayStatesTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tttGatewayStatesTableIdx.setStatus("current")
_TttGatewayStatesTableRowStatus_Type = RowStatus
_TttGatewayStatesTableRowStatus_Object = MibTableColumn
tttGatewayStatesTableRowStatus = _TttGatewayStatesTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 20, 1, 1, 1, 2),
    _TttGatewayStatesTableRowStatus_Type()
)
tttGatewayStatesTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tttGatewayStatesTableRowStatus.setStatus("current")


class _TttGatewayStatesTableVersion_Type(DisplayString):
    """Custom type tttGatewayStatesTableVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TttGatewayStatesTableVersion_Type.__name__ = "DisplayString"
_TttGatewayStatesTableVersion_Object = MibTableColumn
tttGatewayStatesTableVersion = _TttGatewayStatesTableVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 20, 1, 1, 1, 3),
    _TttGatewayStatesTableVersion_Type()
)
tttGatewayStatesTableVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tttGatewayStatesTableVersion.setStatus("current")


class _TttGatewayStatesTableTimeStamp_Type(DisplayString):
    """Custom type tttGatewayStatesTableTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TttGatewayStatesTableTimeStamp_Type.__name__ = "DisplayString"
_TttGatewayStatesTableTimeStamp_Object = MibTableColumn
tttGatewayStatesTableTimeStamp = _TttGatewayStatesTableTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 40822, 20, 1, 1, 1, 4),
    _TttGatewayStatesTableTimeStamp_Type()
)
tttGatewayStatesTableTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tttGatewayStatesTableTimeStamp.setStatus("current")


class _TttGatewayStatesTableIdent_Type(DisplayString):
    """Custom type tttGatewayStatesTableIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TttGatewayStatesTableIdent_Type.__name__ = "DisplayString"
_TttGatewayStatesTableIdent_Object = MibTableColumn
tttGatewayStatesTableIdent = _TttGatewayStatesTableIdent_Object(
    (1, 3, 6, 1, 4, 1, 40822, 20, 1, 1, 1, 5),
    _TttGatewayStatesTableIdent_Type()
)
tttGatewayStatesTableIdent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tttGatewayStatesTableIdent.setStatus("current")


class _TttGatewayStatesTableDfTimeStamp_Type(DisplayString):
    """Custom type tttGatewayStatesTableDfTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TttGatewayStatesTableDfTimeStamp_Type.__name__ = "DisplayString"
_TttGatewayStatesTableDfTimeStamp_Object = MibTableColumn
tttGatewayStatesTableDfTimeStamp = _TttGatewayStatesTableDfTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 40822, 20, 1, 1, 1, 6),
    _TttGatewayStatesTableDfTimeStamp_Type()
)
tttGatewayStatesTableDfTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tttGatewayStatesTableDfTimeStamp.setStatus("current")
_TttGatewayStatesTableDfState_Type = ComponentState
_TttGatewayStatesTableDfState_Object = MibTableColumn
tttGatewayStatesTableDfState = _TttGatewayStatesTableDfState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 20, 1, 1, 1, 7),
    _TttGatewayStatesTableDfState_Type()
)
tttGatewayStatesTableDfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tttGatewayStatesTableDfState.setStatus("current")


class _TttGatewayStatesTableDfStateReason_Type(DisplayString):
    """Custom type tttGatewayStatesTableDfStateReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TttGatewayStatesTableDfStateReason_Type.__name__ = "DisplayString"
_TttGatewayStatesTableDfStateReason_Object = MibTableColumn
tttGatewayStatesTableDfStateReason = _TttGatewayStatesTableDfStateReason_Object(
    (1, 3, 6, 1, 4, 1, 40822, 20, 1, 1, 1, 8),
    _TttGatewayStatesTableDfStateReason_Type()
)
tttGatewayStatesTableDfStateReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tttGatewayStatesTableDfStateReason.setStatus("current")


class _TttGatewayStatesTableDfGSSI_Type(DisplayString):
    """Custom type tttGatewayStatesTableDfGSSI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TttGatewayStatesTableDfGSSI_Type.__name__ = "DisplayString"
_TttGatewayStatesTableDfGSSI_Object = MibTableColumn
tttGatewayStatesTableDfGSSI = _TttGatewayStatesTableDfGSSI_Object(
    (1, 3, 6, 1, 4, 1, 40822, 20, 1, 1, 1, 9),
    _TttGatewayStatesTableDfGSSI_Type()
)
tttGatewayStatesTableDfGSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tttGatewayStatesTableDfGSSI.setStatus("current")


class _TttGatewayStatesTableIpruTimeStamp_Type(DisplayString):
    """Custom type tttGatewayStatesTableIpruTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TttGatewayStatesTableIpruTimeStamp_Type.__name__ = "DisplayString"
_TttGatewayStatesTableIpruTimeStamp_Object = MibTableColumn
tttGatewayStatesTableIpruTimeStamp = _TttGatewayStatesTableIpruTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 40822, 20, 1, 1, 1, 10),
    _TttGatewayStatesTableIpruTimeStamp_Type()
)
tttGatewayStatesTableIpruTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tttGatewayStatesTableIpruTimeStamp.setStatus("current")
_TttGatewayStatesTableIpruState_Type = ComponentState
_TttGatewayStatesTableIpruState_Object = MibTableColumn
tttGatewayStatesTableIpruState = _TttGatewayStatesTableIpruState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 20, 1, 1, 1, 11),
    _TttGatewayStatesTableIpruState_Type()
)
tttGatewayStatesTableIpruState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tttGatewayStatesTableIpruState.setStatus("current")


class _TttGatewayStatesTableIpruStateReason_Type(DisplayString):
    """Custom type tttGatewayStatesTableIpruStateReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TttGatewayStatesTableIpruStateReason_Type.__name__ = "DisplayString"
_TttGatewayStatesTableIpruStateReason_Object = MibTableColumn
tttGatewayStatesTableIpruStateReason = _TttGatewayStatesTableIpruStateReason_Object(
    (1, 3, 6, 1, 4, 1, 40822, 20, 1, 1, 1, 12),
    _TttGatewayStatesTableIpruStateReason_Type()
)
tttGatewayStatesTableIpruStateReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tttGatewayStatesTableIpruStateReason.setStatus("current")


class _TttGatewayStatesTableIpruGSSI_Type(DisplayString):
    """Custom type tttGatewayStatesTableIpruGSSI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TttGatewayStatesTableIpruGSSI_Type.__name__ = "DisplayString"
_TttGatewayStatesTableIpruGSSI_Object = MibTableColumn
tttGatewayStatesTableIpruGSSI = _TttGatewayStatesTableIpruGSSI_Object(
    (1, 3, 6, 1, 4, 1, 40822, 20, 1, 1, 1, 13),
    _TttGatewayStatesTableIpruGSSI_Type()
)
tttGatewayStatesTableIpruGSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tttGatewayStatesTableIpruGSSI.setStatus("current")

# Managed Objects groups


# Notification objects

tmgSessionsStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 1, 3, 1)
)
tmgSessionsStateTrap.setObjects(
    ("Hagedorn-MIB", "tmgSessionsTableState")
)
if mibBuilder.loadTexts:
    tmgSessionsStateTrap.setStatus(
        "current"
    )

ksGenKryxConnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 2, 2, 1)
)
ksGenKryxConnectedTrap.setObjects(
    ("Hagedorn-MIB", "ksGenKryxConnected")
)
if mibBuilder.loadTexts:
    ksGenKryxConnectedTrap.setStatus(
        "current"
    )

ksGenKryxLastStatusCodeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 2, 2, 2)
)
ksGenKryxLastStatusCodeTrap.setObjects(
    ("Hagedorn-MIB", "ksGenKryxLastStatusCode")
)
if mibBuilder.loadTexts:
    ksGenKryxLastStatusCodeTrap.setStatus(
        "current"
    )

ksGenKryxLastStatusTextTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 2, 2, 3)
)
ksGenKryxLastStatusTextTrap.setObjects(
    ("Hagedorn-MIB", "ksGenKryxLastStatusText")
)
if mibBuilder.loadTexts:
    ksGenKryxLastStatusTextTrap.setStatus(
        "current"
    )

iprtGenUserNameTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 1)
)
iprtGenUserNameTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenUserName")
)
if mibBuilder.loadTexts:
    iprtGenUserNameTrap.setStatus(
        "current"
    )

iprtGenVersionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 2)
)
iprtGenVersionTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenVersion")
)
if mibBuilder.loadTexts:
    iprtGenVersionTrap.setStatus(
        "current"
    )

iprtGenStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 3)
)
iprtGenStateTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenState")
)
if mibBuilder.loadTexts:
    iprtGenStateTrap.setStatus(
        "current"
    )

iprtGenOsUserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 4)
)
iprtGenOsUserTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenOsUser")
)
if mibBuilder.loadTexts:
    iprtGenOsUserTrap.setStatus(
        "current"
    )

iprtGenRoleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 5)
)
iprtGenRoleTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenRole")
)
if mibBuilder.loadTexts:
    iprtGenRoleTrap.setStatus(
        "current"
    )

iprtGenVtlstStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 6)
)
iprtGenVtlstStateTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenVtlstState")
)
if mibBuilder.loadTexts:
    iprtGenVtlstStateTrap.setStatus(
        "current"
    )

iprtGenRecorderStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 7)
)
iprtGenRecorderStateTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenRecorderState")
)
if mibBuilder.loadTexts:
    iprtGenRecorderStateTrap.setStatus(
        "current"
    )

iprtGenAudioBoxDeviceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 8)
)
iprtGenAudioBoxDeviceTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenAudioBoxDevice")
)
if mibBuilder.loadTexts:
    iprtGenAudioBoxDeviceTrap.setStatus(
        "current"
    )

iprtGenAudioBoxExtSpeaker1VolumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 9)
)
iprtGenAudioBoxExtSpeaker1VolumeTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenAudioBoxExtSpeaker1Volume")
)
if mibBuilder.loadTexts:
    iprtGenAudioBoxExtSpeaker1VolumeTrap.setStatus(
        "current"
    )

iprtGenAudioBoxExtSpeaker2VolumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 10)
)
iprtGenAudioBoxExtSpeaker2VolumeTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenAudioBoxExtSpeaker2Volume")
)
if mibBuilder.loadTexts:
    iprtGenAudioBoxExtSpeaker2VolumeTrap.setStatus(
        "current"
    )

iprtGenAudioBoxExtSpeaker3VolumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 11)
)
iprtGenAudioBoxExtSpeaker3VolumeTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenAudioBoxExtSpeaker3Volume")
)
if mibBuilder.loadTexts:
    iprtGenAudioBoxExtSpeaker3VolumeTrap.setStatus(
        "current"
    )

iprtGenAudioBoxExtSpeaker4VolumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 12)
)
iprtGenAudioBoxExtSpeaker4VolumeTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenAudioBoxExtSpeaker4Volume")
)
if mibBuilder.loadTexts:
    iprtGenAudioBoxExtSpeaker4VolumeTrap.setStatus(
        "current"
    )

iprtGenAudioBoxActualSpeakerVolumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 13)
)
iprtGenAudioBoxActualSpeakerVolumeTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenAudioBoxActualSpeakerVolume")
)
if mibBuilder.loadTexts:
    iprtGenAudioBoxActualSpeakerVolumeTrap.setStatus(
        "current"
    )

iprtGenAudioBoxMixedSpeakerVolumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 14)
)
iprtGenAudioBoxMixedSpeakerVolumeTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenAudioBoxMixedSpeakerVolume")
)
if mibBuilder.loadTexts:
    iprtGenAudioBoxMixedSpeakerVolumeTrap.setStatus(
        "current"
    )

iprtGenAudioBoxHeadsetSpeakerVolumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 15)
)
iprtGenAudioBoxHeadsetSpeakerVolumeTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenAudioBoxHeadsetSpeakerVolume")
)
if mibBuilder.loadTexts:
    iprtGenAudioBoxHeadsetSpeakerVolumeTrap.setStatus(
        "current"
    )

iprtGenAudioBoxHandsetSpeakerVolumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 16)
)
iprtGenAudioBoxHandsetSpeakerVolumeTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenAudioBoxHandsetSpeakerVolume")
)
if mibBuilder.loadTexts:
    iprtGenAudioBoxHandsetSpeakerVolumeTrap.setStatus(
        "current"
    )

iprtGenAudioBoxLineOutSpeakerVolumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 17)
)
iprtGenAudioBoxLineOutSpeakerVolumeTrap.setObjects(
    ("Hagedorn-MIB", "iprtGenAudioBoxHandsetSpeakerVolume")
)
if mibBuilder.loadTexts:
    iprtGenAudioBoxLineOutSpeakerVolumeTrap.setStatus(
        "current"
    )

iprtChannelsRegisteredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 4, 1)
)
iprtChannelsRegisteredTrap.setObjects(
    ("Hagedorn-MIB", "iprtChannelsTableRegistered")
)
if mibBuilder.loadTexts:
    iprtChannelsRegisteredTrap.setStatus(
        "current"
    )

iprtChannelsStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 4, 2)
)
iprtChannelsStateTrap.setObjects(
    ("Hagedorn-MIB", "iprtChannelsTableState")
)
if mibBuilder.loadTexts:
    iprtChannelsStateTrap.setStatus(
        "current"
    )

iprtChannelsTableISSITrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 4, 3)
)
iprtChannelsTableISSITrap.setObjects(
    ("Hagedorn-MIB", "iprtChannelsTableISSI")
)
if mibBuilder.loadTexts:
    iprtChannelsTableISSITrap.setStatus(
        "current"
    )

iprtChannelsTableGSSITrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 4, 4)
)
iprtChannelsTableGSSITrap.setObjects(
    ("Hagedorn-MIB", "iprtChannelsTableGSSI")
)
if mibBuilder.loadTexts:
    iprtChannelsTableGSSITrap.setStatus(
        "current"
    )

iprtChannelsTableDeviceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 4, 5)
)
iprtChannelsTableDeviceTrap.setObjects(
    ("Hagedorn-MIB", "iprtChannelsTableDevice")
)
if mibBuilder.loadTexts:
    iprtChannelsTableDeviceTrap.setStatus(
        "current"
    )

iprtChannelsTableCommTypeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 4, 6)
)
iprtChannelsTableCommTypeTrap.setObjects(
    ("Hagedorn-MIB", "iprtChannelsTableCommType")
)
if mibBuilder.loadTexts:
    iprtChannelsTableCommTypeTrap.setStatus(
        "current"
    )

iprtAudioTableSpeakerNameTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 6, 1)
)
iprtAudioTableSpeakerNameTrap.setObjects(
    ("Hagedorn-MIB", "iprtAudioTableSpeakerName")
)
if mibBuilder.loadTexts:
    iprtAudioTableSpeakerNameTrap.setStatus(
        "current"
    )

iprtAudioTableSpeakerVolumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 6, 2)
)
iprtAudioTableSpeakerVolumeTrap.setObjects(
    ("Hagedorn-MIB", "iprtAudioTableSpeakerVolume")
)
if mibBuilder.loadTexts:
    iprtAudioTableSpeakerVolumeTrap.setStatus(
        "current"
    )

iprtAudioTableMicrophoneNameTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 6, 3)
)
iprtAudioTableMicrophoneNameTrap.setObjects(
    ("Hagedorn-MIB", "iprtAudioTableMicrophoneName")
)
if mibBuilder.loadTexts:
    iprtAudioTableMicrophoneNameTrap.setStatus(
        "current"
    )

iprtAudioTableMicrophoneVolumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 6, 4)
)
iprtAudioTableMicrophoneVolumeTrap.setObjects(
    ("Hagedorn-MIB", "iprtAudioTableMicrophoneVolume")
)
if mibBuilder.loadTexts:
    iprtAudioTableMicrophoneVolumeTrap.setStatus(
        "current"
    )

iprtAudioTableNoiseGateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 6, 5)
)
iprtAudioTableNoiseGateTrap.setObjects(
    ("Hagedorn-MIB", "iprtAudioTableNoiseGate")
)
if mibBuilder.loadTexts:
    iprtAudioTableNoiseGateTrap.setStatus(
        "current"
    )

iprtAudioTableNoiseGateTresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 6, 6)
)
iprtAudioTableNoiseGateTresholdTrap.setObjects(
    ("Hagedorn-MIB", "iprtAudioTableNoiseGateTreshold")
)
if mibBuilder.loadTexts:
    iprtAudioTableNoiseGateTresholdTrap.setStatus(
        "current"
    )

iprtAudioTableNoiseGateAttackTimeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 6, 7)
)
iprtAudioTableNoiseGateAttackTimeTrap.setObjects(
    ("Hagedorn-MIB", "iprtAudioTableNoiseGateAttackTime")
)
if mibBuilder.loadTexts:
    iprtAudioTableNoiseGateAttackTimeTrap.setStatus(
        "current"
    )

iprtAudioTableNoiseGateReleaseTimeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 6, 8)
)
iprtAudioTableNoiseGateReleaseTimeTrap.setObjects(
    ("Hagedorn-MIB", "iprtAudioTableNoiseGateReleaseTime")
)
if mibBuilder.loadTexts:
    iprtAudioTableNoiseGateReleaseTimeTrap.setStatus(
        "current"
    )

iprtAudioTableNoiseGateHoldTimeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 6, 9)
)
iprtAudioTableNoiseGateHoldTimeTrap.setObjects(
    ("Hagedorn-MIB", "iprtAudioTableNoiseGateHoldTime")
)
if mibBuilder.loadTexts:
    iprtAudioTableNoiseGateHoldTimeTrap.setStatus(
        "current"
    )

crysGenTmgListenerStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 4, 0, 1)
)
crysGenTmgListenerStateTrap.setObjects(
    ("Hagedorn-MIB", "crysGenTmgListenerState")
)
if mibBuilder.loadTexts:
    crysGenTmgListenerStateTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Hagedorn-MIB",
    **{"TMGGeneralState": TMGGeneralState,
       "TMGSessionState": TMGSessionState,
       "ComponentState": ComponentState,
       "CrysCallCommType": CrysCallCommType,
       "CrysCallTalkerType": CrysCallTalkerType,
       "IPRTChannelState": IPRTChannelState,
       "IPRTChannelDevice": IPRTChannelDevice,
       "IPRTChannelCommType": IPRTChannelCommType,
       "IPRTGeneralState": IPRTGeneralState,
       "IPRTConnectionsState": IPRTConnectionsState,
       "IPRTAudioBoxDevice": IPRTAudioBoxDevice,
       "IPRTAudioNoiseGate": IPRTAudioNoiseGate,
       "TIPRUProcState": TIPRUProcState,
       "TIPRUAudioState": TIPRUAudioState,
       "TIPRURadioState": TIPRURadioState,
       "TIPRUMode": TIPRUMode,
       "TIPRURSP": TIPRURSP,
       "TAudioBoxProcState": TAudioBoxProcState,
       "TAudioBoxAudioState": TAudioBoxAudioState,
       "TRecorderServiceState": TRecorderServiceState,
       "TRecorderDatabaseState": TRecorderDatabaseState,
       "TSystemConfigWebServiceState": TSystemConfigWebServiceState,
       "TSystemConfigXmlDocState": TSystemConfigXmlDocState,
       "TSystemConfigDatabaseState": TSystemConfigDatabaseState,
       "TConnectionState": TConnectionState,
       "TTimeLimitUnit": TTimeLimitUnit,
       "TTmgProxyServiceState": TTmgProxyServiceState,
       "TGeneralState": TGeneralState,
       "TLicenceState": TLicenceState,
       "TDrGwClientType": TDrGwClientType,
       "TClientConnectionType": TClientConnectionType,
       "TClientState": TClientState,
       "ChannelState": ChannelState,
       "ChannelDevice": ChannelDevice,
       "ChannelCommType": ChannelCommType,
       "hagedorn": hagedorn,
       "tmg": tmg,
       "tmgGeneral": tmgGeneral,
       "tmgGenStateCrypto": tmgGenStateCrypto,
       "tmgGenStateRATS": tmgGenStateRATS,
       "tmgGenStateE1C": tmgGenStateE1C,
       "tmgSessions": tmgSessions,
       "tmgSessionsTable": tmgSessionsTable,
       "tmgSessionsTableEntry": tmgSessionsTableEntry,
       "tmgSessionsTableIdx": tmgSessionsTableIdx,
       "tmgSessionsTableRowStatus": tmgSessionsTableRowStatus,
       "tmgSessionsTableISSI": tmgSessionsTableISSI,
       "tmgSessionsTableState": tmgSessionsTableState,
       "tmgSessionsTableInitState": tmgSessionsTableInitState,
       "tmgSessionsTableTcpSocketsPort": tmgSessionsTableTcpSocketsPort,
       "tmgSessionsTableTCS": tmgSessionsTableTCS,
       "tmgSessionsTableTcpSocketsPort2": tmgSessionsTableTcpSocketsPort2,
       "tmgSessionsTableTCS2": tmgSessionsTableTCS2,
       "tmgSessionsTableWsUser": tmgSessionsTableWsUser,
       "tmgSessionsTablePwd": tmgSessionsTablePwd,
       "tmgSessionsTableUseEncryptedLogin": tmgSessionsTableUseEncryptedLogin,
       "tmgSessionsTableSpeechTimeslot": tmgSessionsTableSpeechTimeslot,
       "tmgSessionsTableMonTimeslots": tmgSessionsTableMonTimeslots,
       "tmgSessionsTableE1TrunkState": tmgSessionsTableE1TrunkState,
       "tmgSessionsTableReadTCSStates": tmgSessionsTableReadTCSStates,
       "tmgSessionsTableTCSStateTCS": tmgSessionsTableTCSStateTCS,
       "tmgSessionsTableTCSStateDXT": tmgSessionsTableTCSStateDXT,
       "tmgSessionsTableTCSStateCDDConnection": tmgSessionsTableTCSStateCDDConnection,
       "tmgSessionsTableTCSStateCDDServer": tmgSessionsTableTCSStateCDDServer,
       "tmgSessionsTableTCSStateTDSC": tmgSessionsTableTCSStateTDSC,
       "tmgSessionsTraps": tmgSessionsTraps,
       "tmgSessionsStateTrap": tmgSessionsStateTrap,
       "tmgClients": tmgClients,
       "tmgClientsTable": tmgClientsTable,
       "tmgClientsTableEntry": tmgClientsTableEntry,
       "tmgClientsTableIdx": tmgClientsTableIdx,
       "tmgClientsTableRowStatus": tmgClientsTableRowStatus,
       "tmgClientsTableName": tmgClientsTableName,
       "tmgClientsTableIPPort": tmgClientsTableIPPort,
       "tmgClientsTableVersion": tmgClientsTableVersion,
       "tmgE1States": tmgE1States,
       "tmgE1StatesTable": tmgE1StatesTable,
       "tmgE1StatesTableEntry": tmgE1StatesTableEntry,
       "tmgE1StatesTableIdx": tmgE1StatesTableIdx,
       "tmgE1StatesTableRowStatus": tmgE1StatesTableRowStatus,
       "tmgE1StatesTableName": tmgE1StatesTableName,
       "tmgE1StatesTableState": tmgE1StatesTableState,
       "kryptoSrv": kryptoSrv,
       "ksGeneral": ksGeneral,
       "ksGenKryxConnected": ksGenKryxConnected,
       "ksGenKryxLastStatusCode": ksGenKryxLastStatusCode,
       "ksGenKryxLastStatusText": ksGenKryxLastStatusText,
       "ksGeneralTraps": ksGeneralTraps,
       "ksGenKryxConnectedTrap": ksGenKryxConnectedTrap,
       "ksGenKryxLastStatusCodeTrap": ksGenKryxLastStatusCodeTrap,
       "ksGenKryxLastStatusTextTrap": ksGenKryxLastStatusTextTrap,
       "ipRadioTouch": ipRadioTouch,
       "iprtGeneral": iprtGeneral,
       "iprtGenUserName": iprtGenUserName,
       "iprtGenVersion": iprtGenVersion,
       "iprtGenState": iprtGenState,
       "iprtGenOsUser": iprtGenOsUser,
       "iprtGenRole": iprtGenRole,
       "iprtGenVtlstState": iprtGenVtlstState,
       "iprtGenRecorderState": iprtGenRecorderState,
       "iprtGenAudioBoxDevice": iprtGenAudioBoxDevice,
       "iprtGenAudioBoxExtSpeaker1Volume": iprtGenAudioBoxExtSpeaker1Volume,
       "iprtGenAudioBoxExtSpeaker2Volume": iprtGenAudioBoxExtSpeaker2Volume,
       "iprtGenAudioBoxExtSpeaker3Volume": iprtGenAudioBoxExtSpeaker3Volume,
       "iprtGenAudioBoxExtSpeaker4Volume": iprtGenAudioBoxExtSpeaker4Volume,
       "iprtGenAudioBoxActualSpeakerVolume": iprtGenAudioBoxActualSpeakerVolume,
       "iprtGenAudioBoxMixedSpeakerVolume": iprtGenAudioBoxMixedSpeakerVolume,
       "iprtGenAudioBoxHeadsetSpeakerVolume": iprtGenAudioBoxHeadsetSpeakerVolume,
       "iprtGenAudioBoxHandsetSpeakerVolume": iprtGenAudioBoxHandsetSpeakerVolume,
       "iprtGenAudioBoxLineOutSpeakerVolume": iprtGenAudioBoxLineOutSpeakerVolume,
       "iprtGeneralTraps": iprtGeneralTraps,
       "iprtGenUserNameTrap": iprtGenUserNameTrap,
       "iprtGenVersionTrap": iprtGenVersionTrap,
       "iprtGenStateTrap": iprtGenStateTrap,
       "iprtGenOsUserTrap": iprtGenOsUserTrap,
       "iprtGenRoleTrap": iprtGenRoleTrap,
       "iprtGenVtlstStateTrap": iprtGenVtlstStateTrap,
       "iprtGenRecorderStateTrap": iprtGenRecorderStateTrap,
       "iprtGenAudioBoxDeviceTrap": iprtGenAudioBoxDeviceTrap,
       "iprtGenAudioBoxExtSpeaker1VolumeTrap": iprtGenAudioBoxExtSpeaker1VolumeTrap,
       "iprtGenAudioBoxExtSpeaker2VolumeTrap": iprtGenAudioBoxExtSpeaker2VolumeTrap,
       "iprtGenAudioBoxExtSpeaker3VolumeTrap": iprtGenAudioBoxExtSpeaker3VolumeTrap,
       "iprtGenAudioBoxExtSpeaker4VolumeTrap": iprtGenAudioBoxExtSpeaker4VolumeTrap,
       "iprtGenAudioBoxActualSpeakerVolumeTrap": iprtGenAudioBoxActualSpeakerVolumeTrap,
       "iprtGenAudioBoxMixedSpeakerVolumeTrap": iprtGenAudioBoxMixedSpeakerVolumeTrap,
       "iprtGenAudioBoxHeadsetSpeakerVolumeTrap": iprtGenAudioBoxHeadsetSpeakerVolumeTrap,
       "iprtGenAudioBoxHandsetSpeakerVolumeTrap": iprtGenAudioBoxHandsetSpeakerVolumeTrap,
       "iprtGenAudioBoxLineOutSpeakerVolumeTrap": iprtGenAudioBoxLineOutSpeakerVolumeTrap,
       "iprtChannels": iprtChannels,
       "iprtChannelsTable": iprtChannelsTable,
       "iprtChannelsTableEntry": iprtChannelsTableEntry,
       "iprtChannelsTableIdx": iprtChannelsTableIdx,
       "iprtChannelsTableRowStatus": iprtChannelsTableRowStatus,
       "iprtChannelsTableID": iprtChannelsTableID,
       "iprtChannelsTableRegistered": iprtChannelsTableRegistered,
       "iprtChannelsTableState": iprtChannelsTableState,
       "iprtChannelsTableISSI": iprtChannelsTableISSI,
       "iprtChannelsTableGSSI": iprtChannelsTableGSSI,
       "iprtChannelsTableDevice": iprtChannelsTableDevice,
       "iprtChannelsTableCommType": iprtChannelsTableCommType,
       "iprtChannelsTraps": iprtChannelsTraps,
       "iprtChannelsRegisteredTrap": iprtChannelsRegisteredTrap,
       "iprtChannelsStateTrap": iprtChannelsStateTrap,
       "iprtChannelsTableISSITrap": iprtChannelsTableISSITrap,
       "iprtChannelsTableGSSITrap": iprtChannelsTableGSSITrap,
       "iprtChannelsTableDeviceTrap": iprtChannelsTableDeviceTrap,
       "iprtChannelsTableCommTypeTrap": iprtChannelsTableCommTypeTrap,
       "iprtAudio": iprtAudio,
       "iprtAudioTable": iprtAudioTable,
       "iprtAudioTableEntry": iprtAudioTableEntry,
       "iprtAudioTableIdx": iprtAudioTableIdx,
       "iprtAudioTableRowStatus": iprtAudioTableRowStatus,
       "iprtAudioTableID": iprtAudioTableID,
       "iprtAudioTableSpeakerName": iprtAudioTableSpeakerName,
       "iprtAudioTableSpeakerVolume": iprtAudioTableSpeakerVolume,
       "iprtAudioTableMicrophoneName": iprtAudioTableMicrophoneName,
       "iprtAudioTableMicrophoneVolume": iprtAudioTableMicrophoneVolume,
       "iprtAudioTableNoiseGate": iprtAudioTableNoiseGate,
       "iprtAudioTableNoiseGateTreshold": iprtAudioTableNoiseGateTreshold,
       "iprtAudioTableNoiseGateAttackTime": iprtAudioTableNoiseGateAttackTime,
       "iprtAudioTableNoiseGateReleaseTime": iprtAudioTableNoiseGateReleaseTime,
       "iprtAudioTableNoiseGateHoldTime": iprtAudioTableNoiseGateHoldTime,
       "iprtAudioTraps": iprtAudioTraps,
       "iprtAudioTableSpeakerNameTrap": iprtAudioTableSpeakerNameTrap,
       "iprtAudioTableSpeakerVolumeTrap": iprtAudioTableSpeakerVolumeTrap,
       "iprtAudioTableMicrophoneNameTrap": iprtAudioTableMicrophoneNameTrap,
       "iprtAudioTableMicrophoneVolumeTrap": iprtAudioTableMicrophoneVolumeTrap,
       "iprtAudioTableNoiseGateTrap": iprtAudioTableNoiseGateTrap,
       "iprtAudioTableNoiseGateTresholdTrap": iprtAudioTableNoiseGateTresholdTrap,
       "iprtAudioTableNoiseGateAttackTimeTrap": iprtAudioTableNoiseGateAttackTimeTrap,
       "iprtAudioTableNoiseGateReleaseTimeTrap": iprtAudioTableNoiseGateReleaseTimeTrap,
       "iprtAudioTableNoiseGateHoldTimeTrap": iprtAudioTableNoiseGateHoldTimeTrap,
       "crys": crys,
       "crysGeneralTraps": crysGeneralTraps,
       "crysGenTmgListenerStateTrap": crysGenTmgListenerStateTrap,
       "crysGeneral": crysGeneral,
       "crysGenTmg": crysGenTmg,
       "crysGenTmgListenAddress": crysGenTmgListenAddress,
       "crysGenTmgListenerState": crysGenTmgListenerState,
       "crysGenTmgSocketAddress": crysGenTmgSocketAddress,
       "crysGenTmgSocketState": crysGenTmgSocketState,
       "crysGenE1s": crysGenE1s,
       "crysGenE1sListenSocketAddress": crysGenE1sListenSocketAddress,
       "crysGenE1sListenSocketState": crysGenE1sListenSocketState,
       "crysGenE1sSendSocketAddress": crysGenE1sSendSocketAddress,
       "crysGenE1sSendToAddress": crysGenE1sSendToAddress,
       "crysGenE1sSendSocketState": crysGenE1sSendSocketState,
       "crysGenRats": crysGenRats,
       "crysGenRatsListenSocketAddress": crysGenRatsListenSocketAddress,
       "crysGenRatsListenSocketState": crysGenRatsListenSocketState,
       "crysGenRatsSendSocketAddress": crysGenRatsSendSocketAddress,
       "crysGenRatsSendToAddress": crysGenRatsSendToAddress,
       "crysGenRatsSendSocketState": crysGenRatsSendSocketState,
       "crysMkkDaemons": crysMkkDaemons,
       "crysMkkDaemonsTable": crysMkkDaemonsTable,
       "crysMkkDaemonsTableEntry": crysMkkDaemonsTableEntry,
       "crysMkkDaemonsTableIdx": crysMkkDaemonsTableIdx,
       "crysMkkDaemonsTableRowStatus": crysMkkDaemonsTableRowStatus,
       "crysMkkDaemonsTableMkkDaemonNr": crysMkkDaemonsTableMkkDaemonNr,
       "crysMkkDaemonsTableAddress": crysMkkDaemonsTableAddress,
       "crysMkkDaemonsTableConnStatus": crysMkkDaemonsTableConnStatus,
       "crysMkkDaemonsTableVersion": crysMkkDaemonsTableVersion,
       "crysMkkDaemonsTableDriverVersion": crysMkkDaemonsTableDriverVersion,
       "crysMkkDaemonsTableDriverError": crysMkkDaemonsTableDriverError,
       "crysMkkCards": crysMkkCards,
       "crysMkkCardsTable": crysMkkCardsTable,
       "crysMkkCardsTableEntry": crysMkkCardsTableEntry,
       "crysMkkCardsTableIdx": crysMkkCardsTableIdx,
       "crysMkkCardsTableRowStatus": crysMkkCardsTableRowStatus,
       "crysMkkCardsTableCardNr": crysMkkCardsTableCardNr,
       "crysMkkCardsTableMkkDaemonNr": crysMkkCardsTableMkkDaemonNr,
       "crysMkkCardsTableVersion": crysMkkCardsTableVersion,
       "crysMkkCardsTableHwID": crysMkkCardsTableHwID,
       "crysMkkCardsTableSimcardCount": crysMkkCardsTableSimcardCount,
       "crysMkkCardsTableSimcardLogicalStartNr": crysMkkCardsTableSimcardLogicalStartNr,
       "crysMkkCardsTableSimcardLogicalEndNr": crysMkkCardsTableSimcardLogicalEndNr,
       "crysMkkCardsTableError": crysMkkCardsTableError,
       "crysSimCards": crysSimCards,
       "crysSimCardsTable": crysSimCardsTable,
       "crysSimCardsTableEntry": crysSimCardsTableEntry,
       "crysSimCardsTableIdx": crysSimCardsTableIdx,
       "crysSimCardsTableRowStatus": crysSimCardsTableRowStatus,
       "crysSimCardsTableCardNr": crysSimCardsTableCardNr,
       "crysSimCardsTableMkkDaemonNr": crysSimCardsTableMkkDaemonNr,
       "crysSimCardsTableHwId": crysSimCardsTableHwId,
       "crysSimCardsTableSubId": crysSimCardsTableSubId,
       "crysSimCardsTableHwOpta": crysSimCardsTableHwOpta,
       "crysSimCardsTableStatus": crysSimCardsTableStatus,
       "crysSimCardsTableLastSW": crysSimCardsTableLastSW,
       "crysCalls": crysCalls,
       "crysCallsTable": crysCallsTable,
       "crysCallsTableEntry": crysCallsTableEntry,
       "crysCallsTableIdx": crysCallsTableIdx,
       "crysCallsTableRowStatus": crysCallsTableRowStatus,
       "crysCallsTableSsrcFromE1": crysCallsTableSsrcFromE1,
       "crysCallsTableMkkDaemonNr": crysCallsTableMkkDaemonNr,
       "crysCallsTableMkkSimCardNr": crysCallsTableMkkSimCardNr,
       "crysCallsTableCommType": crysCallsTableCommType,
       "crysCallsTableDuplex": crysCallsTableDuplex,
       "crysCallsTableE2ee": crysCallsTableE2ee,
       "crysCallsTableCallerITSI": crysCallsTableCallerITSI,
       "crysCallsTableCallerOpta": crysCallsTableCallerOpta,
       "crysCallsTableCalleeTSI": crysCallsTableCalleeTSI,
       "crysCallsTableCalleeOpta": crysCallsTableCalleeOpta,
       "crysCallsTableTalkerType": crysCallsTableTalkerType,
       "crysCallsTableTalkerITSI": crysCallsTableTalkerITSI,
       "crysCallsTableTalkerOpta": crysCallsTableTalkerOpta,
       "crysCallsTableStartTime": crysCallsTableStartTime,
       "crysCallsTableLastActivityTime": crysCallsTableLastActivityTime,
       "crysCallsTableSimCardLastSW": crysCallsTableSimCardLastSW,
       "crysCallsTableError": crysCallsTableError,
       "rats": rats,
       "ratsGeneralTraps": ratsGeneralTraps,
       "ratsGeneral": ratsGeneral,
       "ratsGenTmg": ratsGenTmg,
       "ratsGenTmgListenAddress": ratsGenTmgListenAddress,
       "ratsGenTmgListenerState": ratsGenTmgListenerState,
       "ratsGenTmgSocketAddress": ratsGenTmgSocketAddress,
       "ratsGenTmgSocketState": ratsGenTmgSocketState,
       "ratsGenE1s": ratsGenE1s,
       "ratsGenE1sListenSocketAddress": ratsGenE1sListenSocketAddress,
       "ratsGenE1sListenSocketState": ratsGenE1sListenSocketState,
       "ratsGenE1sSendSocketAddress": ratsGenE1sSendSocketAddress,
       "ratsGenE1sSendToAddress": ratsGenE1sSendToAddress,
       "ratsGenE1sSendSocketState": ratsGenE1sSendSocketState,
       "ratsGenCrys": ratsGenCrys,
       "ratsGenCrysListenSocketAddress": ratsGenCrysListenSocketAddress,
       "ratsGenCrysListenSocketState": ratsGenCrysListenSocketState,
       "ratsGenCrysSendSocketAddress": ratsGenCrysSendSocketAddress,
       "ratsGenCrysSendToAddress": ratsGenCrysSendToAddress,
       "ratsGenCrysSendSocketState": ratsGenCrysSendSocketState,
       "ratsGenStatus": ratsGenStatus,
       "ratsGenStatusConfig": ratsGenStatusConfig,
       "ratsGenStatusGroupsCount": ratsGenStatusGroupsCount,
       "ratsGenStatusMembersCount": ratsGenStatusMembersCount,
       "e1s": e1s,
       "e1sGeneralTraps": e1sGeneralTraps,
       "e1sGeneral": e1sGeneral,
       "e1sGenTmg": e1sGenTmg,
       "e1sGenTmgListenAddress": e1sGenTmgListenAddress,
       "e1sGenTmgListenerState": e1sGenTmgListenerState,
       "e1sGenTmgSocketAddress": e1sGenTmgSocketAddress,
       "e1sGenTmgSocketState": e1sGenTmgSocketState,
       "e1sGenComm": e1sGenComm,
       "e1sGenCommListenSocketAddress": e1sGenCommListenSocketAddress,
       "e1sGenCommListenSocketState": e1sGenCommListenSocketState,
       "e1sGenCommSendSocketAddress": e1sGenCommSendSocketAddress,
       "e1sGenCommSendToAddress": e1sGenCommSendToAddress,
       "e1sGenCommSendSocketState": e1sGenCommSendSocketState,
       "e1sPorts": e1sPorts,
       "e1sPortsTable": e1sPortsTable,
       "e1sPortsTableEntry": e1sPortsTableEntry,
       "e1sPortsTableIdx": e1sPortsTableIdx,
       "e1sPortsTableRowStatus": e1sPortsTableRowStatus,
       "e1sPortsTablePortNr": e1sPortsTablePortNr,
       "e1sPortsTableStatus": e1sPortsTableStatus,
       "e1sPortsTableAlarm": e1sPortsTableAlarm,
       "e1sPortsTableAIS": e1sPortsTableAIS,
       "e1sPortsTableALOS": e1sPortsTableALOS,
       "e1sPortsTableLCV": e1sPortsTableLCV,
       "e1sPortsTableLIULOS": e1sPortsTableLIULOS,
       "e1sPortsTableLIUOC": e1sPortsTableLIUOC,
       "e1sPortsTableLIUSC": e1sPortsTableLIUSC,
       "e1sPortsTableLOF": e1sPortsTableLOF,
       "e1sPortsTableLOS": e1sPortsTableLOS,
       "e1sPortsTableRAI": e1sPortsTableRAI,
       "e1sPortsTableRED": e1sPortsTableRED,
       "e1sPortsTableBITErr": e1sPortsTableBITErr,
       "e1sPortsTableCRC4Err": e1sPortsTableCRC4Err,
       "e1sPortsTableFASErr": e1sPortsTableFASErr,
       "e1sPortsTableFEBErr": e1sPortsTableFEBErr,
       "e1sPortsTableFERErr": e1sPortsTableFERErr,
       "e1sPortsTableOOFErr": e1sPortsTableOOFErr,
       "ipRadioUnit": ipRadioUnit,
       "ipruProcA": ipruProcA,
       "ipruProcAProcState": ipruProcAProcState,
       "ipruProcAAudioState": ipruProcAAudioState,
       "ipruProcARadioState": ipruProcARadioState,
       "ipruProcAMode": ipruProcAMode,
       "ipruProcAActGroup": ipruProcAActGroup,
       "ipruProcARSP": ipruProcARSP,
       "ipruProcB": ipruProcB,
       "ipruProcBProcState": ipruProcBProcState,
       "ipruProcBAudioState": ipruProcBAudioState,
       "ipruProcBRadioState": ipruProcBRadioState,
       "ipruProcBMode": ipruProcBMode,
       "ipruProcBActGroup": ipruProcBActGroup,
       "ipruProcBRSP": ipruProcBRSP,
       "audioBox": audioBox,
       "audioBoxProcState": audioBoxProcState,
       "audioBoxAudioState": audioBoxAudioState,
       "recorder": recorder,
       "recorderGeneral": recorderGeneral,
       "recorderGenVersion": recorderGenVersion,
       "recorderGenServiceState": recorderGenServiceState,
       "recorderGenGatewaysConnected": recorderGenGatewaysConnected,
       "recorderGenDatabaseState": recorderGenDatabaseState,
       "recorderGenCallCount": recorderGenCallCount,
       "recorderGenSdsCount": recorderGenSdsCount,
       "recorderGenStatusCount": recorderGenStatusCount,
       "recorderGenFreeSpace": recorderGenFreeSpace,
       "systemconfig": systemconfig,
       "systemconfigGeneral": systemconfigGeneral,
       "systemconfigGenVersion": systemconfigGenVersion,
       "systemconfigGenWebServiceState": systemconfigGenWebServiceState,
       "systemconfigGenXmlDocState": systemconfigGenXmlDocState,
       "systemconfigGenDatabaseState": systemconfigGenDatabaseState,
       "systemconfigGenPhonebookItemCount": systemconfigGenPhonebookItemCount,
       "systemconfigGenAnalogChannelCount": systemconfigGenAnalogChannelCount,
       "systemconfigGenAnalogRadioCount": systemconfigGenAnalogRadioCount,
       "systemconfigGenTetraGroupCount": systemconfigGenTetraGroupCount,
       "systemconfigGenTetraRadioCount": systemconfigGenTetraRadioCount,
       "systemconfigGenTetraApplicationCount": systemconfigGenTetraApplicationCount,
       "logrotate": logrotate,
       "logrotateGeneral": logrotateGeneral,
       "logrotateGenVersion": logrotateGenVersion,
       "logrotateGenTimeStamp": logrotateGenTimeStamp,
       "logrotateGenNewestFile": logrotateGenNewestFile,
       "logrotateGenOldestFile": logrotateGenOldestFile,
       "dbmaintenance": dbmaintenance,
       "dbmaintenanceGeneral": dbmaintenanceGeneral,
       "dbmaintenanceGenVersion": dbmaintenanceGenVersion,
       "dbmaintenanceGenBeginTimeStamp": dbmaintenanceGenBeginTimeStamp,
       "dbmaintenanceGenEndTimeStamp": dbmaintenanceGenEndTimeStamp,
       "dbmaintenanceGenDBNode": dbmaintenanceGenDBNode,
       "dbmaintenanceGenDBName": dbmaintenanceGenDBName,
       "dbmaintenanceGenDBConnectionState": dbmaintenanceGenDBConnectionState,
       "dbmaintenanceGenDbConnectionStateTStamp": dbmaintenanceGenDbConnectionStateTStamp,
       "dbmaintenanceGenForceTime": dbmaintenanceGenForceTime,
       "dbmaintenanceGenMaintenaceInterval": dbmaintenanceGenMaintenaceInterval,
       "dbmaintenanceGenCheckInterval": dbmaintenanceGenCheckInterval,
       "dbmaintenanceCall": dbmaintenanceCall,
       "dbmaintenanceCallIsTimeLimit": dbmaintenanceCallIsTimeLimit,
       "dbmaintenanceCallTimeLimitVal": dbmaintenanceCallTimeLimitVal,
       "dbmaintenanceCallTimeLimitUnit": dbmaintenanceCallTimeLimitUnit,
       "dbmaintenanceCallSimplexSQLStmt": dbmaintenanceCallSimplexSQLStmt,
       "dbmaintenanceCallSimplexSQLResCount": dbmaintenanceCallSimplexSQLResCount,
       "dbmaintenanceCallDuplexSQLStmt": dbmaintenanceCallDuplexSQLStmt,
       "dbmaintenanceCallDuplexSQLResCount": dbmaintenanceCallDuplexSQLResCount,
       "dbmaintenanceCallAudioIsTimeLimit": dbmaintenanceCallAudioIsTimeLimit,
       "dbmaintenanceCallAudioTimeLimitVal": dbmaintenanceCallAudioTimeLimitVal,
       "dbmaintenanceCallAudioTimeLimitUnit": dbmaintenanceCallAudioTimeLimitUnit,
       "dbmaintenanceSDS": dbmaintenanceSDS,
       "dbmaintenanceSDSIsTimeLimit": dbmaintenanceSDSIsTimeLimit,
       "dbmaintenanceSDSTimeLimitVal": dbmaintenanceSDSTimeLimitVal,
       "dbmaintenanceSDSTimeLimitUnit": dbmaintenanceSDSTimeLimitUnit,
       "dbmaintenanceSDSSQLStmt": dbmaintenanceSDSSQLStmt,
       "dbmaintenanceSDSSQLResCount": dbmaintenanceSDSSQLResCount,
       "dbmaintenanceStatus": dbmaintenanceStatus,
       "dbmaintenanceStatusIsTimeLimit": dbmaintenanceStatusIsTimeLimit,
       "dbmaintenanceStatusTimeLimitVal": dbmaintenanceStatusTimeLimitVal,
       "dbmaintenanceStatusTimeLimitUnit": dbmaintenanceStatusTimeLimitUnit,
       "dbmaintenanceStatusSQLStmt": dbmaintenanceStatusSQLStmt,
       "dbmaintenanceStatusSQLResCount": dbmaintenanceStatusSQLResCount,
       "dbWatchdog": dbWatchdog,
       "dbWatchdogGeneral": dbWatchdogGeneral,
       "dbWatchdogGenVersion": dbWatchdogGenVersion,
       "dbWatchdogGenTimeStamp": dbWatchdogGenTimeStamp,
       "dbWatchdogGenName": dbWatchdogGenName,
       "dbWatchdogGenNode": dbWatchdogGenNode,
       "dbWatchdogGenEngine": dbWatchdogGenEngine,
       "dbWatchdogGenConnectionState": dbWatchdogGenConnectionState,
       "tmgProxy": tmgProxy,
       "tmgProxyGeneral": tmgProxyGeneral,
       "tmgProxyGenVersion": tmgProxyGenVersion,
       "tmgProxyGenServiceState": tmgProxyGenServiceState,
       "tmgProxyGenRATSState": tmgProxyGenRATSState,
       "tmgProxyGenLicenceState": tmgProxyGenLicenceState,
       "tmgProxyDrGwClients": tmgProxyDrGwClients,
       "tmgProxyDrGwClientsTable": tmgProxyDrGwClientsTable,
       "tmgProxyDrGwClientsTableEntry": tmgProxyDrGwClientsTableEntry,
       "tmgProxyDrGwClientsTableIdx": tmgProxyDrGwClientsTableIdx,
       "tmgProxyDrGwClientsTableRowStatus": tmgProxyDrGwClientsTableRowStatus,
       "tmgProxyDrGwClientsTableName": tmgProxyDrGwClientsTableName,
       "tmgProxyDrGwClientsTableDescription": tmgProxyDrGwClientsTableDescription,
       "tmgProxyDrGwClientsTableType": tmgProxyDrGwClientsTableType,
       "tmgProxyDrGwClientsTableSipState": tmgProxyDrGwClientsTableSipState,
       "tmgProxyDrGwClientsTableSoapState": tmgProxyDrGwClientsTableSoapState,
       "tmgProxyClients": tmgProxyClients,
       "tmgProxyClientsTable": tmgProxyClientsTable,
       "tmgProxyClientsTableEntry": tmgProxyClientsTableEntry,
       "tmgProxyClientsTableIdx": tmgProxyClientsTableIdx,
       "tmgProxyClientsTableRowStatus": tmgProxyClientsTableRowStatus,
       "tmgProxyClientsTableName": tmgProxyClientsTableName,
       "tmgProxyClientsTableVersion": tmgProxyClientsTableVersion,
       "tmgProxyClientsTableConnectionType": tmgProxyClientsTableConnectionType,
       "tmgProxyClientsTableSipIpPort": tmgProxyClientsTableSipIpPort,
       "tmgProxyClientsTableSipDrGwVersion": tmgProxyClientsTableSipDrGwVersion,
       "tmgProxyClientsTableSipState": tmgProxyClientsTableSipState,
       "tmgProxyClientsTableSoapIpPort": tmgProxyClientsTableSoapIpPort,
       "tmgProxyClientsTableSoapDrGwVersion": tmgProxyClientsTableSoapDrGwVersion,
       "tmgProxyClientsTableSoapState": tmgProxyClientsTableSoapState,
       "tmgProxyClientsTableGroupDialogCount": tmgProxyClientsTableGroupDialogCount,
       "tmgProxyClientsTableIndividualDialogCount": tmgProxyClientsTableIndividualDialogCount,
       "ratsProxy": ratsProxy,
       "ratsProxyGeneral": ratsProxyGeneral,
       "ratsProxyGenVersion": ratsProxyGenVersion,
       "ratsProxyGenTmgListenAddress": ratsProxyGenTmgListenAddress,
       "ratsProxyGenTmgListenerState": ratsProxyGenTmgListenerState,
       "ratsProxyGenTmgSocketAddress": ratsProxyGenTmgSocketAddress,
       "ratsProxyGenTmgSocketState": ratsProxyGenTmgSocketState,
       "ratsProxyGenStatusConfig": ratsProxyGenStatusConfig,
       "ratsProxyGenStatusGroupsCount": ratsProxyGenStatusGroupsCount,
       "ratsProxyGenStatusMembersCount": ratsProxyGenStatusMembersCount,
       "maintenanceSrv": maintenanceSrv,
       "maintenanceSrvGeneral": maintenanceSrvGeneral,
       "maintenanceSrvGenVersion": maintenanceSrvGenVersion,
       "maintenanceSrvGenInterval": maintenanceSrvGenInterval,
       "maintenanceSrvGenLowDiskSpace": maintenanceSrvGenLowDiskSpace,
       "maintenanceSrvGenRootDir": maintenanceSrvGenRootDir,
       "maintenanceSrvGenFileMask": maintenanceSrvGenFileMask,
       "maintenanceSrvGenExcludeMask": maintenanceSrvGenExcludeMask,
       "maintenanceSrvGenValidDays": maintenanceSrvGenValidDays,
       "maintenanceSrvGenValidMins": maintenanceSrvGenValidMins,
       "maintenanceSrvGenDoLog": maintenanceSrvGenDoLog,
       "maintenanceSrvGenCheckAtTime": maintenanceSrvGenCheckAtTime,
       "maintenanceSrvGenZipEnabled": maintenanceSrvGenZipEnabled,
       "maintenanceSrvGenZipDestDir": maintenanceSrvGenZipDestDir,
       "maintenanceSrvGenZipValidDays": maintenanceSrvGenZipValidDays,
       "dfPhonebook": dfPhonebook,
       "dfPhonebookGeneral": dfPhonebookGeneral,
       "dfPhonebookGenVersion": dfPhonebookGenVersion,
       "dfPhonebookGenDBHost": dfPhonebookGenDBHost,
       "dfPhonebookGenDBName": dfPhonebookGenDBName,
       "dfPhonebookGenDBTable": dfPhonebookGenDBTable,
       "dfPhonebookGenDBConnectionState": dfPhonebookGenDBConnectionState,
       "dfPhonebookGenDBConnectionStateReason": dfPhonebookGenDBConnectionStateReason,
       "dfPhonebookGenWSUri": dfPhonebookGenWSUri,
       "dfPhonebookGenWSUser": dfPhonebookGenWSUser,
       "dfPhonebookGenWSConnectionState": dfPhonebookGenWSConnectionState,
       "dfPhonebookGenWSConnectionStateReason": dfPhonebookGenWSConnectionStateReason,
       "dfPhonebookGenXMLTetra": dfPhonebookGenXMLTetra,
       "dfPhonebookGenXMLTetraGroup": dfPhonebookGenXMLTetraGroup,
       "dfPhonebookGenXMLInfo": dfPhonebookGenXMLInfo,
       "dfPhonebookGenFolderDF": dfPhonebookGenFolderDF,
       "dfPhonebookGenFolderWeb": dfPhonebookGenFolderWeb,
       "sipRecGateway": sipRecGateway,
       "sipRecGatewayGeneral": sipRecGatewayGeneral,
       "sipRecGatewayGenVersion": sipRecGatewayGenVersion,
       "sipRecGatewayGenSipIdentity": sipRecGatewayGenSipIdentity,
       "sipRecGatewayGenSipLocalIp": sipRecGatewayGenSipLocalIp,
       "sipRecGatewayGenSipLocalPort": sipRecGatewayGenSipLocalPort,
       "sipRecGatewayGenSipTransTimeout": sipRecGatewayGenSipTransTimeout,
       "sipRecGatewayGenSipTransRetryCount": sipRecGatewayGenSipTransRetryCount,
       "sipRecGatewayGenSipDialogDestroyTimeout": sipRecGatewayGenSipDialogDestroyTimeout,
       "sipRecGatewayGenRecIp": sipRecGatewayGenRecIp,
       "sipRecGatewayGenRecPort": sipRecGatewayGenRecPort,
       "sipRecGatewayGenRecUseSendBuffer": sipRecGatewayGenRecUseSendBuffer,
       "sipRecGatewayGenDevAutoDiscovery": sipRecGatewayGenDevAutoDiscovery,
       "sipRecGatewayGenDevAcceptedUserAgent": sipRecGatewayGenDevAcceptedUserAgent,
       "sipRecGatewayGenDevBroadcastIp": sipRecGatewayGenDevBroadcastIp,
       "sipRecGatewayGenDevBroadcastPort": sipRecGatewayGenDevBroadcastPort,
       "sipRecGatewayGenDevRecIndCall": sipRecGatewayGenDevRecIndCall,
       "sipRecGatewayDev": sipRecGatewayDev,
       "sipRecGatewayDevTable": sipRecGatewayDevTable,
       "sipRecGatewayTableEntry": sipRecGatewayTableEntry,
       "sipRecGatewayTableIdx": sipRecGatewayTableIdx,
       "sipRecGatewayTableRowStatus": sipRecGatewayTableRowStatus,
       "sipRecGatewayTableDescription": sipRecGatewayTableDescription,
       "sipRecGatewayTableType": sipRecGatewayTableType,
       "sipRecGatewayTableRemoteIP": sipRecGatewayTableRemoteIP,
       "sipRecGatewayTableRemotePort": sipRecGatewayTableRemotePort,
       "sipRecGatewayTableMulticastIP": sipRecGatewayTableMulticastIP,
       "sipRecGatewayTableMulticastPort": sipRecGatewayTableMulticastPort,
       "ipRadioPhone": ipRadioPhone,
       "iprpGeneral": iprpGeneral,
       "iprpGenSwVersion": iprpGenSwVersion,
       "iprpGenHwFwVersion": iprpGenHwFwVersion,
       "iprpGenAudioFwVersion": iprpGenAudioFwVersion,
       "iprpGenSwBundleVersion": iprpGenSwBundleVersion,
       "iprpGenSerialNr": iprpGenSerialNr,
       "iprpGenOsScriptsVersion": iprpGenOsScriptsVersion,
       "iprpWorkplace": iprpWorkplace,
       "iprpWorkplaceName": iprpWorkplaceName,
       "iprpWorkplaceOpta": iprpWorkplaceOpta,
       "iprpChannels": iprpChannels,
       "iprpChannelsTable": iprpChannelsTable,
       "iprpChannelsTableEntry": iprpChannelsTableEntry,
       "iprpChannelsTableIdx": iprpChannelsTableIdx,
       "iprpChannelsTableRowStatus": iprpChannelsTableRowStatus,
       "iprpChannelsTableID": iprpChannelsTableID,
       "iprpChannelsTableRegistered": iprpChannelsTableRegistered,
       "iprpChannelsTableState": iprpChannelsTableState,
       "iprpChannelsTableISSI": iprpChannelsTableISSI,
       "iprpChannelsTableGSSI": iprpChannelsTableGSSI,
       "iprpChannelsTableDevice": iprpChannelsTableDevice,
       "iprpChannelsTableCommType": iprpChannelsTableCommType,
       "tttGateway": tttGateway,
       "tttGatewayStates": tttGatewayStates,
       "tttGatewayStatesTable": tttGatewayStatesTable,
       "tttGatewayStatesTableEntry": tttGatewayStatesTableEntry,
       "tttGatewayStatesTableIdx": tttGatewayStatesTableIdx,
       "tttGatewayStatesTableRowStatus": tttGatewayStatesTableRowStatus,
       "tttGatewayStatesTableVersion": tttGatewayStatesTableVersion,
       "tttGatewayStatesTableTimeStamp": tttGatewayStatesTableTimeStamp,
       "tttGatewayStatesTableIdent": tttGatewayStatesTableIdent,
       "tttGatewayStatesTableDfTimeStamp": tttGatewayStatesTableDfTimeStamp,
       "tttGatewayStatesTableDfState": tttGatewayStatesTableDfState,
       "tttGatewayStatesTableDfStateReason": tttGatewayStatesTableDfStateReason,
       "tttGatewayStatesTableDfGSSI": tttGatewayStatesTableDfGSSI,
       "tttGatewayStatesTableIpruTimeStamp": tttGatewayStatesTableIpruTimeStamp,
       "tttGatewayStatesTableIpruState": tttGatewayStatesTableIpruState,
       "tttGatewayStatesTableIpruStateReason": tttGatewayStatesTableIpruStateReason,
       "tttGatewayStatesTableIpruGSSI": tttGatewayStatesTableIpruGSSI}
)
