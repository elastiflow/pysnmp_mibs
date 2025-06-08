# SNMP MIB module (DIGI-MODBUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-MODBUS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:30 2025
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

(digiModbus,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiModbus")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class Switch(Integer32):
    """Custom type Switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )





class Action(Integer32):
    """Custom type Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("execute", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ModbusGlobal_ObjectIdentity = ObjectIdentity
modbusGlobal = _ModbusGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 11)
)
_GlobalStatisticsClear_Type = Action
_GlobalStatisticsClear_Object = MibScalar
globalStatisticsClear = _GlobalStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 11, 11),
    _GlobalStatisticsClear_Type()
)
globalStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalStatisticsClear.setStatus("mandatory")
_GlobalConnectionAttempts_Type = Integer32
_GlobalConnectionAttempts_Object = MibScalar
globalConnectionAttempts = _GlobalConnectionAttempts_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 11, 12),
    _GlobalConnectionAttempts_Type()
)
globalConnectionAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalConnectionAttempts.setStatus("mandatory")
_GlobalConnectionCompletes_Type = Integer32
_GlobalConnectionCompletes_Object = MibScalar
globalConnectionCompletes = _GlobalConnectionCompletes_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 11, 13),
    _GlobalConnectionCompletes_Type()
)
globalConnectionCompletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalConnectionCompletes.setStatus("mandatory")
_GlobalFailedLookups_Type = Integer32
_GlobalFailedLookups_Object = MibScalar
globalFailedLookups = _GlobalFailedLookups_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 11, 14),
    _GlobalFailedLookups_Type()
)
globalFailedLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFailedLookups.setStatus("mandatory")
_MasterDescriptor_ObjectIdentity = ObjectIdentity
masterDescriptor = _MasterDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12)
)
_MasterDescriptorSettingsTable_Object = MibTable
masterDescriptorSettingsTable = _MasterDescriptorSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11)
)
if mibBuilder.loadTexts:
    masterDescriptorSettingsTable.setStatus("mandatory")
_MasterDescriptorSettingsEntry_Object = MibTableRow
masterDescriptorSettingsEntry = _MasterDescriptorSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1)
)
masterDescriptorSettingsEntry.setIndexNames(
    (0, "DIGI-MODBUS-MIB", "masterDescriptorSettingsIndex"),
)
if mibBuilder.loadTexts:
    masterDescriptorSettingsEntry.setStatus("mandatory")
_MasterDescriptorSettingsIndex_Type = Integer32
_MasterDescriptorSettingsIndex_Object = MibTableColumn
masterDescriptorSettingsIndex = _MasterDescriptorSettingsIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1, 11),
    _MasterDescriptorSettingsIndex_Type()
)
masterDescriptorSettingsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorSettingsIndex.setStatus("mandatory")
_MasterDescriptorSettingsClear_Type = Action
_MasterDescriptorSettingsClear_Object = MibTableColumn
masterDescriptorSettingsClear = _MasterDescriptorSettingsClear_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1, 12),
    _MasterDescriptorSettingsClear_Type()
)
masterDescriptorSettingsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterDescriptorSettingsClear.setStatus("mandatory")
_MasterDescriptorSerial_Type = Switch
_MasterDescriptorSerial_Object = MibTableColumn
masterDescriptorSerial = _MasterDescriptorSerial_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1, 13),
    _MasterDescriptorSerial_Type()
)
masterDescriptorSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterDescriptorSerial.setStatus("mandatory")
_MasterDescriptorTCP_Type = Switch
_MasterDescriptorTCP_Object = MibTableColumn
masterDescriptorTCP = _MasterDescriptorTCP_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1, 14),
    _MasterDescriptorTCP_Type()
)
masterDescriptorTCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterDescriptorTCP.setStatus("mandatory")
_MasterDescriptorIPAddressStarting_Type = IpAddress
_MasterDescriptorIPAddressStarting_Object = MibTableColumn
masterDescriptorIPAddressStarting = _MasterDescriptorIPAddressStarting_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1, 15),
    _MasterDescriptorIPAddressStarting_Type()
)
masterDescriptorIPAddressStarting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterDescriptorIPAddressStarting.setStatus("mandatory")
_MasterDescriptorIPAddressEnding_Type = IpAddress
_MasterDescriptorIPAddressEnding_Object = MibTableColumn
masterDescriptorIPAddressEnding = _MasterDescriptorIPAddressEnding_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1, 16),
    _MasterDescriptorIPAddressEnding_Type()
)
masterDescriptorIPAddressEnding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterDescriptorIPAddressEnding.setStatus("mandatory")
_MasterDescriptorStartingSerialPort_Type = Integer32
_MasterDescriptorStartingSerialPort_Object = MibTableColumn
masterDescriptorStartingSerialPort = _MasterDescriptorStartingSerialPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1, 17),
    _MasterDescriptorStartingSerialPort_Type()
)
masterDescriptorStartingSerialPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterDescriptorStartingSerialPort.setStatus("mandatory")
_MasterDescriptorEndingSerialPort_Type = Integer32
_MasterDescriptorEndingSerialPort_Object = MibTableColumn
masterDescriptorEndingSerialPort = _MasterDescriptorEndingSerialPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1, 18),
    _MasterDescriptorEndingSerialPort_Type()
)
masterDescriptorEndingSerialPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterDescriptorEndingSerialPort.setStatus("mandatory")


