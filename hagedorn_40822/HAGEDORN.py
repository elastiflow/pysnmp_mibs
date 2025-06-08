# SNMP MIB module (HAGEDORN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/hagedorn_40822/HAGEDORN.mib
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
 RowStatus,
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
    "RowStatus",
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
        *(("tTCS-STATE-T-UNKNOWN-C", 0),
          ("tTCS-STATE-T-OK-C", 1),
          ("tTCS-STATE-T-NOK-C", 2),
          ("tTCS-STATE-T-WO-EX-C", 3),
          ("tTCS-STATE-T-WO-RE-C", 4),
          ("tTCS-STATE-T-BL-EX-C", 5),
          ("tTCS-STATE-T-BL-ID-C", 6),
          ("tTCS-STATE-T-BL-RE-C", 7),
          ("tTCS-STATE-T-TE-EX-C", 8),
          ("tTCS-STATE-T-SE-OU-C", 9),
          ("tTCS-STATE-T-SE-NH-C", 10))
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



class IPRChannelState(TextualConvention, Integer32):
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



# MIB Managed Objects in the order of their OIDs

_Hagedorn_ObjectIdentity = ObjectIdentity
hagedorn = _Hagedorn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822)
)
if mibBuilder.loadTexts:
    hagedorn.setStatus("current")
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
_TmgGenTCSState_Type = TMGGeneralState
_TmgGenTCSState_Object = MibScalar
tmgGenTCSState = _TmgGenTCSState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 1, 1),
    _TmgGenTCSState_Type()
)
tmgGenTCSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmgGenTCSState.setStatus("current")
_TmgGenDXTConnection_Type = TMGGeneralState
_TmgGenDXTConnection_Object = MibScalar
tmgGenDXTConnection = _TmgGenDXTConnection_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 1, 2),
    _TmgGenDXTConnection_Type()
)
tmgGenDXTConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmgGenDXTConnection.setStatus("current")
_TmgGenCDDConnection_Type = TMGGeneralState
_TmgGenCDDConnection_Object = MibScalar
tmgGenCDDConnection = _TmgGenCDDConnection_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 1, 3),
    _TmgGenCDDConnection_Type()
)
tmgGenCDDConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmgGenCDDConnection.setStatus("current")
_TmgGenCDDServer_Type = TMGGeneralState
_TmgGenCDDServer_Object = MibScalar
tmgGenCDDServer = _TmgGenCDDServer_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 1, 4),
    _TmgGenCDDServer_Type()
)
tmgGenCDDServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmgGenCDDServer.setStatus("current")
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
    (0, "HAGEDORN", "tmgSessionsTableIdx"),
)
if mibBuilder.loadTexts:
    tmgSessionsTableEntry.setStatus("current")
_TmgSessionsTableIdx_Type = Integer32
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
tmgSessionsTableRowStatus.setMaxAccess("read-write")
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
_TmgSessionsUseTcpSockets_Type = Integer32
_TmgSessionsUseTcpSockets_Object = MibScalar
tmgSessionsUseTcpSockets = _TmgSessionsUseTcpSockets_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 5),
    _TmgSessionsUseTcpSockets_Type()
)
tmgSessionsUseTcpSockets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsUseTcpSockets.setStatus("current")
_TmgSessionsTcpSocketsPort_Type = Integer32
_TmgSessionsTcpSocketsPort_Object = MibScalar
tmgSessionsTcpSocketsPort = _TmgSessionsTcpSocketsPort_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 6),
    _TmgSessionsTcpSocketsPort_Type()
)
tmgSessionsTcpSocketsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTcpSocketsPort.setStatus("current")


class _TmgSessionsTCS_Type(OctetString):
    """Custom type tmgSessionsTCS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgSessionsTCS_Type.__name__ = "OctetString"
_TmgSessionsTCS_Object = MibScalar
tmgSessionsTCS = _TmgSessionsTCS_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 7),
    _TmgSessionsTCS_Type()
)
tmgSessionsTCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTCS.setStatus("current")


class _TmgSessionsWsUser_Type(OctetString):
    """Custom type tmgSessionsWsUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgSessionsWsUser_Type.__name__ = "OctetString"
