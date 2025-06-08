# SNMP MIB module (NDS-DTH3-EXTRA-SERVICES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-EXTRA-SERVICES.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:44:39 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ndsDTH3Encoder = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AddServices_ObjectIdentity = ObjectIdentity
addServices = _AddServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19)
)


class _AddServicesNoServices_Type(Integer32):
    """Custom type addServicesNoServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AddServicesNoServices_Type.__name__ = "Integer32"
_AddServicesNoServices_Object = MibScalar
addServicesNoServices = _AddServicesNoServices_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 1),
    _AddServicesNoServices_Type()
)
addServicesNoServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addServicesNoServices.setStatus("current")
_AddServicesTimeDateTable_Object = MibTable
addServicesTimeDateTable = _AddServicesTimeDateTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 2)
)
if mibBuilder.loadTexts:
    addServicesTimeDateTable.setStatus("current")
_AddServicesTimeDateEntry_Object = MibTableRow
addServicesTimeDateEntry = _AddServicesTimeDateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 2, 1)
)
addServicesTimeDateEntry.setIndexNames(
    (0, "NDS-DTH3-EXTRA-SERVICES", "addServicesTimeDateIndex"),
)
if mibBuilder.loadTexts:
    addServicesTimeDateEntry.setStatus("current")


class _AddServicesTimeDateIndex_Type(Integer32):
    """Custom type addServicesTimeDateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AddServicesTimeDateIndex_Type.__name__ = "Integer32"
_AddServicesTimeDateIndex_Object = MibTableColumn
addServicesTimeDateIndex = _AddServicesTimeDateIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 2, 1, 1),
    _AddServicesTimeDateIndex_Type()
)
addServicesTimeDateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addServicesTimeDateIndex.setStatus("current")
_AddServicesnextTimeDate_Type = DateAndTime
_AddServicesnextTimeDate_Object = MibTableColumn
addServicesnextTimeDate = _AddServicesnextTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 2, 1, 2),
    _AddServicesnextTimeDate_Type()
)
addServicesnextTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addServicesnextTimeDate.setStatus("current")
_AddServicesServiceTable_Object = MibTable
addServicesServiceTable = _AddServicesServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 3)
)
if mibBuilder.loadTexts:
    addServicesServiceTable.setStatus("current")
_AddServicesServiceEntry_Object = MibTableRow
addServicesServiceEntry = _AddServicesServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 3, 1)
)
addServicesServiceEntry.setIndexNames(
    (0, "NDS-DTH3-EXTRA-SERVICES", "addServicesCurrentNextIndex"),
    (0, "NDS-DTH3-EXTRA-SERVICES", "addServicesIndex"),
)
if mibBuilder.loadTexts:
    addServicesServiceEntry.setStatus("current")


class _AddServicesCurrentNextIndex_Type(Integer32):
    """Custom type addServicesCurrentNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index-current", 1),
          ("index-next", 2))
    )


_AddServicesCurrentNextIndex_Type.__name__ = "Integer32"
_AddServicesCurrentNextIndex_Object = MibTableColumn
addServicesCurrentNextIndex = _AddServicesCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 3, 1, 1),
    _AddServicesCurrentNextIndex_Type()
)
addServicesCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addServicesCurrentNextIndex.setStatus("current")


class _AddServicesIndex_Type(Integer32):
    """Custom type addServicesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AddServicesIndex_Type.__name__ = "Integer32"
_AddServicesIndex_Object = MibTableColumn
addServicesIndex = _AddServicesIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 3, 1, 2),
    _AddServicesIndex_Type()
)
addServicesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addServicesIndex.setStatus("current")


class _AddServicesInputServiceID_Type(Integer32):
    """Custom type addServicesInputServiceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AddServicesInputServiceID_Type.__name__ = "Integer32"
_AddServicesInputServiceID_Object = MibTableColumn
addServicesInputServiceID = _AddServicesInputServiceID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 3, 1, 3),
    _AddServicesInputServiceID_Type()
)
addServicesInputServiceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addServicesInputServiceID.setStatus("current")


class _AddServicesInputPMTPID_Type(Integer32):
    """Custom type addServicesInputPMTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 8191),
    )


_AddServicesInputPMTPID_Type.__name__ = "Integer32"
_AddServicesInputPMTPID_Object = MibTableColumn
addServicesInputPMTPID = _AddServicesInputPMTPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 3, 1, 4),
    _AddServicesInputPMTPID_Type()
)
addServicesInputPMTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addServicesInputPMTPID.setStatus("current")


class _AddServicesInputPCRPID_Type(Integer32):
    """Custom type addServicesInputPCRPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 8191),
    )


_AddServicesInputPCRPID_Type.__name__ = "Integer32"
_AddServicesInputPCRPID_Object = MibTableColumn
addServicesInputPCRPID = _AddServicesInputPCRPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 3, 1, 5),
    _AddServicesInputPCRPID_Type()
)
addServicesInputPCRPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addServicesInputPCRPID.setStatus("current")


class _AddServicesInputServiceName_Type(DisplayString):
    """Custom type addServicesInputServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AddServicesInputServiceName_Type.__name__ = "DisplayString"
