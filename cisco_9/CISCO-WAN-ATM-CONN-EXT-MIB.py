# SNMP MIB module (CISCO-WAN-ATM-CONN-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-WAN-ATM-CONN-EXT-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:03:15 2025
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

(cmgwIndex,) = mibBuilder.importSymbols(
    "CISCO-MEDIA-GATEWAY-MIB",
    "cmgwIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(BulkConfigResult,
 ConfigIterator) = mibBuilder.importSymbols(
    "CISCO-TC",
    "BulkConfigResult",
    "ConfigIterator")

(CiscoWanNsapAtmAddress,
 cwAtmChanCnfgEntry) = mibBuilder.importSymbols(
    "CISCO-WAN-ATM-CONN-MIB",
    "CiscoWanNsapAtmAddress",
    "cwAtmChanCnfgEntry")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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

ciscoWanAtmConnExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 320)
)
if mibBuilder.loadTexts:
    ciscoWanAtmConnExtMIB.setRevisions(
        ("2002-12-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CwAtmConnExtMibObjects_ObjectIdentity = ObjectIdentity
cwAtmConnExtMibObjects = _CwAtmConnExtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1)
)
_CwAtmChanExtConfig_ObjectIdentity = ObjectIdentity
cwAtmChanExtConfig = _CwAtmChanExtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1)
)
_CwAtmChanExtConfigTable_Object = MibTable
cwAtmChanExtConfigTable = _CwAtmChanExtConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwAtmChanExtConfigTable.setStatus("current")
_CwAtmChanExtConfigEntry_Object = MibTableRow
cwAtmChanExtConfigEntry = _CwAtmChanExtConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwAtmChanExtConfigEntry.setStatus("current")


class _CwacChanPvcType_Type(Integer32):
    """Custom type cwacChanPvcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 1),
          ("aal2", 2),
          ("aal1", 3))
    )


_CwacChanPvcType_Type.__name__ = "Integer32"
_CwacChanPvcType_Object = MibTableColumn
cwacChanPvcType = _CwacChanPvcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 1),
    _CwacChanPvcType_Type()
)
cwacChanPvcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanPvcType.setStatus("current")


class _CwacChanProtection_Type(Integer32):
    """Custom type cwacChanProtection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 2))
    )


_CwacChanProtection_Type.__name__ = "Integer32"
_CwacChanProtection_Object = MibTableColumn
cwacChanProtection = _CwacChanProtection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 2),
    _CwacChanProtection_Type()
)
cwacChanProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanProtection.setStatus("current")


class _CwacChanPreference_Type(Integer32):
    """Custom type cwacChanPreference based on Integer32"""
    defaultValue = 0

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
          ("primary", 1),
          ("secondary", 2))
    )


_CwacChanPreference_Type.__name__ = "Integer32"
_CwacChanPreference_Object = MibTableColumn
cwacChanPreference = _CwacChanPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 3),
    _CwacChanPreference_Type()
)
cwacChanPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanPreference.setStatus("current")


class _CwacChanActivityState_Type(Integer32):
    """Custom type cwacChanActivityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("active", 2),
          ("standby", 3),
          ("failed", 4))
    )


_CwacChanActivityState_Type.__name__ = "Integer32"
_CwacChanActivityState_Object = MibTableColumn
cwacChanActivityState = _CwacChanActivityState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 4),
    _CwacChanActivityState_Type()
)
cwacChanActivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacChanActivityState.setStatus("current")


class _CwacChanApplication_Type(Integer32):
    """Custom type cwacChanApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("control", 1),
          ("bearer", 2),
          ("signaling", 3))
    )


_CwacChanApplication_Type.__name__ = "Integer32"
_CwacChanApplication_Object = MibTableColumn
cwacChanApplication = _CwacChanApplication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 5),
    _CwacChanApplication_Type()
)
cwacChanApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanApplication.setStatus("current")


class _CwacChanFallbackPort_Type(InterfaceIndexOrZero):
    """Custom type cwacChanFallbackPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_CwacChanFallbackPort_Type.__name__ = "InterfaceIndexOrZero"
_CwacChanFallbackPort_Object = MibTableColumn
cwacChanFallbackPort = _CwacChanFallbackPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 6),
    _CwacChanFallbackPort_Type()
)
cwacChanFallbackPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanFallbackPort.setStatus("current")


class _CwacChanFallbackVpi_Type(Integer32):
    """Custom type cwacChanFallbackVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwacChanFallbackVpi_Type.__name__ = "Integer32"
_CwacChanFallbackVpi_Object = MibTableColumn
cwacChanFallbackVpi = _CwacChanFallbackVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 7),
    _CwacChanFallbackVpi_Type()
)
cwacChanFallbackVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanFallbackVpi.setStatus("current")


