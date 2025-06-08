# SNMP MIB module (SIGUR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/sigur_56627/SIGUR-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:57:19 2025
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
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SigurProduct_ObjectIdentity = ObjectIdentity
sigurProduct = _SigurProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56627)
)
_Controllers_ObjectIdentity = ObjectIdentity
controllers = _Controllers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56627, 1)
)
_Informs_ObjectIdentity = ObjectIdentity
informs = _Informs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56627, 1, 0)
)


class _SerialNumber_Type(OctetString):
    """Custom type serialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SerialNumber_Type.__name__ = "OctetString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 1),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_OsdpReaderStateTable_Object = MibTable
osdpReaderStateTable = _OsdpReaderStateTable_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 2)
)
if mibBuilder.loadTexts:
    osdpReaderStateTable.setStatus("current")
_OsdpReaderStateEntry_Object = MibTableRow
osdpReaderStateEntry = _OsdpReaderStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 2, 1)
)
osdpReaderStateEntry.setIndexNames(
    (0, "SIGUR-MIB", "osdpNumber"),
)
if mibBuilder.loadTexts:
    osdpReaderStateEntry.setStatus("current")
_OsdpNumber_Type = Counter32
_OsdpNumber_Object = MibTableColumn
osdpNumber = _OsdpNumber_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 2, 1, 1),
    _OsdpNumber_Type()
)
osdpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpNumber.setStatus("current")


class _OsdpState_Type(Integer32):
    """Custom type osdpState based on Integer32"""
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
        *(("Unknown", 0),
          ("NotConfigured", 1),
          ("Misconfigured", 2),
          ("Offline", 3),
          ("Online", 4),
          ("Unencrypted", 5))
    )


_OsdpState_Type.__name__ = "Integer32"
_OsdpState_Object = MibTableColumn
osdpState = _OsdpState_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 2, 1, 2),
    _OsdpState_Type()
)
osdpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpState.setStatus("current")
_OsdpAddress_Type = Counter32
_OsdpAddress_Object = MibTableColumn
osdpAddress = _OsdpAddress_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 2, 1, 3),
    _OsdpAddress_Type()
)
osdpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpAddress.setStatus("current")
_Voltage_Type = Integer32
_Voltage_Object = MibScalar
voltage = _Voltage_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 3),
    _Voltage_Type()
)
voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage.setStatus("current")


class _FireAlarmState_Type(Integer32):
    """Custom type fireAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Unknown", 0),
          ("Fire", 1),
          ("NotFire", 2))
    )


_FireAlarmState_Type.__name__ = "Integer32"
_FireAlarmState_Object = MibScalar
fireAlarmState = _FireAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 4),
    _FireAlarmState_Type()
)
fireAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fireAlarmState.setStatus("current")
_LocalDateTime_Type = DateAndTime
_LocalDateTime_Object = MibScalar
localDateTime = _LocalDateTime_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 5),
    _LocalDateTime_Type()
)
localDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localDateTime.setStatus("current")


class _BatteryOperation_Type(Integer32):
    """Custom type batteryOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Unknown", 0),
          ("Charging", 1),
          ("EmergencyPower", 2))
    )


_BatteryOperation_Type.__name__ = "Integer32"
_BatteryOperation_Object = MibScalar
batteryOperation = _BatteryOperation_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 6),
    _BatteryOperation_Type()
)
batteryOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryOperation.setStatus("current")


class _TamperState_Type(Integer32):
    """Custom type tamperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Unknown", 0),
          ("Normal", 1),
          ("BreakIn", 2))
    )


_TamperState_Type.__name__ = "Integer32"
_TamperState_Object = MibScalar
tamperState = _TamperState_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 7),
    _TamperState_Type()
)
tamperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tamperState.setStatus("current")
_IoPortStateTable_Object = MibTable
ioPortStateTable = _IoPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 8)
)
if mibBuilder.loadTexts:
    ioPortStateTable.setStatus("current")
_IoPortStateEntry_Object = MibTableRow
ioPortStateEntry = _IoPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 8, 1)
)
ioPortStateEntry.setIndexNames(
    (0, "SIGUR-MIB", "accessPoint"),
)
if mibBuilder.loadTexts:
    ioPortStateEntry.setStatus("current")