class _MasterDescriptorFormat_Type(Integer32):
    """Custom type masterDescriptorFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtu", 1),
          ("ascii", 2))
    )


_MasterDescriptorFormat_Type.__name__ = "Integer32"
_MasterDescriptorFormat_Object = MibTableColumn
masterDescriptorFormat = _MasterDescriptorFormat_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1, 19),
    _MasterDescriptorFormat_Type()
)
masterDescriptorFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterDescriptorFormat.setStatus("mandatory")
_MasterDescriptorCloseOnError_Type = Switch
_MasterDescriptorCloseOnError_Object = MibTableColumn
masterDescriptorCloseOnError = _MasterDescriptorCloseOnError_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1, 20),
    _MasterDescriptorCloseOnError_Type()
)
masterDescriptorCloseOnError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterDescriptorCloseOnError.setStatus("mandatory")


class _MasterDescriptorBroadcastAddress_Type(Integer32):
    """Custom type masterDescriptorBroadcastAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 247),
    )


_MasterDescriptorBroadcastAddress_Type.__name__ = "Integer32"
_MasterDescriptorBroadcastAddress_Object = MibTableColumn
masterDescriptorBroadcastAddress = _MasterDescriptorBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1, 21),
    _MasterDescriptorBroadcastAddress_Type()
)
masterDescriptorBroadcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterDescriptorBroadcastAddress.setStatus("mandatory")
_MasterDescriptorCharacterTimeout_Type = Integer32
_MasterDescriptorCharacterTimeout_Object = MibTableColumn
masterDescriptorCharacterTimeout = _MasterDescriptorCharacterTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1, 22),
    _MasterDescriptorCharacterTimeout_Type()
)
masterDescriptorCharacterTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterDescriptorCharacterTimeout.setStatus("mandatory")
_MasterDescriptorTransactionTimeout_Type = Integer32
_MasterDescriptorTransactionTimeout_Object = MibTableColumn
masterDescriptorTransactionTimeout = _MasterDescriptorTransactionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1, 23),
    _MasterDescriptorTransactionTimeout_Type()
)
masterDescriptorTransactionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterDescriptorTransactionTimeout.setStatus("mandatory")
_MasterDescriptorConnectionTimeout_Type = Integer32
_MasterDescriptorConnectionTimeout_Object = MibTableColumn
masterDescriptorConnectionTimeout = _MasterDescriptorConnectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1, 24),
    _MasterDescriptorConnectionTimeout_Type()
)
masterDescriptorConnectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterDescriptorConnectionTimeout.setStatus("mandatory")
_MasterDescriptorSlaveConnections_Type = DisplayString
_MasterDescriptorSlaveConnections_Object = MibTableColumn
masterDescriptorSlaveConnections = _MasterDescriptorSlaveConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1, 25),
    _MasterDescriptorSlaveConnections_Type()
)
masterDescriptorSlaveConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterDescriptorSlaveConnections.setStatus("mandatory")
_MasterDescriptorSlaveConnectionsMap_Type = Integer32
_MasterDescriptorSlaveConnectionsMap_Object = MibTableColumn
masterDescriptorSlaveConnectionsMap = _MasterDescriptorSlaveConnectionsMap_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 11, 1, 26),
    _MasterDescriptorSlaveConnectionsMap_Type()
)
masterDescriptorSlaveConnectionsMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterDescriptorSlaveConnectionsMap.setStatus("mandatory")
_MasterDescriptorStatisticsTable_Object = MibTable
masterDescriptorStatisticsTable = _MasterDescriptorStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12)
)
if mibBuilder.loadTexts:
    masterDescriptorStatisticsTable.setStatus("mandatory")