class _CwacChanFallbackVci_Type(Integer32):
    """Custom type cwacChanFallbackVci based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwacChanFallbackVci_Type.__name__ = "Integer32"
_CwacChanFallbackVci_Object = MibTableColumn
cwacChanFallbackVci = _CwacChanFallbackVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 8),
    _CwacChanFallbackVci_Type()
)
cwacChanFallbackVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanFallbackVci.setStatus("current")


class _CwacChanFarEndAddressType_Type(AddressFamilyNumbers):
    """Custom type cwacChanFarEndAddressType based on AddressFamilyNumbers"""
    defaultValue = 0


_CwacChanFarEndAddressType_Type.__name__ = "AddressFamilyNumbers"
_CwacChanFarEndAddressType_Object = MibTableColumn
cwacChanFarEndAddressType = _CwacChanFarEndAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 9),
    _CwacChanFarEndAddressType_Type()
)
cwacChanFarEndAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanFarEndAddressType.setStatus("current")


class _CwacChanFarEndE164Address_Type(DisplayString):
    """Custom type cwacChanFarEndE164Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CwacChanFarEndE164Address_Type.__name__ = "DisplayString"
_CwacChanFarEndE164Address_Object = MibTableColumn
cwacChanFarEndE164Address = _CwacChanFarEndE164Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 10),
    _CwacChanFarEndE164Address_Type()
)
cwacChanFarEndE164Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanFarEndE164Address.setStatus("current")


class _CwacChanFarEndGWIDAddress_Type(DisplayString):
    """Custom type cwacChanFarEndGWIDAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CwacChanFarEndGWIDAddress_Type.__name__ = "DisplayString"
_CwacChanFarEndGWIDAddress_Object = MibTableColumn
cwacChanFarEndGWIDAddress = _CwacChanFarEndGWIDAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 11),
    _CwacChanFarEndGWIDAddress_Type()
)
cwacChanFarEndGWIDAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanFarEndGWIDAddress.setStatus("current")
_CwacChanFarEndNSAPAddress_Type = CiscoWanNsapAtmAddress
_CwacChanFarEndNSAPAddress_Object = MibTableColumn
cwacChanFarEndNSAPAddress = _CwacChanFarEndNSAPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 12),
    _CwacChanFarEndNSAPAddress_Type()
)
cwacChanFarEndNSAPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanFarEndNSAPAddress.setStatus("current")


class _CwacChanVCCI_Type(Integer32):
    """Custom type cwacChanVCCI based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwacChanVCCI_Type.__name__ = "Integer32"
_CwacChanVCCI_Object = MibTableColumn
cwacChanVCCI = _CwacChanVCCI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 13),
    _CwacChanVCCI_Type()
)
cwacChanVCCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanVCCI.setStatus("current")


class _CwacChanLifNum_Type(Integer32):
    """Custom type cwacChanLifNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CwacChanLifNum_Type.__name__ = "Integer32"
_CwacChanLifNum_Object = MibTableColumn
cwacChanLifNum = _CwacChanLifNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 14),
    _CwacChanLifNum_Type()
)
cwacChanLifNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanLifNum.setStatus("current")


class _CwacChanCuTimer_Type(Integer32):
    """Custom type cwacChanCuTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
        ValueRangeConstraint(255, 255),
    )


_CwacChanCuTimer_Type.__name__ = "Integer32"
_CwacChanCuTimer_Object = MibTableColumn
cwacChanCuTimer = _CwacChanCuTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 15),
    _CwacChanCuTimer_Type()
)
cwacChanCuTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanCuTimer.setStatus("current")
if mibBuilder.loadTexts:
    cwacChanCuTimer.setUnits("millisecond")


class _CwacChanCacMaster_Type(Integer32):
    """Custom type cwacChanCacMaster based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_CwacChanCacMaster_Type.__name__ = "Integer32"
_CwacChanCacMaster_Object = MibTableColumn
cwacChanCacMaster = _CwacChanCacMaster_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 16),
    _CwacChanCacMaster_Type()
)
cwacChanCacMaster.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanCacMaster.setStatus("current")


class _CwacChanVADTolerance_Type(Integer32):
    """Custom type cwacChanVADTolerance based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CwacChanVADTolerance_Type.__name__ = "Integer32"
_CwacChanVADTolerance_Object = MibTableColumn
cwacChanVADTolerance = _CwacChanVADTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 17),
    _CwacChanVADTolerance_Type()
)
cwacChanVADTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanVADTolerance.setStatus("current")
if mibBuilder.loadTexts:
    cwacChanVADTolerance.setUnits("0.0001 percent")