_AccessPoint_Type = Integer32
_AccessPoint_Object = MibTableColumn
accessPoint = _AccessPoint_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 8, 1, 1),
    _AccessPoint_Type()
)
accessPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessPoint.setStatus("current")


class _Function_Type(Integer32):
    """Custom type function based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-3,
              -2,
              -1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68)
        )
    )
    namedValues = NamedValues(
        *(("liReaderUn", -3),
          ("liReaderIn", -2),
          ("liReaderOut", -1),
          ("Unknown", 0),
          ("liTurnstilePanelA", 1),
          ("liTurnstilePanelB", 2),
          ("liTurnstilePanelL", 3),
          ("loTurnstileIndA", 4),
          ("loTurnstileIndB", 5),
          ("loTurnstileIndL", 6),
          ("liTurnstileDetA", 7),
          ("liTurnstileDetB", 8),
          ("loTurnstileCntlA", 9),
          ("loTurnstileCntlB", 10),
          ("loTurnstileCntlL", 11),
          ("liDoorDet", 12),
          ("liDoorRteA", 13),
          ("liDoorRteB", 14),
          ("liDoorRteX", 15),
          ("liDoorLock", 16),
          ("loDoorLock", 17),
          ("loDoorUnlock", 18),
          ("liGateDetA", 19),
          ("liGateDetB", 20),
          ("liGateDetC", 21),
          ("liGatePanelM", 22),
          ("liGatePanelS", 23),
          ("loOprAllowed", 24),
          ("loOprDeny", 25),
          ("liFire", 26),
          ("liOpd", 27),
          ("loBreakAlarm", 28),
          ("liRegDetA", 29),
          ("liRegDetB", 30),
          ("liTurnstileDetX", 31),
          ("loImpAllowA", 32),
          ("loImpAllowB", 33),
          ("loImpDenyA", 34),
          ("loImpDenyB", 35),
          ("liReqmngstateNormal", 36),
          ("liReqmngstateLock", 37),
          ("liReqmngstateUnlock", 38),
          ("loAlmNormal", 39),
          ("loAlmAlarm", 40),
          ("loDoorHoldAlarm", 41),
          ("liDcin", 42),
          ("loMngstateLock", 43),
          ("loAcceptA", 44),
          ("loAcceptB", 45),
          ("loRejectA", 46),
          ("loRejectB", 47),
          ("loMngstateUnlock", 48),
          ("loPowerMain", 49),
          ("loPowerStandby", 50),
          ("loTraflightA", 51),
          ("loTraflightB", 52),
          ("loCardinpocket", 53),
          ("loLedc", 54),
          ("loWaitingAlkoA", 55),
          ("loWaitingAlkoB", 56),
          ("liSurpressalko", 57),
          ("liHallsensor", 58),
          ("loWaitingEscortA", 59),
          ("loWaitingEscortB", 60),
          ("loGateOpen", 61),
          ("loGateClose", 62),
          ("loGateStop", 63),
          ("loGateOpen2", 64),
          ("loGateClose2", 65),
          ("liGateDd", 66),
          ("liGateDu", 67),
          ("liResetPeopleCnt", 68))
    )


_Function_Type.__name__ = "Integer32"
_Function_Object = MibTableColumn
function = _Function_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 8, 1, 2),
    _Function_Type()
)
function.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    function.setStatus("current")


class _PhysicalPin_Type(Integer32):
    """Custom type physicalPin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-4,
              -3,
              -2,
              -1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38)
        )
    )
    namedValues = NamedValues(
        *(("port4", -4),
          ("port3", -3),
          ("port2", -2),
          ("port1", -1),
          ("portDet1Pass1", 0),
          ("portDet2Pass2", 1),
          ("portDet3Rte1", 2),
          ("portDet4Rte2", 3),
          ("portDet5StopPass3", 4),
          ("portDet6Pass4", 5),
          ("portDet7Rte3", 6),
          ("portDet8Rte4", 7),
          ("portDet9Auxin1", 8),
          ("portDet10Auxin2", 9),
          ("portOpd", 10),
          ("portFire", 11),
          ("portDcd", 12),
          ("portK1", 13),
          ("portK2", 14),
          ("portK3", 15),
          ("portK4", 16),
          ("portOut1Auxout1", 17),
          ("portOut2Auxout2", 18),
          ("portOut3", 19),
          ("portOut4", 20),
          ("portOut5", 21),
          ("portL1ALed1", 22),
          ("portL1B", 23),
          ("portL2ALed2", 24),
          ("portL2B", 25),
          ("portL3A", 26),
          ("portL3B", 27),
          ("portL4A", 28),
          ("portL4B", 29),
          ("portCpi1", 30),
          ("portCpi2", 31),
          ("portCpi3", 32),
          ("portLedrx", 33),
          ("portLedtx", 34),
          ("portLedpwr", 35),
          ("portSnd", 36),
          ("portRst", 37),
          ("portBat", 38))
    )