_MasterDescriptorStatisticsEntry_Object = MibTableRow
masterDescriptorStatisticsEntry = _MasterDescriptorStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1)
)
masterDescriptorStatisticsEntry.setIndexNames(
    (0, "DIGI-MODBUS-MIB", "masterDescriptorStatisticsIndex"),
)
if mibBuilder.loadTexts:
    masterDescriptorStatisticsEntry.setStatus("mandatory")
_MasterDescriptorStatisticsIndex_Type = Integer32
_MasterDescriptorStatisticsIndex_Object = MibTableColumn
masterDescriptorStatisticsIndex = _MasterDescriptorStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 11),
    _MasterDescriptorStatisticsIndex_Type()
)
masterDescriptorStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorStatisticsIndex.setStatus("mandatory")
_MasterDescriptorStatisticsClear_Type = Action
_MasterDescriptorStatisticsClear_Object = MibTableColumn
masterDescriptorStatisticsClear = _MasterDescriptorStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 12),
    _MasterDescriptorStatisticsClear_Type()
)
masterDescriptorStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterDescriptorStatisticsClear.setStatus("mandatory")
_MasterDescriptorConnections_Type = Integer32
_MasterDescriptorConnections_Object = MibTableColumn
masterDescriptorConnections = _MasterDescriptorConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 13),
    _MasterDescriptorConnections_Type()
)
masterDescriptorConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorConnections.setStatus("mandatory")
_MasterDescriptorCompletedConnections_Type = Integer32
_MasterDescriptorCompletedConnections_Object = MibTableColumn
masterDescriptorCompletedConnections = _MasterDescriptorCompletedConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 14),
    _MasterDescriptorCompletedConnections_Type()
)
masterDescriptorCompletedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorCompletedConnections.setStatus("mandatory")
_MasterDescriptorResourceFailures_Type = Integer32
_MasterDescriptorResourceFailures_Object = MibTableColumn
masterDescriptorResourceFailures = _MasterDescriptorResourceFailures_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 15),
    _MasterDescriptorResourceFailures_Type()
)
masterDescriptorResourceFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorResourceFailures.setStatus("mandatory")
_MasterDescriptorConnectionTimeouts_Type = Integer32
_MasterDescriptorConnectionTimeouts_Object = MibTableColumn
masterDescriptorConnectionTimeouts = _MasterDescriptorConnectionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 16),
    _MasterDescriptorConnectionTimeouts_Type()
)
masterDescriptorConnectionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorConnectionTimeouts.setStatus("mandatory")
_MasterDescriptorConnectionHangups_Type = Integer32
_MasterDescriptorConnectionHangups_Object = MibTableColumn
masterDescriptorConnectionHangups = _MasterDescriptorConnectionHangups_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 17),
    _MasterDescriptorConnectionHangups_Type()
)
masterDescriptorConnectionHangups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorConnectionHangups.setStatus("mandatory")
_MasterDescriptorOpenSerialMasterFailures_Type = Integer32
_MasterDescriptorOpenSerialMasterFailures_Object = MibTableColumn
masterDescriptorOpenSerialMasterFailures = _MasterDescriptorOpenSerialMasterFailures_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 18),
    _MasterDescriptorOpenSerialMasterFailures_Type()
)
masterDescriptorOpenSerialMasterFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorOpenSerialMasterFailures.setStatus("mandatory")
_MasterDescriptorValidRequests_Type = Integer32
_MasterDescriptorValidRequests_Object = MibTableColumn
masterDescriptorValidRequests = _MasterDescriptorValidRequests_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 19),
    _MasterDescriptorValidRequests_Type()
)
masterDescriptorValidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorValidRequests.setStatus("mandatory")
_MasterDescriptorRequestCharTimeouts_Type = Integer32
_MasterDescriptorRequestCharTimeouts_Object = MibTableColumn
masterDescriptorRequestCharTimeouts = _MasterDescriptorRequestCharTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 20),
    _MasterDescriptorRequestCharTimeouts_Type()
)
masterDescriptorRequestCharTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorRequestCharTimeouts.setStatus("mandatory")
_MasterDescriptorSlaveLookupFailures_Type = Integer32
_MasterDescriptorSlaveLookupFailures_Object = MibTableColumn
masterDescriptorSlaveLookupFailures = _MasterDescriptorSlaveLookupFailures_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 21),
    _MasterDescriptorSlaveLookupFailures_Type()
)
masterDescriptorSlaveLookupFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorSlaveLookupFailures.setStatus("mandatory")
_MasterDescriptorProtocolFailures_Type = Integer32
_MasterDescriptorProtocolFailures_Object = MibTableColumn
masterDescriptorProtocolFailures = _MasterDescriptorProtocolFailures_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 22),
    _MasterDescriptorProtocolFailures_Type()
)
masterDescriptorProtocolFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorProtocolFailures.setStatus("mandatory")
_MasterDescriptorInvalidCRCRequests_Type = Integer32
_MasterDescriptorInvalidCRCRequests_Object = MibTableColumn
masterDescriptorInvalidCRCRequests = _MasterDescriptorInvalidCRCRequests_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 23),
    _MasterDescriptorInvalidCRCRequests_Type()
)
masterDescriptorInvalidCRCRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorInvalidCRCRequests.setStatus("mandatory")
_MasterDescriptorInvalidLRCRequests_Type = Integer32
_MasterDescriptorInvalidLRCRequests_Object = MibTableColumn
masterDescriptorInvalidLRCRequests = _MasterDescriptorInvalidLRCRequests_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 24),
    _MasterDescriptorInvalidLRCRequests_Type()
)
masterDescriptorInvalidLRCRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorInvalidLRCRequests.setStatus("mandatory")
_MasterDescriptorValidResponses_Type = Integer32
_MasterDescriptorValidResponses_Object = MibTableColumn
masterDescriptorValidResponses = _MasterDescriptorValidResponses_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 25),
    _MasterDescriptorValidResponses_Type()
)
masterDescriptorValidResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorValidResponses.setStatus("mandatory")
_MasterDescriptorResponseMasterHangups_Type = Integer32
_MasterDescriptorResponseMasterHangups_Object = MibTableColumn
masterDescriptorResponseMasterHangups = _MasterDescriptorResponseMasterHangups_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 26),
    _MasterDescriptorResponseMasterHangups_Type()
)
masterDescriptorResponseMasterHangups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorResponseMasterHangups.setStatus("mandatory")
_MasterDescriptorResponseTransactionTimeouts_Type = Integer32
_MasterDescriptorResponseTransactionTimeouts_Object = MibTableColumn
masterDescriptorResponseTransactionTimeouts = _MasterDescriptorResponseTransactionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 12, 12, 1, 27),
    _MasterDescriptorResponseTransactionTimeouts_Type()
)
masterDescriptorResponseTransactionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterDescriptorResponseTransactionTimeouts.setStatus("mandatory")
_SlaveDescriptor_ObjectIdentity = ObjectIdentity
slaveDescriptor = _SlaveDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13)
)
_SlaveDescriptorSettingsTable_Object = MibTable
slaveDescriptorSettingsTable = _SlaveDescriptorSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 11)
)
if mibBuilder.loadTexts:
    slaveDescriptorSettingsTable.setStatus("mandatory")