_TmgSessionsWsUser_Object = MibScalar
tmgSessionsWsUser = _TmgSessionsWsUser_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 8),
    _TmgSessionsWsUser_Type()
)
tmgSessionsWsUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsWsUser.setStatus("current")


class _TmgSessionsPwd_Type(OctetString):
    """Custom type tmgSessionsPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgSessionsPwd_Type.__name__ = "OctetString"
_TmgSessionsPwd_Object = MibScalar
tmgSessionsPwd = _TmgSessionsPwd_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 9),
    _TmgSessionsPwd_Type()
)
tmgSessionsPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsPwd.setStatus("current")
_TmgSessionsTableUseEncryptedLogin_Type = Integer32
_TmgSessionsTableUseEncryptedLogin_Object = MibTableColumn
tmgSessionsTableUseEncryptedLogin = _TmgSessionsTableUseEncryptedLogin_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 10),
    _TmgSessionsTableUseEncryptedLogin_Type()
)
tmgSessionsTableUseEncryptedLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableUseEncryptedLogin.setStatus("current")
_TmgSessionsTableSpeechTimeslot_Type = Integer32
_TmgSessionsTableSpeechTimeslot_Object = MibTableColumn
tmgSessionsTableSpeechTimeslot = _TmgSessionsTableSpeechTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 11),
    _TmgSessionsTableSpeechTimeslot_Type()
)
tmgSessionsTableSpeechTimeslot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableSpeechTimeslot.setStatus("current")
_TmgSessionsTableMonTimeslots_Type = Integer32
_TmgSessionsTableMonTimeslots_Object = MibTableColumn
tmgSessionsTableMonTimeslots = _TmgSessionsTableMonTimeslots_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 2, 1, 1, 12),
    _TmgSessionsTableMonTimeslots_Type()
)
tmgSessionsTableMonTimeslots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgSessionsTableMonTimeslots.setStatus("current")
_TmgGeneralTraps_ObjectIdentity = ObjectIdentity
tmgGeneralTraps = _TmgGeneralTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 1, 3)
)
if mibBuilder.loadTexts:
    tmgGeneralTraps.setStatus("current")
_TmgSessionsTraps_ObjectIdentity = ObjectIdentity
tmgSessionsTraps = _TmgSessionsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 1, 4)
)
if mibBuilder.loadTexts:
    tmgSessionsTraps.setStatus("current")
_TmgClients_ObjectIdentity = ObjectIdentity
tmgClients = _TmgClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 1, 5)
)
if mibBuilder.loadTexts:
    tmgClients.setStatus("current")
_TmgClientsTable_Object = MibTable
tmgClientsTable = _TmgClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmgClientsTable.setStatus("current")
_TmgClientsTableEntry_Object = MibTableRow
tmgClientsTableEntry = _TmgClientsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 5, 1, 1)
)
tmgClientsTableEntry.setIndexNames(
    (0, "HAGEDORN", "tmgClientsTableIdx"),
)
if mibBuilder.loadTexts:
    tmgClientsTableEntry.setStatus("current")
_TmgClientsTableIdx_Type = Integer32
_TmgClientsTableIdx_Object = MibTableColumn
tmgClientsTableIdx = _TmgClientsTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 5, 1, 1, 1),
    _TmgClientsTableIdx_Type()
)
tmgClientsTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmgClientsTableIdx.setStatus("current")
_TmgClientsTableRowStatus_Type = RowStatus
_TmgClientsTableRowStatus_Object = MibTableColumn
tmgClientsTableRowStatus = _TmgClientsTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 5, 1, 1, 2),
    _TmgClientsTableRowStatus_Type()
)
tmgClientsTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgClientsTableRowStatus.setStatus("current")


class _TmgClientsTableName_Type(OctetString):
    """Custom type tmgClientsTableName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgClientsTableName_Type.__name__ = "OctetString"