class _CwacChanVADDutyCycle_Type(Integer32):
    """Custom type cwacChanVADDutyCycle based on Integer32"""
    defaultValue = 61

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CwacChanVADDutyCycle_Type.__name__ = "Integer32"
_CwacChanVADDutyCycle_Object = MibTableColumn
cwacChanVADDutyCycle = _CwacChanVADDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 18),
    _CwacChanVADDutyCycle_Type()
)
cwacChanVADDutyCycle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanVADDutyCycle.setStatus("current")
if mibBuilder.loadTexts:
    cwacChanVADDutyCycle.setUnits("0.01 percent")


class _CwacChanAal2CidFillTimer_Type(Integer32):
    """Custom type cwacChanAal2CidFillTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CwacChanAal2CidFillTimer_Type.__name__ = "Integer32"
_CwacChanAal2CidFillTimer_Object = MibTableColumn
cwacChanAal2CidFillTimer = _CwacChanAal2CidFillTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 19),
    _CwacChanAal2CidFillTimer_Type()
)
cwacChanAal2CidFillTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanAal2CidFillTimer.setStatus("current")
if mibBuilder.loadTexts:
    cwacChanAal2CidFillTimer.setUnits("milliseconds")


class _CwacChanRepetition_Type(ConfigIterator):
    """Custom type cwacChanRepetition based on ConfigIterator"""
    defaultValue = 1


_CwacChanRepetition_Type.__name__ = "ConfigIterator"
_CwacChanRepetition_Object = MibTableColumn
cwacChanRepetition = _CwacChanRepetition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 20),
    _CwacChanRepetition_Type()
)
cwacChanRepetition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanRepetition.setStatus("current")
_CwacChanRepetitionOwner_Type = OwnerString
_CwacChanRepetitionOwner_Object = MibTableColumn
cwacChanRepetitionOwner = _CwacChanRepetitionOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 21),
    _CwacChanRepetitionOwner_Type()
)
cwacChanRepetitionOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwacChanRepetitionOwner.setStatus("current")
_CwacChanRepetitionResult_Type = BulkConfigResult
_CwacChanRepetitionResult_Object = MibTableColumn
cwacChanRepetitionResult = _CwacChanRepetitionResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 1, 1, 22),
    _CwacChanRepetitionResult_Type()
)
cwacChanRepetitionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacChanRepetitionResult.setStatus("current")
_CwacDualPvcTable_Object = MibTable
cwacDualPvcTable = _CwacDualPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cwacDualPvcTable.setStatus("current")
_CwacDualPvcEntry_Object = MibTableRow
cwacDualPvcEntry = _CwacDualPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 2, 1)
)
cwacDualPvcEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
)
if mibBuilder.loadTexts:
    cwacDualPvcEntry.setStatus("current")


class _CwacDualPvcOamCellGap_Type(Integer32):
    """Custom type cwacDualPvcOamCellGap based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 5000),
    )


_CwacDualPvcOamCellGap_Type.__name__ = "Integer32"
_CwacDualPvcOamCellGap_Object = MibTableColumn
cwacDualPvcOamCellGap = _CwacDualPvcOamCellGap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 2, 1, 1),
    _CwacDualPvcOamCellGap_Type()
)
cwacDualPvcOamCellGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwacDualPvcOamCellGap.setStatus("current")
if mibBuilder.loadTexts:
    cwacDualPvcOamCellGap.setUnits("millisecond")


class _CwacDualPvcRetryThreshold_Type(Integer32):
    """Custom type cwacDualPvcRetryThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CwacDualPvcRetryThreshold_Type.__name__ = "Integer32"
_CwacDualPvcRetryThreshold_Object = MibTableColumn
cwacDualPvcRetryThreshold = _CwacDualPvcRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 2, 1, 2),
    _CwacDualPvcRetryThreshold_Type()
)
cwacDualPvcRetryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwacDualPvcRetryThreshold.setStatus("current")


class _CwacDualPvcRecoverThreshold_Type(Integer32):
    """Custom type cwacDualPvcRecoverThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CwacDualPvcRecoverThreshold_Type.__name__ = "Integer32"
_CwacDualPvcRecoverThreshold_Object = MibTableColumn
cwacDualPvcRecoverThreshold = _CwacDualPvcRecoverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 1, 1, 2, 1, 3),
    _CwacDualPvcRecoverThreshold_Type()
)
cwacDualPvcRecoverThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwacDualPvcRecoverThreshold.setStatus("current")
_CwAtmConnExtMibConformance_ObjectIdentity = ObjectIdentity
cwAtmConnExtMibConformance = _CwAtmConnExtMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 2)
)
_CwAtmConnExtMibCompliances_ObjectIdentity = ObjectIdentity
cwAtmConnExtMibCompliances = _CwAtmConnExtMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 2, 1)
)
_CwAtmConnExtMibGroups_ObjectIdentity = ObjectIdentity
cwAtmConnExtMibGroups = _CwAtmConnExtMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 2, 2)
)
cwAtmChanCnfgEntry.registerAugmentions(
    ("CISCO-WAN-ATM-CONN-EXT-MIB",
     "cwAtmChanExtConfigEntry")
)
cwAtmChanExtConfigEntry.setIndexNames(*cwAtmChanCnfgEntry.getIndexNames())