_SlaveDescriptorSettingsEntry_Object = MibTableRow
slaveDescriptorSettingsEntry = _SlaveDescriptorSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 11, 1)
)
slaveDescriptorSettingsEntry.setIndexNames(
    (0, "DIGI-MODBUS-MIB", "slaveDescriptorSettingsIndex"),
)
if mibBuilder.loadTexts:
    slaveDescriptorSettingsEntry.setStatus("mandatory")
_SlaveDescriptorSettingsIndex_Type = Integer32
_SlaveDescriptorSettingsIndex_Object = MibTableColumn
slaveDescriptorSettingsIndex = _SlaveDescriptorSettingsIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 11, 1, 11),
    _SlaveDescriptorSettingsIndex_Type()
)
slaveDescriptorSettingsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveDescriptorSettingsIndex.setStatus("mandatory")
_SlaveDescriptorSettingsClear_Type = Action
_SlaveDescriptorSettingsClear_Object = MibTableColumn
slaveDescriptorSettingsClear = _SlaveDescriptorSettingsClear_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 11, 1, 12),
    _SlaveDescriptorSettingsClear_Type()
)
slaveDescriptorSettingsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveDescriptorSettingsClear.setStatus("mandatory")
_SlaveDescriptorSerial_Type = Switch
_SlaveDescriptorSerial_Object = MibTableColumn
slaveDescriptorSerial = _SlaveDescriptorSerial_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 11, 1, 13),
    _SlaveDescriptorSerial_Type()
)
slaveDescriptorSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveDescriptorSerial.setStatus("mandatory")
_SlaveDescriptorTCP_Type = Switch
_SlaveDescriptorTCP_Object = MibTableColumn
slaveDescriptorTCP = _SlaveDescriptorTCP_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 11, 1, 14),
    _SlaveDescriptorTCP_Type()
)
slaveDescriptorTCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveDescriptorTCP.setStatus("mandatory")