_TmgClientsTableName_Object = MibTableColumn
tmgClientsTableName = _TmgClientsTableName_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 5, 1, 1, 3),
    _TmgClientsTableName_Type()
)
tmgClientsTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgClientsTableName.setStatus("current")


class _TmgClientsTableIPPort_Type(OctetString):
    """Custom type tmgClientsTableIPPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgClientsTableIPPort_Type.__name__ = "OctetString"
_TmgClientsTableIPPort_Object = MibTableColumn
tmgClientsTableIPPort = _TmgClientsTableIPPort_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 5, 1, 1, 4),
    _TmgClientsTableIPPort_Type()
)
tmgClientsTableIPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgClientsTableIPPort.setStatus("current")


class _TmgClientsTableVersion_Type(OctetString):
    """Custom type tmgClientsTableVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmgClientsTableVersion_Type.__name__ = "OctetString"
_TmgClientsTableVersion_Object = MibTableColumn
tmgClientsTableVersion = _TmgClientsTableVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 1, 5, 1, 1, 5),
    _TmgClientsTableVersion_Type()
)
tmgClientsTableVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmgClientsTableVersion.setStatus("current")
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
_KsGenKryxClientConnected_Type = Integer32
_KsGenKryxClientConnected_Object = MibScalar
ksGenKryxClientConnected = _KsGenKryxClientConnected_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 1, 1),
    _KsGenKryxClientConnected_Type()
)
ksGenKryxClientConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ksGenKryxClientConnected.setStatus("current")
_KsGenKryxServerConnected_Type = Integer32
_KsGenKryxServerConnected_Object = MibScalar
ksGenKryxServerConnected = _KsGenKryxServerConnected_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 1, 2),
    _KsGenKryxServerConnected_Type()
)
ksGenKryxServerConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ksGenKryxServerConnected.setStatus("current")
_KsGenKryxLastStatusCode_Type = Integer32
_KsGenKryxLastStatusCode_Object = MibScalar
ksGenKryxLastStatusCode = _KsGenKryxLastStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 1, 3),
    _KsGenKryxLastStatusCode_Type()
)
ksGenKryxLastStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ksGenKryxLastStatusCode.setStatus("current")


class _KsGenKryxLastStatusText_Type(OctetString):
    """Custom type ksGenKryxLastStatusText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KsGenKryxLastStatusText_Type.__name__ = "OctetString"
_KsGenKryxLastStatusText_Object = MibScalar
ksGenKryxLastStatusText = _KsGenKryxLastStatusText_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 1, 4),
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
_KsSimCards_ObjectIdentity = ObjectIdentity
ksSimCards = _KsSimCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3)
)
if mibBuilder.loadTexts:
    ksSimCards.setStatus("current")
_KsSimCardsTable_Object = MibTable
ksSimCardsTable = _KsSimCardsTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ksSimCardsTable.setStatus("current")
_KsSimCardsTableEntry_Object = MibTableRow
ksSimCardsTableEntry = _KsSimCardsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1)
)
ksSimCardsTableEntry.setIndexNames(
    (0, "HAGEDORN", "ksSimCardsTableIdx"),
)
if mibBuilder.loadTexts:
    ksSimCardsTableEntry.setStatus("current")
_KsSimCardsTableIdx_Type = Integer32
_KsSimCardsTableIdx_Object = MibTableColumn
ksSimCardsTableIdx = _KsSimCardsTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1, 1),
    _KsSimCardsTableIdx_Type()
)
ksSimCardsTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ksSimCardsTableIdx.setStatus("current")
_KsSimCardsTableRowStatus_Type = RowStatus
_KsSimCardsTableRowStatus_Object = MibTableColumn
ksSimCardsTableRowStatus = _KsSimCardsTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1, 2),
    _KsSimCardsTableRowStatus_Type()
)
ksSimCardsTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ksSimCardsTableRowStatus.setStatus("current")
_KsSimCardsTableCardNr_Type = Integer32
_KsSimCardsTableCardNr_Object = MibTableColumn
ksSimCardsTableCardNr = _KsSimCardsTableCardNr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1, 3),
    _KsSimCardsTableCardNr_Type()
)
ksSimCardsTableCardNr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ksSimCardsTableCardNr.setStatus("current")
_KsSimCardsTableMkkNr_Type = Integer32
_KsSimCardsTableMkkNr_Object = MibTableColumn
ksSimCardsTableMkkNr = _KsSimCardsTableMkkNr_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1, 4),
    _KsSimCardsTableMkkNr_Type()
)
ksSimCardsTableMkkNr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ksSimCardsTableMkkNr.setStatus("current")
_KsSimCardsTablePort_Type = Integer32
_KsSimCardsTablePort_Object = MibTableColumn
ksSimCardsTablePort = _KsSimCardsTablePort_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1, 5),
    _KsSimCardsTablePort_Type()
)
ksSimCardsTablePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ksSimCardsTablePort.setStatus("current")


class _KsSimCardsTableType_Type(OctetString):
    """Custom type ksSimCardsTableType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KsSimCardsTableType_Type.__name__ = "OctetString"