_AddServicesInputServiceName_Object = MibTableColumn
addServicesInputServiceName = _AddServicesInputServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 3, 1, 6),
    _AddServicesInputServiceName_Type()
)
addServicesInputServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addServicesInputServiceName.setStatus("current")


class _AddServicesInputServiceType_Type(Integer32):
    """Custom type addServicesInputServiceType based on Integer32"""
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
        *(("digital-television-service", 0),
          ("digital-radio-service", 1),
          ("teletext-service", 2),
          ("data-broadcast-service", 3))
    )


_AddServicesInputServiceType_Type.__name__ = "Integer32"
_AddServicesInputServiceType_Object = MibTableColumn
addServicesInputServiceType = _AddServicesInputServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 3, 1, 7),
    _AddServicesInputServiceType_Type()
)
addServicesInputServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addServicesInputServiceType.setStatus("current")


class _AddServicesScrambled_Type(Integer32):
    """Custom type addServicesScrambled based on Integer32"""
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
        *(("in-the-clear", 0),
          ("ras", 1),
          ("biss-mux-key", 2),
          ("biss-mode-1", 3),
          ("biss-mode-2", 4))
    )


_AddServicesScrambled_Type.__name__ = "Integer32"
_AddServicesScrambled_Object = MibTableColumn
addServicesScrambled = _AddServicesScrambled_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 3, 1, 8),
    _AddServicesScrambled_Type()
)
addServicesScrambled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addServicesScrambled.setStatus("current")


class _AddServicesBISSSessionWord_Type(OctetString):
    """Custom type addServicesBISSSessionWord based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 7),
    )


_AddServicesBISSSessionWord_Type.__name__ = "OctetString"
_AddServicesBISSSessionWord_Object = MibTableColumn
addServicesBISSSessionWord = _AddServicesBISSSessionWord_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 3, 1, 9),
    _AddServicesBISSSessionWord_Type()
)
addServicesBISSSessionWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addServicesBISSSessionWord.setStatus("current")


class _AddServicesBISSEncryptedSessionWord_Type(OctetString):
    """Custom type addServicesBISSEncryptedSessionWord based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AddServicesBISSEncryptedSessionWord_Type.__name__ = "OctetString"
_AddServicesBISSEncryptedSessionWord_Object = MibTableColumn
addServicesBISSEncryptedSessionWord = _AddServicesBISSEncryptedSessionWord_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 3, 1, 10),
    _AddServicesBISSEncryptedSessionWord_Type()
)
addServicesBISSEncryptedSessionWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addServicesBISSEncryptedSessionWord.setStatus("current")


class _AddServicesLogicalChannel_Type(Integer32):
    """Custom type addServicesLogicalChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AddServicesLogicalChannel_Type.__name__ = "Integer32"
_AddServicesLogicalChannel_Object = MibTableColumn
addServicesLogicalChannel = _AddServicesLogicalChannel_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 3, 1, 11),
    _AddServicesLogicalChannel_Type()
)
addServicesLogicalChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addServicesLogicalChannel.setStatus("current")
_AddServicesStreamTable_Object = MibTable
addServicesStreamTable = _AddServicesStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 4)
)
if mibBuilder.loadTexts:
    addServicesStreamTable.setStatus("current")
_AddServicesStreamEntry_Object = MibTableRow
addServicesStreamEntry = _AddServicesStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 4, 1)
)
addServicesStreamEntry.setIndexNames(
    (0, "NDS-DTH3-EXTRA-SERVICES", "addServicesStreamCurrentNextIndex"),
    (0, "NDS-DTH3-EXTRA-SERVICES", "addServicesServiceIndex"),
    (0, "NDS-DTH3-EXTRA-SERVICES", "addServicesStreamIndex"),
)
if mibBuilder.loadTexts:
    addServicesStreamEntry.setStatus("current")


class _AddServicesStreamCurrentNextIndex_Type(Integer32):
    """Custom type addServicesStreamCurrentNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index-current", 1),
          ("index-next", 2))
    )


_AddServicesStreamCurrentNextIndex_Type.__name__ = "Integer32"
_AddServicesStreamCurrentNextIndex_Object = MibTableColumn
addServicesStreamCurrentNextIndex = _AddServicesStreamCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 4, 1, 1),
    _AddServicesStreamCurrentNextIndex_Type()
)
addServicesStreamCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addServicesStreamCurrentNextIndex.setStatus("current")


class _AddServicesServiceIndex_Type(Integer32):
    """Custom type addServicesServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AddServicesServiceIndex_Type.__name__ = "Integer32"
_AddServicesServiceIndex_Object = MibTableColumn
addServicesServiceIndex = _AddServicesServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 4, 1, 2),
    _AddServicesServiceIndex_Type()
)
addServicesServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addServicesServiceIndex.setStatus("current")


class _AddServicesStreamIndex_Type(Integer32):
    """Custom type addServicesStreamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_AddServicesStreamIndex_Type.__name__ = "Integer32"