# Managed Objects groups

cwacChanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 2, 2, 1)
)
cwacChanConfigGroup.setObjects(
      *(("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanPvcType"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanProtection"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanPreference"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanActivityState"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanApplication"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanFallbackPort"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanFallbackVpi"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanFallbackVci"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanFarEndAddressType"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanFarEndE164Address"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanFarEndGWIDAddress"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanFarEndNSAPAddress"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanVCCI"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanLifNum"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanCuTimer"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanCacMaster"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanVADTolerance"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanVADDutyCycle"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanAal2CidFillTimer"))
)
if mibBuilder.loadTexts:
    cwacChanConfigGroup.setStatus("current")

cwacDualPvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 2, 2, 2)
)
cwacDualPvcGroup.setObjects(
      *(("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacDualPvcOamCellGap"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacDualPvcRetryThreshold"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacDualPvcRecoverThreshold"))
)
if mibBuilder.loadTexts:
    cwacDualPvcGroup.setStatus("current")

cwacRepeatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 2, 2, 3)
)
cwacRepeatGroup.setObjects(
      *(("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanRepetition"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanRepetitionOwner"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanRepetitionResult"))
)
if mibBuilder.loadTexts:
    cwacRepeatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwAtmConnExtMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 320, 2, 1, 1)
)
cwAtmConnExtMibCompliance.setObjects(
      *(("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacChanConfigGroup"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacDualPvcGroup"),
        ("CISCO-WAN-ATM-CONN-EXT-MIB", "cwacRepeatGroup"))
)
if mibBuilder.loadTexts:
    cwAtmConnExtMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-ATM-CONN-EXT-MIB",
    **{"ciscoWanAtmConnExtMIB": ciscoWanAtmConnExtMIB,
       "cwAtmConnExtMibObjects": cwAtmConnExtMibObjects,
       "cwAtmChanExtConfig": cwAtmChanExtConfig,
       "cwAtmChanExtConfigTable": cwAtmChanExtConfigTable,
       "cwAtmChanExtConfigEntry": cwAtmChanExtConfigEntry,
       "cwacChanPvcType": cwacChanPvcType,
       "cwacChanProtection": cwacChanProtection,
       "cwacChanPreference": cwacChanPreference,
       "cwacChanActivityState": cwacChanActivityState,
       "cwacChanApplication": cwacChanApplication,
       "cwacChanFallbackPort": cwacChanFallbackPort,
       "cwacChanFallbackVpi": cwacChanFallbackVpi,
       "cwacChanFallbackVci": cwacChanFallbackVci,
       "cwacChanFarEndAddressType": cwacChanFarEndAddressType,
       "cwacChanFarEndE164Address": cwacChanFarEndE164Address,
       "cwacChanFarEndGWIDAddress": cwacChanFarEndGWIDAddress,
       "cwacChanFarEndNSAPAddress": cwacChanFarEndNSAPAddress,
       "cwacChanVCCI": cwacChanVCCI,
       "cwacChanLifNum": cwacChanLifNum,
       "cwacChanCuTimer": cwacChanCuTimer,
       "cwacChanCacMaster": cwacChanCacMaster,
       "cwacChanVADTolerance": cwacChanVADTolerance,
       "cwacChanVADDutyCycle": cwacChanVADDutyCycle,
       "cwacChanAal2CidFillTimer": cwacChanAal2CidFillTimer,
       "cwacChanRepetition": cwacChanRepetition,
       "cwacChanRepetitionOwner": cwacChanRepetitionOwner,
       "cwacChanRepetitionResult": cwacChanRepetitionResult,
       "cwacDualPvcTable": cwacDualPvcTable,
       "cwacDualPvcEntry": cwacDualPvcEntry,
       "cwacDualPvcOamCellGap": cwacDualPvcOamCellGap,
       "cwacDualPvcRetryThreshold": cwacDualPvcRetryThreshold,
       "cwacDualPvcRecoverThreshold": cwacDualPvcRecoverThreshold,
       "cwAtmConnExtMibConformance": cwAtmConnExtMibConformance,
       "cwAtmConnExtMibCompliances": cwAtmConnExtMibCompliances,
       "cwAtmConnExtMibCompliance": cwAtmConnExtMibCompliance,
       "cwAtmConnExtMibGroups": cwAtmConnExtMibGroups,
       "cwacChanConfigGroup": cwacChanConfigGroup,
       "cwacDualPvcGroup": cwacDualPvcGroup,
       "cwacRepeatGroup": cwacRepeatGroup}
)