_KsSimCardsTableType_Object = MibTableColumn
ksSimCardsTableType = _KsSimCardsTableType_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1, 6),
    _KsSimCardsTableType_Type()
)
ksSimCardsTableType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ksSimCardsTableType.setStatus("current")


class _KsSimCardsTableOpta_Type(OctetString):
    """Custom type ksSimCardsTableOpta based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KsSimCardsTableOpta_Type.__name__ = "OctetString"
_KsSimCardsTableOpta_Object = MibTableColumn
ksSimCardsTableOpta = _KsSimCardsTableOpta_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1, 7),
    _KsSimCardsTableOpta_Type()
)
ksSimCardsTableOpta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ksSimCardsTableOpta.setStatus("current")
_KsSimCardsTableISSI_Type = Integer32
_KsSimCardsTableISSI_Object = MibTableColumn
ksSimCardsTableISSI = _KsSimCardsTableISSI_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1, 8),
    _KsSimCardsTableISSI_Type()
)
ksSimCardsTableISSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ksSimCardsTableISSI.setStatus("current")


class _KsSimCardsTableForeignOpta_Type(OctetString):
    """Custom type ksSimCardsTableForeignOpta based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KsSimCardsTableForeignOpta_Type.__name__ = "OctetString"
_KsSimCardsTableForeignOpta_Object = MibTableColumn
ksSimCardsTableForeignOpta = _KsSimCardsTableForeignOpta_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1, 9),
    _KsSimCardsTableForeignOpta_Type()
)
ksSimCardsTableForeignOpta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ksSimCardsTableForeignOpta.setStatus("current")
_KsSimCardsTableForeignISSI_Type = Integer32
_KsSimCardsTableForeignISSI_Object = MibTableColumn
ksSimCardsTableForeignISSI = _KsSimCardsTableForeignISSI_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1, 10),
    _KsSimCardsTableForeignISSI_Type()
)
ksSimCardsTableForeignISSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ksSimCardsTableForeignISSI.setStatus("current")


class _KsSimCardsTableGtsi_Type(OctetString):
    """Custom type ksSimCardsTableGtsi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KsSimCardsTableGtsi_Type.__name__ = "OctetString"
_KsSimCardsTableGtsi_Object = MibTableColumn
ksSimCardsTableGtsi = _KsSimCardsTableGtsi_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1, 11),
    _KsSimCardsTableGtsi_Type()
)
ksSimCardsTableGtsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ksSimCardsTableGtsi.setStatus("current")


class _KsSimCardsTableCallerItsi_Type(OctetString):
    """Custom type ksSimCardsTableCallerItsi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KsSimCardsTableCallerItsi_Type.__name__ = "OctetString"
_KsSimCardsTableCallerItsi_Object = MibTableColumn
ksSimCardsTableCallerItsi = _KsSimCardsTableCallerItsi_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1, 12),
    _KsSimCardsTableCallerItsi_Type()
)
ksSimCardsTableCallerItsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ksSimCardsTableCallerItsi.setStatus("current")


