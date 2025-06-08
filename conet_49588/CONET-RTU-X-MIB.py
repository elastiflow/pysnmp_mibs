# SNMP MIB module (CONET-RTU-X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/conet_49588/CONET-RTU-X-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:56:15 2025
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

(conetExperimental,) = mibBuilder.importSymbols(
    "CONET-MIB",
    "conetExperimental")

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

conetRTUX = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ConetRTUXNotifications_ObjectIdentity = ObjectIdentity
conetRTUXNotifications = _ConetRTUXNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 0)
)
if mibBuilder.loadTexts:
    conetRTUXNotifications.setStatus("current")
_ConetRTUXTypes_ObjectIdentity = ObjectIdentity
conetRTUXTypes = _ConetRTUXTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 1)
)
if mibBuilder.loadTexts:
    conetRTUXTypes.setStatus("current")


class _RtuPortId_Type(OctetString):
    """Custom type rtuPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RtuPortId_Type.__name__ = "OctetString"
_RtuPortId_Object = MibScalar
rtuPortId = _RtuPortId_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 1, 1),
    _RtuPortId_Type()
)
rtuPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtuPortId.setStatus("current")
_ConetRTUXIO_ObjectIdentity = ObjectIdentity
conetRTUXIO = _ConetRTUXIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 2)
)
if mibBuilder.loadTexts:
    conetRTUXIO.setStatus("current")
_ConetIOPortStateTable_Object = MibTable
conetIOPortStateTable = _ConetIOPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 2, 1)
)
if mibBuilder.loadTexts:
    conetIOPortStateTable.setStatus("current")
_ConetIOPortStateEntry_Object = MibTableRow
conetIOPortStateEntry = _ConetIOPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 2, 1, 1)
)
conetIOPortStateEntry.setIndexNames(
    (0, "CONET-RTU-X-MIB", "psPortId"),
)
if mibBuilder.loadTexts:
    conetIOPortStateEntry.setStatus("current")


class _PsPortId_Type(OctetString):
    """Custom type psPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PsPortId_Type.__name__ = "OctetString"
_PsPortId_Object = MibTableColumn
psPortId = _PsPortId_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 2, 1, 1, 1),
    _PsPortId_Type()
)
psPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psPortId.setStatus("current")


class _PsDetection_Type(OctetString):
    """Custom type psDetection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PsDetection_Type.__name__ = "OctetString"
_PsDetection_Object = MibTableColumn
psDetection = _PsDetection_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 2, 1, 1, 2),
    _PsDetection_Type()
)
psDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDetection.setStatus("current")
_PsPeriType_Type = OctetString
_PsPeriType_Object = MibTableColumn
psPeriType = _PsPeriType_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 2, 1, 1, 3),
    _PsPeriType_Type()
)
psPeriType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPeriType.setStatus("current")
_PsValue_Type = OctetString
_PsValue_Object = MibTableColumn
psValue = _PsValue_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 2, 1, 1, 4),
    _PsValue_Type()
)
psValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psValue.setStatus("current")
_PsAlarmState_Type = OctetString
_PsAlarmState_Object = MibTableColumn
psAlarmState = _PsAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 2, 1, 1, 5),
    _PsAlarmState_Type()
)
psAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmState.setStatus("current")
_ConetRTUXSerial_ObjectIdentity = ObjectIdentity
conetRTUXSerial = _ConetRTUXSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3)
)
if mibBuilder.loadTexts:
    conetRTUXSerial.setStatus("current")
_ConetSerialPortTable_Object = MibTable
conetSerialPortTable = _ConetSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1)
)
if mibBuilder.loadTexts:
    conetSerialPortTable.setStatus("current")
_ConetSerialPortEntry_Object = MibTableRow
conetSerialPortEntry = _ConetSerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1)
)
conetSerialPortEntry.setIndexNames(
    (0, "CONET-RTU-X-MIB", "spDeviceName"),
)
if mibBuilder.loadTexts:
    conetSerialPortEntry.setStatus("current")


class _SpDeviceName_Type(OctetString):
    """Custom type spDeviceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SpDeviceName_Type.__name__ = "OctetString"
_SpDeviceName_Object = MibTableColumn
spDeviceName = _SpDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 1),
    _SpDeviceName_Type()
)
spDeviceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spDeviceName.setStatus("current")