class _SlaveDescriptorStartingModbusAddress_Type(Integer32):
    """Custom type slaveDescriptorStartingModbusAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlaveDescriptorStartingModbusAddress_Type.__name__ = "Integer32"
_SlaveDescriptorStartingModbusAddress_Object = MibTableColumn
slaveDescriptorStartingModbusAddress = _SlaveDescriptorStartingModbusAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 11, 1, 15),
    _SlaveDescriptorStartingModbusAddress_Type()
)
slaveDescriptorStartingModbusAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveDescriptorStartingModbusAddress.setStatus("mandatory")


class _SlaveDescriptorEndingModbusAddress_Type(Integer32):
    """Custom type slaveDescriptorEndingModbusAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlaveDescriptorEndingModbusAddress_Type.__name__ = "Integer32"
_SlaveDescriptorEndingModbusAddress_Object = MibTableColumn
slaveDescriptorEndingModbusAddress = _SlaveDescriptorEndingModbusAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 11, 1, 16),
    _SlaveDescriptorEndingModbusAddress_Type()
)
slaveDescriptorEndingModbusAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveDescriptorEndingModbusAddress.setStatus("mandatory")


class _SlaveDescriptorFixedModbusAddress_Type(Integer32):
    """Custom type slaveDescriptorFixedModbusAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlaveDescriptorFixedModbusAddress_Type.__name__ = "Integer32"
_SlaveDescriptorFixedModbusAddress_Object = MibTableColumn
slaveDescriptorFixedModbusAddress = _SlaveDescriptorFixedModbusAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 11, 1, 17),
    _SlaveDescriptorFixedModbusAddress_Type()
)
slaveDescriptorFixedModbusAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveDescriptorFixedModbusAddress.setStatus("mandatory")
_SlaveDescriptorIPAddress_Type = IpAddress
_SlaveDescriptorIPAddress_Object = MibTableColumn
slaveDescriptorIPAddress = _SlaveDescriptorIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 11, 1, 18),
    _SlaveDescriptorIPAddress_Type()
)
slaveDescriptorIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveDescriptorIPAddress.setStatus("mandatory")
_SlaveDescriptorStartingSerialPort_Type = Integer32
_SlaveDescriptorStartingSerialPort_Object = MibTableColumn
slaveDescriptorStartingSerialPort = _SlaveDescriptorStartingSerialPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 11, 1, 19),
    _SlaveDescriptorStartingSerialPort_Type()
)
slaveDescriptorStartingSerialPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveDescriptorStartingSerialPort.setStatus("mandatory")
_SlaveDescriptorEndingSerialPort_Type = Integer32
_SlaveDescriptorEndingSerialPort_Object = MibTableColumn
slaveDescriptorEndingSerialPort = _SlaveDescriptorEndingSerialPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 11, 1, 20),
    _SlaveDescriptorEndingSerialPort_Type()
)
slaveDescriptorEndingSerialPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveDescriptorEndingSerialPort.setStatus("mandatory")


class _SlaveDescriptorFormat_Type(Integer32):
    """Custom type slaveDescriptorFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtu", 1),
          ("ascii", 2))
    )


_SlaveDescriptorFormat_Type.__name__ = "Integer32"
_SlaveDescriptorFormat_Object = MibTableColumn
slaveDescriptorFormat = _SlaveDescriptorFormat_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 11, 1, 21),
    _SlaveDescriptorFormat_Type()
)
slaveDescriptorFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveDescriptorFormat.setStatus("mandatory")
_SlaveDescriptorCharacterTimeout_Type = Integer32
_SlaveDescriptorCharacterTimeout_Object = MibTableColumn
slaveDescriptorCharacterTimeout = _SlaveDescriptorCharacterTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 11, 1, 22),
    _SlaveDescriptorCharacterTimeout_Type()
)
slaveDescriptorCharacterTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveDescriptorCharacterTimeout.setStatus("mandatory")
_SlaveDescriptorTransactionTimeout_Type = Integer32
_SlaveDescriptorTransactionTimeout_Object = MibTableColumn
slaveDescriptorTransactionTimeout = _SlaveDescriptorTransactionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 11, 1, 23),
    _SlaveDescriptorTransactionTimeout_Type()
)
slaveDescriptorTransactionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveDescriptorTransactionTimeout.setStatus("mandatory")
_SlaveDescriptorStatisticsTable_Object = MibTable
slaveDescriptorStatisticsTable = _SlaveDescriptorStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12)
)
if mibBuilder.loadTexts:
    slaveDescriptorStatisticsTable.setStatus("mandatory")
_SlaveDescriptorStatisticsEntry_Object = MibTableRow
slaveDescriptorStatisticsEntry = _SlaveDescriptorStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1)
)
slaveDescriptorStatisticsEntry.setIndexNames(
    (0, "DIGI-MODBUS-MIB", "slaveDescriptorStatisticsIndex"),
)
if mibBuilder.loadTexts:
    slaveDescriptorStatisticsEntry.setStatus("mandatory")