class _KsSimCardsTableCalleeItsi_Type(OctetString):
    """Custom type ksSimCardsTableCalleeItsi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KsSimCardsTableCalleeItsi_Type.__name__ = "OctetString"
_KsSimCardsTableCalleeItsi_Object = MibTableColumn
ksSimCardsTableCalleeItsi = _KsSimCardsTableCalleeItsi_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1, 13),
    _KsSimCardsTableCalleeItsi_Type()
)
ksSimCardsTableCalleeItsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ksSimCardsTableCalleeItsi.setStatus("current")
_KsSimCardsTableKryptoStatus_Type = Integer32
_KsSimCardsTableKryptoStatus_Object = MibTableColumn
ksSimCardsTableKryptoStatus = _KsSimCardsTableKryptoStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1, 14),
    _KsSimCardsTableKryptoStatus_Type()
)
ksSimCardsTableKryptoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ksSimCardsTableKryptoStatus.setStatus("current")
_KsSimCardsTableLastStatusCode_Type = Integer32
_KsSimCardsTableLastStatusCode_Object = MibTableColumn
ksSimCardsTableLastStatusCode = _KsSimCardsTableLastStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1, 15),
    _KsSimCardsTableLastStatusCode_Type()
)
ksSimCardsTableLastStatusCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ksSimCardsTableLastStatusCode.setStatus("current")


class _KsSimCardsTableLastStatusText_Type(OctetString):
    """Custom type ksSimCardsTableLastStatusText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KsSimCardsTableLastStatusText_Type.__name__ = "OctetString"
_KsSimCardsTableLastStatusText_Object = MibTableColumn
ksSimCardsTableLastStatusText = _KsSimCardsTableLastStatusText_Object(
    (1, 3, 6, 1, 4, 1, 40822, 2, 3, 1, 1, 16),
    _KsSimCardsTableLastStatusText_Type()
)
ksSimCardsTableLastStatusText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ksSimCardsTableLastStatusText.setStatus("current")
_IpRadio_ObjectIdentity = ObjectIdentity
ipRadio = _IpRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 3)
)
if mibBuilder.loadTexts:
    ipRadio.setStatus("current")
_IprGeneral_ObjectIdentity = ObjectIdentity
iprGeneral = _IprGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1)
)
if mibBuilder.loadTexts:
    iprGeneral.setStatus("current")


class _IprGenUserName_Type(OctetString):
    """Custom type iprGenUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprGenUserName_Type.__name__ = "OctetString"
_IprGenUserName_Object = MibScalar
iprGenUserName = _IprGenUserName_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 1),
    _IprGenUserName_Type()
)
iprGenUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprGenUserName.setStatus("current")


class _IprGenVersion_Type(OctetString):
    """Custom type iprGenVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprGenVersion_Type.__name__ = "OctetString"
_IprGenVersion_Object = MibScalar
iprGenVersion = _IprGenVersion_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 1, 2),
    _IprGenVersion_Type()
)
iprGenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprGenVersion.setStatus("current")
_IprGeneralTraps_ObjectIdentity = ObjectIdentity
iprGeneralTraps = _IprGeneralTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2)
)
if mibBuilder.loadTexts:
    iprGeneralTraps.setStatus("current")
_IprChannels_ObjectIdentity = ObjectIdentity
iprChannels = _IprChannels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3)
)
if mibBuilder.loadTexts:
    iprChannels.setStatus("current")
_IprChannelsTable_Object = MibTable
iprChannelsTable = _IprChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1)
)
if mibBuilder.loadTexts:
    iprChannelsTable.setStatus("current")
_IprChannelsTableEntry_Object = MibTableRow
iprChannelsTableEntry = _IprChannelsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1)
)
iprChannelsTableEntry.setIndexNames(
    (0, "HAGEDORN", "iprChannelsTableIdx"),
)
if mibBuilder.loadTexts:
    iprChannelsTableEntry.setStatus("current")