class _SpCommand_Type(OctetString):
    """Custom type spCommand based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_SpCommand_Type.__name__ = "OctetString"
_SpCommand_Object = MibTableColumn
spCommand = _SpCommand_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 2),
    _SpCommand_Type()
)
spCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spCommand.setStatus("current")


class _SpResponse_Type(OctetString):
    """Custom type spResponse based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_SpResponse_Type.__name__ = "OctetString"
_SpResponse_Object = MibTableColumn
spResponse = _SpResponse_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 3),
    _SpResponse_Type()
)
spResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spResponse.setStatus("current")


class _SpBaudRate_Type(Integer32):
    """Custom type spBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(110, 230400),
    )


_SpBaudRate_Type.__name__ = "Integer32"
_SpBaudRate_Object = MibTableColumn
spBaudRate = _SpBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 4),
    _SpBaudRate_Type()
)
spBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spBaudRate.setStatus("current")


class _SpDataBits_Type(Integer32):
    """Custom type spDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 8),
    )


_SpDataBits_Type.__name__ = "Integer32"
_SpDataBits_Object = MibTableColumn
spDataBits = _SpDataBits_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 5),
    _SpDataBits_Type()
)
spDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spDataBits.setStatus("current")


class _SpStopBits_Type(Integer32):
    """Custom type spStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SpStopBits_Type.__name__ = "Integer32"
_SpStopBits_Object = MibTableColumn
spStopBits = _SpStopBits_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 6),
    _SpStopBits_Type()
)
spStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spStopBits.setStatus("current")


class _SpParity_Type(OctetString):
    """Custom type spParity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SpParity_Type.__name__ = "OctetString"
_SpParity_Object = MibTableColumn
spParity = _SpParity_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 7),
    _SpParity_Type()
)
spParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spParity.setStatus("current")


class _SpRTSCTS_Type(Integer32):
    """Custom type spRTSCTS based on Integer32"""
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


_SpRTSCTS_Type.__name__ = "Integer32"
_SpRTSCTS_Object = MibTableColumn
spRTSCTS = _SpRTSCTS_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 8),
    _SpRTSCTS_Type()
)
spRTSCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spRTSCTS.setStatus("current")


class _SpTCPPort_Type(Integer32):
    """Custom type spTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SpTCPPort_Type.__name__ = "Integer32"
_SpTCPPort_Object = MibTableColumn
spTCPPort = _SpTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 9),
    _SpTCPPort_Type()
)
spTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spTCPPort.setStatus("current")
_SpPortMode_Type = OctetString
_SpPortMode_Object = MibTableColumn
spPortMode = _SpPortMode_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 10),
    _SpPortMode_Type()
)
spPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spPortMode.setStatus("current")


class _SpError_Type(OctetString):
    """Custom type spError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_SpError_Type.__name__ = "OctetString"
_SpError_Object = MibTableColumn
spError = _SpError_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 11),
    _SpError_Type()
)
spError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spError.setStatus("current")


class _SpICRNL_Type(Integer32):
    """Custom type spICRNL based on Integer32"""
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


_SpICRNL_Type.__name__ = "Integer32"
_SpICRNL_Object = MibTableColumn
spICRNL = _SpICRNL_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 12),
    _SpICRNL_Type()
)
spICRNL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spICRNL.setStatus("current")


class _SpIGNCR_Type(Integer32):
    """Custom type spIGNCR based on Integer32"""
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


_SpIGNCR_Type.__name__ = "Integer32"
_SpIGNCR_Object = MibTableColumn
spIGNCR = _SpIGNCR_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 13),
    _SpIGNCR_Type()
)
spIGNCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spIGNCR.setStatus("current")


class _SpINLCR_Type(Integer32):
    """Custom type spINLCR based on Integer32"""
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


_SpINLCR_Type.__name__ = "Integer32"
_SpINLCR_Object = MibTableColumn
spINLCR = _SpINLCR_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 14),
    _SpINLCR_Type()
)
spINLCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spINLCR.setStatus("current")


class _SpOCRNL_Type(Integer32):
    """Custom type spOCRNL based on Integer32"""
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


_SpOCRNL_Type.__name__ = "Integer32"
_SpOCRNL_Object = MibTableColumn
spOCRNL = _SpOCRNL_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 15),
    _SpOCRNL_Type()
)
spOCRNL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spOCRNL.setStatus("current")