_SlaveDescriptorStatisticsIndex_Type = Integer32
_SlaveDescriptorStatisticsIndex_Object = MibTableColumn
slaveDescriptorStatisticsIndex = _SlaveDescriptorStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1, 11),
    _SlaveDescriptorStatisticsIndex_Type()
)
slaveDescriptorStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveDescriptorStatisticsIndex.setStatus("mandatory")
_SlaveDescriptorStatisticsClear_Type = Action
_SlaveDescriptorStatisticsClear_Object = MibTableColumn
slaveDescriptorStatisticsClear = _SlaveDescriptorStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1, 12),
    _SlaveDescriptorStatisticsClear_Type()
)
slaveDescriptorStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveDescriptorStatisticsClear.setStatus("mandatory")
_SlaveDescriptorValidRequests_Type = Integer32
_SlaveDescriptorValidRequests_Object = MibTableColumn
slaveDescriptorValidRequests = _SlaveDescriptorValidRequests_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1, 13),
    _SlaveDescriptorValidRequests_Type()
)
slaveDescriptorValidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveDescriptorValidRequests.setStatus("mandatory")
_SlaveDescriptorOpenSerialSlaveFailures_Type = Integer32
_SlaveDescriptorOpenSerialSlaveFailures_Object = MibTableColumn
slaveDescriptorOpenSerialSlaveFailures = _SlaveDescriptorOpenSerialSlaveFailures_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1, 14),
    _SlaveDescriptorOpenSerialSlaveFailures_Type()
)
slaveDescriptorOpenSerialSlaveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveDescriptorOpenSerialSlaveFailures.setStatus("mandatory")
_SlaveDescriptorOpenTCPSlaveFailures_Type = Integer32
_SlaveDescriptorOpenTCPSlaveFailures_Object = MibTableColumn
slaveDescriptorOpenTCPSlaveFailures = _SlaveDescriptorOpenTCPSlaveFailures_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1, 15),
    _SlaveDescriptorOpenTCPSlaveFailures_Type()
)
slaveDescriptorOpenTCPSlaveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveDescriptorOpenTCPSlaveFailures.setStatus("mandatory")
_SlaveDescriptorRequestTransactionTimeouts_Type = Integer32
_SlaveDescriptorRequestTransactionTimeouts_Object = MibTableColumn
slaveDescriptorRequestTransactionTimeouts = _SlaveDescriptorRequestTransactionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1, 16),
    _SlaveDescriptorRequestTransactionTimeouts_Type()
)
slaveDescriptorRequestTransactionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveDescriptorRequestTransactionTimeouts.setStatus("mandatory")
_SlaveDescriptorRequestSlaveHangups_Type = Integer32
_SlaveDescriptorRequestSlaveHangups_Object = MibTableColumn
slaveDescriptorRequestSlaveHangups = _SlaveDescriptorRequestSlaveHangups_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1, 17),
    _SlaveDescriptorRequestSlaveHangups_Type()
)
slaveDescriptorRequestSlaveHangups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveDescriptorRequestSlaveHangups.setStatus("mandatory")
_SlaveDescriptorRequestTooBigFailures_Type = Integer32
_SlaveDescriptorRequestTooBigFailures_Object = MibTableColumn
slaveDescriptorRequestTooBigFailures = _SlaveDescriptorRequestTooBigFailures_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1, 18),
    _SlaveDescriptorRequestTooBigFailures_Type()
)
slaveDescriptorRequestTooBigFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveDescriptorRequestTooBigFailures.setStatus("mandatory")
_SlaveDescriptorValidResponses_Type = Integer32
_SlaveDescriptorValidResponses_Object = MibTableColumn
slaveDescriptorValidResponses = _SlaveDescriptorValidResponses_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1, 19),
    _SlaveDescriptorValidResponses_Type()
)
slaveDescriptorValidResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveDescriptorValidResponses.setStatus("mandatory")
_SlaveDescriptorResponseCharTimeouts_Type = Integer32
_SlaveDescriptorResponseCharTimeouts_Object = MibTableColumn
slaveDescriptorResponseCharTimeouts = _SlaveDescriptorResponseCharTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1, 20),
    _SlaveDescriptorResponseCharTimeouts_Type()
)
slaveDescriptorResponseCharTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveDescriptorResponseCharTimeouts.setStatus("mandatory")
_SlaveDescriptorResponseSlaveHangups_Type = Integer32
_SlaveDescriptorResponseSlaveHangups_Object = MibTableColumn
slaveDescriptorResponseSlaveHangups = _SlaveDescriptorResponseSlaveHangups_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1, 21),
    _SlaveDescriptorResponseSlaveHangups_Type()
)
slaveDescriptorResponseSlaveHangups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveDescriptorResponseSlaveHangups.setStatus("mandatory")
_SlaveDescriptorProtocolFailures_Type = Integer32
_SlaveDescriptorProtocolFailures_Object = MibTableColumn
slaveDescriptorProtocolFailures = _SlaveDescriptorProtocolFailures_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1, 22),
    _SlaveDescriptorProtocolFailures_Type()
)
slaveDescriptorProtocolFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveDescriptorProtocolFailures.setStatus("mandatory")
_SlaveDescriptorInvalidCRCResponses_Type = Integer32
_SlaveDescriptorInvalidCRCResponses_Object = MibTableColumn
slaveDescriptorInvalidCRCResponses = _SlaveDescriptorInvalidCRCResponses_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1, 23),
    _SlaveDescriptorInvalidCRCResponses_Type()
)
slaveDescriptorInvalidCRCResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveDescriptorInvalidCRCResponses.setStatus("mandatory")
_SlaveDescriptorInvalidLRCResponses_Type = Integer32
_SlaveDescriptorInvalidLRCResponses_Object = MibTableColumn
slaveDescriptorInvalidLRCResponses = _SlaveDescriptorInvalidLRCResponses_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1, 24),
    _SlaveDescriptorInvalidLRCResponses_Type()
)
slaveDescriptorInvalidLRCResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveDescriptorInvalidLRCResponses.setStatus("mandatory")
_SlaveDescriptorResponseTooBigFailures_Type = Integer32
_SlaveDescriptorResponseTooBigFailures_Object = MibTableColumn
slaveDescriptorResponseTooBigFailures = _SlaveDescriptorResponseTooBigFailures_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1, 25),
    _SlaveDescriptorResponseTooBigFailures_Type()
)
slaveDescriptorResponseTooBigFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveDescriptorResponseTooBigFailures.setStatus("mandatory")
_SlaveDescriptorResponseTransactionTimeouts_Type = Integer32
_SlaveDescriptorResponseTransactionTimeouts_Object = MibTableColumn
slaveDescriptorResponseTransactionTimeouts = _SlaveDescriptorResponseTransactionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11, 13, 12, 1, 26),
    _SlaveDescriptorResponseTransactionTimeouts_Type()
)
slaveDescriptorResponseTransactionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveDescriptorResponseTransactionTimeouts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-MODBUS-MIB",
    **{"DisplayString": DisplayString,
       "Switch": Switch,
       "Action": Action,
       "modbusGlobal": modbusGlobal,
       "globalStatisticsClear": globalStatisticsClear,
       "globalConnectionAttempts": globalConnectionAttempts,
       "globalConnectionCompletes": globalConnectionCompletes,
       "globalFailedLookups": globalFailedLookups,
       "masterDescriptor": masterDescriptor,
       "masterDescriptorSettingsTable": masterDescriptorSettingsTable,
       "masterDescriptorSettingsEntry": masterDescriptorSettingsEntry,
       "masterDescriptorSettingsIndex": masterDescriptorSettingsIndex,
       "masterDescriptorSettingsClear": masterDescriptorSettingsClear,
       "masterDescriptorSerial": masterDescriptorSerial,
       "masterDescriptorTCP": masterDescriptorTCP,
       "masterDescriptorIPAddressStarting": masterDescriptorIPAddressStarting,
       "masterDescriptorIPAddressEnding": masterDescriptorIPAddressEnding,
       "masterDescriptorStartingSerialPort": masterDescriptorStartingSerialPort,
       "masterDescriptorEndingSerialPort": masterDescriptorEndingSerialPort,
       "masterDescriptorFormat": masterDescriptorFormat,
       "masterDescriptorCloseOnError": masterDescriptorCloseOnError,
       "masterDescriptorBroadcastAddress": masterDescriptorBroadcastAddress,
       "masterDescriptorCharacterTimeout": masterDescriptorCharacterTimeout,
       "masterDescriptorTransactionTimeout": masterDescriptorTransactionTimeout,
       "masterDescriptorConnectionTimeout": masterDescriptorConnectionTimeout,
       "masterDescriptorSlaveConnections": masterDescriptorSlaveConnections,
       "masterDescriptorSlaveConnectionsMap": masterDescriptorSlaveConnectionsMap,
       "masterDescriptorStatisticsTable": masterDescriptorStatisticsTable,
       "masterDescriptorStatisticsEntry": masterDescriptorStatisticsEntry,
       "masterDescriptorStatisticsIndex": masterDescriptorStatisticsIndex,
       "masterDescriptorStatisticsClear": masterDescriptorStatisticsClear,
       "masterDescriptorConnections": masterDescriptorConnections,
       "masterDescriptorCompletedConnections": masterDescriptorCompletedConnections,
       "masterDescriptorResourceFailures": masterDescriptorResourceFailures,
       "masterDescriptorConnectionTimeouts": masterDescriptorConnectionTimeouts,
       "masterDescriptorConnectionHangups": masterDescriptorConnectionHangups,
       "masterDescriptorOpenSerialMasterFailures": masterDescriptorOpenSerialMasterFailures,
       "masterDescriptorValidRequests": masterDescriptorValidRequests,
       "masterDescriptorRequestCharTimeouts": masterDescriptorRequestCharTimeouts,
       "masterDescriptorSlaveLookupFailures": masterDescriptorSlaveLookupFailures,
       "masterDescriptorProtocolFailures": masterDescriptorProtocolFailures,
       "masterDescriptorInvalidCRCRequests": masterDescriptorInvalidCRCRequests,
       "masterDescriptorInvalidLRCRequests": masterDescriptorInvalidLRCRequests,
       "masterDescriptorValidResponses": masterDescriptorValidResponses,
       "masterDescriptorResponseMasterHangups": masterDescriptorResponseMasterHangups,
       "masterDescriptorResponseTransactionTimeouts": masterDescriptorResponseTransactionTimeouts,
       "slaveDescriptor": slaveDescriptor,
       "slaveDescriptorSettingsTable": slaveDescriptorSettingsTable,
       "slaveDescriptorSettingsEntry": slaveDescriptorSettingsEntry,
       "slaveDescriptorSettingsIndex": slaveDescriptorSettingsIndex,
       "slaveDescriptorSettingsClear": slaveDescriptorSettingsClear,
       "slaveDescriptorSerial": slaveDescriptorSerial,
       "slaveDescriptorTCP": slaveDescriptorTCP,
       "slaveDescriptorStartingModbusAddress": slaveDescriptorStartingModbusAddress,
       "slaveDescriptorEndingModbusAddress": slaveDescriptorEndingModbusAddress,
       "slaveDescriptorFixedModbusAddress": slaveDescriptorFixedModbusAddress,
       "slaveDescriptorIPAddress": slaveDescriptorIPAddress,
       "slaveDescriptorStartingSerialPort": slaveDescriptorStartingSerialPort,
       "slaveDescriptorEndingSerialPort": slaveDescriptorEndingSerialPort,
       "slaveDescriptorFormat": slaveDescriptorFormat,
       "slaveDescriptorCharacterTimeout": slaveDescriptorCharacterTimeout,
       "slaveDescriptorTransactionTimeout": slaveDescriptorTransactionTimeout,
       "slaveDescriptorStatisticsTable": slaveDescriptorStatisticsTable,
       "slaveDescriptorStatisticsEntry": slaveDescriptorStatisticsEntry,
       "slaveDescriptorStatisticsIndex": slaveDescriptorStatisticsIndex,
       "slaveDescriptorStatisticsClear": slaveDescriptorStatisticsClear,
       "slaveDescriptorValidRequests": slaveDescriptorValidRequests,
       "slaveDescriptorOpenSerialSlaveFailures": slaveDescriptorOpenSerialSlaveFailures,
       "slaveDescriptorOpenTCPSlaveFailures": slaveDescriptorOpenTCPSlaveFailures,
       "slaveDescriptorRequestTransactionTimeouts": slaveDescriptorRequestTransactionTimeouts,
       "slaveDescriptorRequestSlaveHangups": slaveDescriptorRequestSlaveHangups,
       "slaveDescriptorRequestTooBigFailures": slaveDescriptorRequestTooBigFailures,
       "slaveDescriptorValidResponses": slaveDescriptorValidResponses,
       "slaveDescriptorResponseCharTimeouts": slaveDescriptorResponseCharTimeouts,
       "slaveDescriptorResponseSlaveHangups": slaveDescriptorResponseSlaveHangups,
       "slaveDescriptorProtocolFailures": slaveDescriptorProtocolFailures,
       "slaveDescriptorInvalidCRCResponses": slaveDescriptorInvalidCRCResponses,
       "slaveDescriptorInvalidLRCResponses": slaveDescriptorInvalidLRCResponses,
       "slaveDescriptorResponseTooBigFailures": slaveDescriptorResponseTooBigFailures,
       "slaveDescriptorResponseTransactionTimeouts": slaveDescriptorResponseTransactionTimeouts}
)