_IprChannelsTableIdx_Type = Integer32
_IprChannelsTableIdx_Object = MibTableColumn
iprChannelsTableIdx = _IprChannelsTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1, 1),
    _IprChannelsTableIdx_Type()
)
iprChannelsTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iprChannelsTableIdx.setStatus("current")
_IprChannelsTableRowStatus_Type = RowStatus
_IprChannelsTableRowStatus_Object = MibTableColumn
iprChannelsTableRowStatus = _IprChannelsTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1, 2),
    _IprChannelsTableRowStatus_Type()
)
iprChannelsTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprChannelsTableRowStatus.setStatus("current")


class _IprChannelsTableID_Type(OctetString):
    """Custom type iprChannelsTableID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprChannelsTableID_Type.__name__ = "OctetString"
_IprChannelsTableID_Object = MibTableColumn
iprChannelsTableID = _IprChannelsTableID_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1, 3),
    _IprChannelsTableID_Type()
)
iprChannelsTableID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprChannelsTableID.setStatus("current")
_IprChannelsTableRegistered_Type = Integer32
_IprChannelsTableRegistered_Object = MibTableColumn
iprChannelsTableRegistered = _IprChannelsTableRegistered_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1, 4),
    _IprChannelsTableRegistered_Type()
)
iprChannelsTableRegistered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprChannelsTableRegistered.setStatus("current")
_IprChannelsTableState_Type = IPRChannelState
_IprChannelsTableState_Object = MibTableColumn
iprChannelsTableState = _IprChannelsTableState_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1, 5),
    _IprChannelsTableState_Type()
)
iprChannelsTableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprChannelsTableState.setStatus("current")


class _IprChannelsTableISSI_Type(OctetString):
    """Custom type iprChannelsTableISSI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprChannelsTableISSI_Type.__name__ = "OctetString"
_IprChannelsTableISSI_Object = MibTableColumn
iprChannelsTableISSI = _IprChannelsTableISSI_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1, 6),
    _IprChannelsTableISSI_Type()
)
iprChannelsTableISSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprChannelsTableISSI.setStatus("current")