_AddServicesStreamIndex_Object = MibTableColumn
addServicesStreamIndex = _AddServicesStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 4, 1, 3),
    _AddServicesStreamIndex_Type()
)
addServicesStreamIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addServicesStreamIndex.setStatus("current")


class _AddServicesStreamType_Type(Integer32):
    """Custom type addServicesStreamType based on Integer32"""
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
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pmt", 1),
          ("video", 2),
          ("mpeg-2-audio", 3),
          ("ac3-audio", 4),
          ("linear-pcm-audio", 5),
          ("mpeg-1-audio", 6),
          ("rs232", 7),
          ("rs422", 8),
          ("teletext", 9),
          ("vbi", 10),
          ("pcr", 11),
          ("private-data", 12),
          ("ecm", 13),
          ("other", 14))
    )


_AddServicesStreamType_Type.__name__ = "Integer32"
_AddServicesStreamType_Object = MibTableColumn
addServicesStreamType = _AddServicesStreamType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 4, 1, 4),
    _AddServicesStreamType_Type()
)
addServicesStreamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addServicesStreamType.setStatus("current")


class _AddServicesStreamValid_Type(Integer32):
    """Custom type addServicesStreamValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-valid", 0),
          ("valid", 1))
    )


_AddServicesStreamValid_Type.__name__ = "Integer32"
_AddServicesStreamValid_Object = MibTableColumn
addServicesStreamValid = _AddServicesStreamValid_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 4, 1, 5),
    _AddServicesStreamValid_Type()
)
addServicesStreamValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addServicesStreamValid.setStatus("current")


class _AddServicesStreamPID_Type(Integer32):
    """Custom type addServicesStreamPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_AddServicesStreamPID_Type.__name__ = "Integer32"
_AddServicesStreamPID_Object = MibTableColumn
addServicesStreamPID = _AddServicesStreamPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 4, 1, 6),
    _AddServicesStreamPID_Type()
)
addServicesStreamPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addServicesStreamPID.setStatus("current")


class _AddServicesStatus_Type(Integer32):
    """Custom type addServicesStatus based on Integer32"""
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


_AddServicesStatus_Type.__name__ = "Integer32"
_AddServicesStatus_Object = MibTableColumn
addServicesStatus = _AddServicesStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 4, 1, 7),
    _AddServicesStatus_Type()
)
addServicesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addServicesStatus.setStatus("current")


class _AddServicesPIDMapping_Type(Integer32):
    """Custom type addServicesPIDMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("duplicatePIDs", 0),
          ("uniquePerService", 1))
    )


_AddServicesPIDMapping_Type.__name__ = "Integer32"
_AddServicesPIDMapping_Object = MibScalar
addServicesPIDMapping = _AddServicesPIDMapping_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 19, 5),
    _AddServicesPIDMapping_Type()
)
addServicesPIDMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addServicesPIDMapping.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-EXTRA-SERVICES",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "addServices": addServices,
       "addServicesNoServices": addServicesNoServices,
       "addServicesTimeDateTable": addServicesTimeDateTable,
       "addServicesTimeDateEntry": addServicesTimeDateEntry,
       "addServicesTimeDateIndex": addServicesTimeDateIndex,
       "addServicesnextTimeDate": addServicesnextTimeDate,
       "addServicesServiceTable": addServicesServiceTable,
       "addServicesServiceEntry": addServicesServiceEntry,
       "addServicesCurrentNextIndex": addServicesCurrentNextIndex,
       "addServicesIndex": addServicesIndex,
       "addServicesInputServiceID": addServicesInputServiceID,
       "addServicesInputPMTPID": addServicesInputPMTPID,
       "addServicesInputPCRPID": addServicesInputPCRPID,
       "addServicesInputServiceName": addServicesInputServiceName,
       "addServicesInputServiceType": addServicesInputServiceType,
       "addServicesScrambled": addServicesScrambled,
       "addServicesBISSSessionWord": addServicesBISSSessionWord,
       "addServicesBISSEncryptedSessionWord": addServicesBISSEncryptedSessionWord,
       "addServicesLogicalChannel": addServicesLogicalChannel,
       "addServicesStreamTable": addServicesStreamTable,
       "addServicesStreamEntry": addServicesStreamEntry,
       "addServicesStreamCurrentNextIndex": addServicesStreamCurrentNextIndex,
       "addServicesServiceIndex": addServicesServiceIndex,
       "addServicesStreamIndex": addServicesStreamIndex,
       "addServicesStreamType": addServicesStreamType,
       "addServicesStreamValid": addServicesStreamValid,
       "addServicesStreamPID": addServicesStreamPID,
       "addServicesStatus": addServicesStatus,
       "addServicesPIDMapping": addServicesPIDMapping}
)