class _SpONLCR_Type(Integer32):
    """Custom type spONLCR based on Integer32"""
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


_SpONLCR_Type.__name__ = "Integer32"
_SpONLCR_Object = MibTableColumn
spONLCR = _SpONLCR_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 16),
    _SpONLCR_Type()
)
spONLCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spONLCR.setStatus("current")


class _SpONLRET_Type(Integer32):
    """Custom type spONLRET based on Integer32"""
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


_SpONLRET_Type.__name__ = "Integer32"
_SpONLRET_Object = MibTableColumn
spONLRET = _SpONLRET_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 3, 1, 1, 17),
    _SpONLRET_Type()
)
spONLRET.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spONLRET.setStatus("current")
_ConetRTUXSystem_ObjectIdentity = ObjectIdentity
conetRTUXSystem = _ConetRTUXSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 4)
)
if mibBuilder.loadTexts:
    conetRTUXSystem.setStatus("current")
_RtuSystemReboot_Type = Integer32
_RtuSystemReboot_Object = MibScalar
rtuSystemReboot = _RtuSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 4, 1),
    _RtuSystemReboot_Type()
)
rtuSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtuSystemReboot.setStatus("current")


class _RtuSystemUplink_Type(OctetString):
    """Custom type rtuSystemUplink based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RtuSystemUplink_Type.__name__ = "OctetString"
_RtuSystemUplink_Object = MibScalar
rtuSystemUplink = _RtuSystemUplink_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 4, 2),
    _RtuSystemUplink_Type()
)
rtuSystemUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtuSystemUplink.setStatus("current")


class _RtuSystemDHCP_Type(Integer32):
    """Custom type rtuSystemDHCP based on Integer32"""
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


_RtuSystemDHCP_Type.__name__ = "Integer32"
_RtuSystemDHCP_Object = MibScalar
rtuSystemDHCP = _RtuSystemDHCP_Object(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 4, 3),
    _RtuSystemDHCP_Type()
)
rtuSystemDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtuSystemDHCP.setStatus("current")

# Managed Objects groups


# Notification objects

rtuIOPortAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 49588, 9999, 2, 0, 1)
)
rtuIOPortAlarm.setObjects(
      *(("CONET-RTU-X-MIB", "rtuPortId"),
        ("CONET-RTU-X-MIB", "psValue"),
        ("CONET-RTU-X-MIB", "psAlarmState"))
)
if mibBuilder.loadTexts:
    rtuIOPortAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONET-RTU-X-MIB",
    **{"conetRTUX": conetRTUX,
       "conetRTUXNotifications": conetRTUXNotifications,
       "rtuIOPortAlarm": rtuIOPortAlarm,
       "conetRTUXTypes": conetRTUXTypes,
       "rtuPortId": rtuPortId,
       "conetRTUXIO": conetRTUXIO,
       "conetIOPortStateTable": conetIOPortStateTable,
       "conetIOPortStateEntry": conetIOPortStateEntry,
       "psPortId": psPortId,
       "psDetection": psDetection,
       "psPeriType": psPeriType,
       "psValue": psValue,
       "psAlarmState": psAlarmState,
       "conetRTUXSerial": conetRTUXSerial,
       "conetSerialPortTable": conetSerialPortTable,
       "conetSerialPortEntry": conetSerialPortEntry,
       "spDeviceName": spDeviceName,
       "spCommand": spCommand,
       "spResponse": spResponse,
       "spBaudRate": spBaudRate,
       "spDataBits": spDataBits,
       "spStopBits": spStopBits,
       "spParity": spParity,
       "spRTSCTS": spRTSCTS,
       "spTCPPort": spTCPPort,
       "spPortMode": spPortMode,
       "spError": spError,
       "spICRNL": spICRNL,
       "spIGNCR": spIGNCR,
       "spINLCR": spINLCR,
       "spOCRNL": spOCRNL,
       "spONLCR": spONLCR,
       "spONLRET": spONLRET,
       "conetRTUXSystem": conetRTUXSystem,
       "rtuSystemReboot": rtuSystemReboot,
       "rtuSystemUplink": rtuSystemUplink,
       "rtuSystemDHCP": rtuSystemDHCP}
)