_PhysicalPin_Type.__name__ = "Integer32"
_PhysicalPin_Object = MibTableColumn
physicalPin = _PhysicalPin_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 8, 1, 3),
    _PhysicalPin_Type()
)
physicalPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPin.setStatus("current")


class _PortState_Type(Integer32):
    """Custom type portState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Unknown", 0),
          ("Inactive", 1),
          ("Active", 2))
    )


_PortState_Type.__name__ = "Integer32"
_PortState_Object = MibTableColumn
portState = _PortState_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 8, 1, 4),
    _PortState_Type()
)
portState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portState.setStatus("current")


class _Direction_Type(Integer32):
    """Custom type direction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Unknown", 0),
          ("Input", 1),
          ("Output", 2))
    )


_Direction_Type.__name__ = "Integer32"
_Direction_Object = MibTableColumn
direction = _Direction_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 8, 1, 5),
    _Direction_Type()
)
direction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    direction.setStatus("current")


class _ActiveState_Type(Integer32):
    """Custom type activeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Normal", 0),
          ("Inverted", 1))
    )


_ActiveState_Type.__name__ = "Integer32"
_ActiveState_Object = MibScalar
activeState = _ActiveState_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 8, 1, 6),
    _ActiveState_Type()
)
activeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeState.setStatus("current")
_Temperature_Type = Integer32
_Temperature_Object = MibScalar
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 56627, 1, 9),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("current")

# Managed Objects groups


# Notification objects

fireAlarmInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 56627, 1, 0, 1)
)
if mibBuilder.loadTexts:
    fireAlarmInform.setStatus(
        "current"
    )

voltageWrongInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 56627, 1, 0, 2)
)
if mibBuilder.loadTexts:
    voltageWrongInform.setStatus(
        "current"
    )

tamperStateInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 56627, 1, 0, 3)
)
if mibBuilder.loadTexts:
    tamperStateInform.setStatus(
        "current"
    )

batteryStateInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 56627, 1, 0, 4)
)
if mibBuilder.loadTexts:
    batteryStateInform.setStatus(
        "current"
    )

breakInInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 56627, 1, 0, 5)
)
if mibBuilder.loadTexts:
    breakInInform.setStatus(
        "current"
    )

osdpReaderStateFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 56627, 1, 0, 6)
)
if mibBuilder.loadTexts:
    osdpReaderStateFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIGUR-MIB",
    **{"sigurProduct": sigurProduct,
       "controllers": controllers,
       "informs": informs,
       "fireAlarmInform": fireAlarmInform,
       "voltageWrongInform": voltageWrongInform,
       "tamperStateInform": tamperStateInform,
       "batteryStateInform": batteryStateInform,
       "breakInInform": breakInInform,
       "osdpReaderStateFail": osdpReaderStateFail,
       "serialNumber": serialNumber,
       "osdpReaderStateTable": osdpReaderStateTable,
       "osdpReaderStateEntry": osdpReaderStateEntry,
       "osdpNumber": osdpNumber,
       "osdpState": osdpState,
       "osdpAddress": osdpAddress,
       "voltage": voltage,
       "fireAlarmState": fireAlarmState,
       "localDateTime": localDateTime,
       "batteryOperation": batteryOperation,
       "tamperState": tamperState,
       "ioPortStateTable": ioPortStateTable,
       "ioPortStateEntry": ioPortStateEntry,
       "accessPoint": accessPoint,
       "function": function,
       "physicalPin": physicalPin,
       "portState": portState,
       "direction": direction,
       "activeState": activeState,
       "temperature": temperature}
)