class _IprChannelsTableGSSI_Type(OctetString):
    """Custom type iprChannelsTableGSSI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IprChannelsTableGSSI_Type.__name__ = "OctetString"
_IprChannelsTableGSSI_Object = MibTableColumn
iprChannelsTableGSSI = _IprChannelsTableGSSI_Object(
    (1, 3, 6, 1, 4, 1, 40822, 3, 3, 1, 1, 7),
    _IprChannelsTableGSSI_Type()
)
iprChannelsTableGSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iprChannelsTableGSSI.setStatus("current")
_IprChannelsTraps_ObjectIdentity = ObjectIdentity
iprChannelsTraps = _IprChannelsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40822, 3, 4)
)
if mibBuilder.loadTexts:
    iprChannelsTraps.setStatus("current")

# Managed Objects groups


# Notification objects

tmgGenTCSStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 1, 3, 1)
)
tmgGenTCSStateTrap.setObjects(
    ("HAGEDORN", "tmgGenTCSState")
)
if mibBuilder.loadTexts:
    tmgGenTCSStateTrap.setStatus(
        "current"
    )

tmgGenDXTConnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 1, 3, 2)
)
tmgGenDXTConnectionTrap.setObjects(
    ("HAGEDORN", "tmgGenDXTConnection")
)
if mibBuilder.loadTexts:
    tmgGenDXTConnectionTrap.setStatus(
        "current"
    )

tmgGenCDDConnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 1, 3, 3)
)
tmgGenCDDConnectionTrap.setObjects(
    ("HAGEDORN", "tmgGenCDDConnection")
)
if mibBuilder.loadTexts:
    tmgGenCDDConnectionTrap.setStatus(
        "current"
    )

tmgGenCDDServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 1, 3, 4)
)
tmgGenCDDServerTrap.setObjects(
    ("HAGEDORN", "tmgGenCDDServer")
)
if mibBuilder.loadTexts:
    tmgGenCDDServerTrap.setStatus(
        "current"
    )

tmgSessionsStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 1, 4, 1)
)
tmgSessionsStateTrap.setObjects(
    ("HAGEDORN", "tmgSessionsTableState")
)
if mibBuilder.loadTexts:
    tmgSessionsStateTrap.setStatus(
        "current"
    )

ksGenKryxClientConnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 2, 2, 1)
)
ksGenKryxClientConnectedTrap.setObjects(
    ("HAGEDORN", "ksGenKryxClientConnected")
)
if mibBuilder.loadTexts:
    ksGenKryxClientConnectedTrap.setStatus(
        "current"
    )

ksGenKryxServerConnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 2, 2, 2)
)
ksGenKryxServerConnectedTrap.setObjects(
    ("HAGEDORN", "ksGenKryxServerConnected")
)
if mibBuilder.loadTexts:
    ksGenKryxServerConnectedTrap.setStatus(
        "current"
    )

ksGenKryxLastStatusCodeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 2, 2, 3)
)
ksGenKryxLastStatusCodeTrap.setObjects(
    ("HAGEDORN", "ksGenKryxLastStatusCode")
)
if mibBuilder.loadTexts:
    ksGenKryxLastStatusCodeTrap.setStatus(
        "current"
    )

ksGenKryxLastStatusTextTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 2, 2, 4)
)
ksGenKryxLastStatusTextTrap.setObjects(
    ("HAGEDORN", "ksGenKryxLastStatusText")
)
if mibBuilder.loadTexts:
    ksGenKryxLastStatusTextTrap.setStatus(
        "current"
    )

iprGenUserNameTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 2, 1)
)
iprGenUserNameTrap.setObjects(
    ("HAGEDORN", "iprGenUserName")
)
if mibBuilder.loadTexts:
    iprGenUserNameTrap.setStatus(
        "current"
    )

iprChannelsRegisteredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 4, 1)
)
iprChannelsRegisteredTrap.setObjects(
    ("HAGEDORN", "iprChannelsTableRegistered")
)
if mibBuilder.loadTexts:
    iprChannelsRegisteredTrap.setStatus(
        "current"
    )

iprChannelsStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40822, 3, 4, 2)
)
iprChannelsStateTrap.setObjects(
    ("HAGEDORN", "iprChannelsTableState")
)
if mibBuilder.loadTexts:
    iprChannelsStateTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HAGEDORN",
    **{"TMGGeneralState": TMGGeneralState,
       "TMGSessionState": TMGSessionState,
       "IPRChannelState": IPRChannelState,
       "hagedorn": hagedorn,
       "tmg": tmg,
       "tmgGeneral": tmgGeneral,
       "tmgGenTCSState": tmgGenTCSState,
       "tmgGenDXTConnection": tmgGenDXTConnection,
       "tmgGenCDDConnection": tmgGenCDDConnection,
       "tmgGenCDDServer": tmgGenCDDServer,
       "tmgSessions": tmgSessions,
       "tmgSessionsTable": tmgSessionsTable,
       "tmgSessionsTableEntry": tmgSessionsTableEntry,
       "tmgSessionsTableIdx": tmgSessionsTableIdx,
       "tmgSessionsTableRowStatus": tmgSessionsTableRowStatus,
       "tmgSessionsTableISSI": tmgSessionsTableISSI,
       "tmgSessionsTableState": tmgSessionsTableState,
       "tmgSessionsUseTcpSockets": tmgSessionsUseTcpSockets,
       "tmgSessionsTcpSocketsPort": tmgSessionsTcpSocketsPort,
       "tmgSessionsTCS": tmgSessionsTCS,
       "tmgSessionsWsUser": tmgSessionsWsUser,
       "tmgSessionsPwd": tmgSessionsPwd,
       "tmgSessionsTableUseEncryptedLogin": tmgSessionsTableUseEncryptedLogin,
       "tmgSessionsTableSpeechTimeslot": tmgSessionsTableSpeechTimeslot,
       "tmgSessionsTableMonTimeslots": tmgSessionsTableMonTimeslots,
       "tmgGeneralTraps": tmgGeneralTraps,
       "tmgGenTCSStateTrap": tmgGenTCSStateTrap,
       "tmgGenDXTConnectionTrap": tmgGenDXTConnectionTrap,
       "tmgGenCDDConnectionTrap": tmgGenCDDConnectionTrap,
       "tmgGenCDDServerTrap": tmgGenCDDServerTrap,
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
       "kryptoSrv": kryptoSrv,
       "ksGeneral": ksGeneral,
       "ksGenKryxClientConnected": ksGenKryxClientConnected,
       "ksGenKryxServerConnected": ksGenKryxServerConnected,
       "ksGenKryxLastStatusCode": ksGenKryxLastStatusCode,
       "ksGenKryxLastStatusText": ksGenKryxLastStatusText,
       "ksGeneralTraps": ksGeneralTraps,
       "ksGenKryxClientConnectedTrap": ksGenKryxClientConnectedTrap,
       "ksGenKryxServerConnectedTrap": ksGenKryxServerConnectedTrap,
       "ksGenKryxLastStatusCodeTrap": ksGenKryxLastStatusCodeTrap,
       "ksGenKryxLastStatusTextTrap": ksGenKryxLastStatusTextTrap,
       "ksSimCards": ksSimCards,
       "ksSimCardsTable": ksSimCardsTable,
       "ksSimCardsTableEntry": ksSimCardsTableEntry,
       "ksSimCardsTableIdx": ksSimCardsTableIdx,
       "ksSimCardsTableRowStatus": ksSimCardsTableRowStatus,
       "ksSimCardsTableCardNr": ksSimCardsTableCardNr,
       "ksSimCardsTableMkkNr": ksSimCardsTableMkkNr,
       "ksSimCardsTablePort": ksSimCardsTablePort,
       "ksSimCardsTableType": ksSimCardsTableType,
       "ksSimCardsTableOpta": ksSimCardsTableOpta,
       "ksSimCardsTableISSI": ksSimCardsTableISSI,
       "ksSimCardsTableForeignOpta": ksSimCardsTableForeignOpta,
       "ksSimCardsTableForeignISSI": ksSimCardsTableForeignISSI,
       "ksSimCardsTableGtsi": ksSimCardsTableGtsi,
       "ksSimCardsTableCallerItsi": ksSimCardsTableCallerItsi,
       "ksSimCardsTableCalleeItsi": ksSimCardsTableCalleeItsi,
       "ksSimCardsTableKryptoStatus": ksSimCardsTableKryptoStatus,
       "ksSimCardsTableLastStatusCode": ksSimCardsTableLastStatusCode,
       "ksSimCardsTableLastStatusText": ksSimCardsTableLastStatusText,
       "ipRadio": ipRadio,
       "iprGeneral": iprGeneral,
       "iprGenUserName": iprGenUserName,
       "iprGenVersion": iprGenVersion,
       "iprGeneralTraps": iprGeneralTraps,
       "iprGenUserNameTrap": iprGenUserNameTrap,
       "iprChannels": iprChannels,
       "iprChannelsTable": iprChannelsTable,
       "iprChannelsTableEntry": iprChannelsTableEntry,
       "iprChannelsTableIdx": iprChannelsTableIdx,
       "iprChannelsTableRowStatus": iprChannelsTableRowStatus,
       "iprChannelsTableID": iprChannelsTableID,
       "iprChannelsTableRegistered": iprChannelsTableRegistered,
       "iprChannelsTableState": iprChannelsTableState,
       "iprChannelsTableISSI": iprChannelsTableISSI,
       "iprChannelsTableGSSI": iprChannelsTableGSSI,
       "iprChannelsTraps": iprChannelsTraps,
       "iprChannelsRegisteredTrap": iprChannelsRegisteredTrap,
       "iprChannelsStateTrap": iprChannelsStateTrap}
)
