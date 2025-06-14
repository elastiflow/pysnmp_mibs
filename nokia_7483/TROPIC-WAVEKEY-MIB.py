# SNMP MIB module (TROPIC-WAVEKEY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-WAVEKEY-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:59:16 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnCardModules,
 tnWaveKeyMIB) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnCardModules",
    "tnWaveKeyMIB")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(AluWdmDisabledEnabled,
 TnCommand,
 TnOchStatus) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmDisabledEnabled",
    "TnCommand",
    "TnOchStatus")


# MODULE-IDENTITY

tnWaveKeyMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    tnWaveKeyMibModule.setRevisions(
        ("2008-05-02 12:00",
         "2009-01-06 12:00",
         "2009-02-27 12:00",
         "2009-03-03 12:00",
         "2009-04-07 12:00",
         "2009-04-10 12:00",
         "2009-07-17 12:00",
         "2010-06-23 12:00",
         "2010-07-21 12:00",
         "2010-07-29 12:00",
         "2010-12-02 12:00",
         "2011-05-23 12:00",
         "2011-05-31 12:00",
         "2011-06-21 12:00",
         "2011-11-30 12:00",
         "2012-09-01 12:00",
         "2013-03-14 12:00",
         "2013-04-12 12:00",
         "2013-08-02 12:00",
         "2014-02-26 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnWaveKeyConf_ObjectIdentity = ObjectIdentity
tnWaveKeyConf = _TnWaveKeyConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1)
)
_TnWaveKeyGroups_ObjectIdentity = ObjectIdentity
tnWaveKeyGroups = _TnWaveKeyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 1)
)
_TnWaveKeyCompliances_ObjectIdentity = ObjectIdentity
tnWaveKeyCompliances = _TnWaveKeyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 2)
)
_TnWaveKeyObjs_ObjectIdentity = ObjectIdentity
tnWaveKeyObjs = _TnWaveKeyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2)
)
_TnWaveKeyBasics_ObjectIdentity = ObjectIdentity
tnWaveKeyBasics = _TnWaveKeyBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1)
)
_TnWaveKeyEncodeTable_Object = MibTable
tnWaveKeyEncodeTable = _TnWaveKeyEncodeTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnWaveKeyEncodeTable.setStatus("current")
_TnWaveKeyEncodeEntry_Object = MibTableRow
tnWaveKeyEncodeEntry = _TnWaveKeyEncodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 4, 1)
)
tnWaveKeyEncodeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnWaveKeyEncodeEntry.setStatus("current")


class _TnWaveKeyEncodeProgrammedWK1_Type(Unsigned32):
    """Custom type tnWaveKeyEncodeProgrammedWK1 based on Unsigned32"""
    defaultValue = 0


_TnWaveKeyEncodeProgrammedWK1_Type.__name__ = "Unsigned32"
_TnWaveKeyEncodeProgrammedWK1_Object = MibTableColumn
tnWaveKeyEncodeProgrammedWK1 = _TnWaveKeyEncodeProgrammedWK1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 4, 1, 1),
    _TnWaveKeyEncodeProgrammedWK1_Type()
)
tnWaveKeyEncodeProgrammedWK1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWaveKeyEncodeProgrammedWK1.setStatus("current")


class _TnWaveKeyEncodeProgrammedWK2_Type(Unsigned32):
    """Custom type tnWaveKeyEncodeProgrammedWK2 based on Unsigned32"""
    defaultValue = 0


_TnWaveKeyEncodeProgrammedWK2_Type.__name__ = "Unsigned32"
_TnWaveKeyEncodeProgrammedWK2_Object = MibTableColumn
tnWaveKeyEncodeProgrammedWK2 = _TnWaveKeyEncodeProgrammedWK2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 4, 1, 2),
    _TnWaveKeyEncodeProgrammedWK2_Type()
)
tnWaveKeyEncodeProgrammedWK2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWaveKeyEncodeProgrammedWK2.setStatus("current")


class _TnWaveKeyEncodeTransmitState_Type(AluWdmDisabledEnabled):
    """Custom type tnWaveKeyEncodeTransmitState based on AluWdmDisabledEnabled"""
    defaultValue = 1


_TnWaveKeyEncodeTransmitState_Type.__name__ = "AluWdmDisabledEnabled"
_TnWaveKeyEncodeTransmitState_Object = MibTableColumn
tnWaveKeyEncodeTransmitState = _TnWaveKeyEncodeTransmitState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 4, 1, 3),
    _TnWaveKeyEncodeTransmitState_Type()
)
tnWaveKeyEncodeTransmitState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWaveKeyEncodeTransmitState.setStatus("current")


class _TnWaveKeyEncodeTrailName_Type(SnmpAdminString):
    """Custom type tnWaveKeyEncodeTrailName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TnWaveKeyEncodeTrailName_Type.__name__ = "SnmpAdminString"
_TnWaveKeyEncodeTrailName_Object = MibTableColumn
tnWaveKeyEncodeTrailName = _TnWaveKeyEncodeTrailName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 4, 1, 4),
    _TnWaveKeyEncodeTrailName_Type()
)
tnWaveKeyEncodeTrailName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyEncodeTrailName.setStatus("current")
_TnWaveKeyEncodeProgrammedNwOutputPower_Type = Integer32
_TnWaveKeyEncodeProgrammedNwOutputPower_Object = MibTableColumn
tnWaveKeyEncodeProgrammedNwOutputPower = _TnWaveKeyEncodeProgrammedNwOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 4, 1, 5),
    _TnWaveKeyEncodeProgrammedNwOutputPower_Type()
)
tnWaveKeyEncodeProgrammedNwOutputPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWaveKeyEncodeProgrammedNwOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    tnWaveKeyEncodeProgrammedNwOutputPower.setUnits("mBm")


class _TnWaveKeyEncodePresentNwOutputPower_Type(Integer32):
    """Custom type tnWaveKeyEncodePresentNwOutputPower based on Integer32"""
    defaultValue = 0


_TnWaveKeyEncodePresentNwOutputPower_Type.__name__ = "Integer32"
_TnWaveKeyEncodePresentNwOutputPower_Object = MibTableColumn
tnWaveKeyEncodePresentNwOutputPower = _TnWaveKeyEncodePresentNwOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 4, 1, 6),
    _TnWaveKeyEncodePresentNwOutputPower_Type()
)
tnWaveKeyEncodePresentNwOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyEncodePresentNwOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    tnWaveKeyEncodePresentNwOutputPower.setUnits("mBm")


class _TnWaveKeyEncodeMaxAttainablePower_Type(Integer32):
    """Custom type tnWaveKeyEncodeMaxAttainablePower based on Integer32"""
    defaultValue = 0


_TnWaveKeyEncodeMaxAttainablePower_Type.__name__ = "Integer32"
_TnWaveKeyEncodeMaxAttainablePower_Object = MibTableColumn
tnWaveKeyEncodeMaxAttainablePower = _TnWaveKeyEncodeMaxAttainablePower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 4, 1, 7),
    _TnWaveKeyEncodeMaxAttainablePower_Type()
)
tnWaveKeyEncodeMaxAttainablePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyEncodeMaxAttainablePower.setStatus("current")
if mibBuilder.loadTexts:
    tnWaveKeyEncodeMaxAttainablePower.setUnits("mBm")


class _TnWaveKeyEncodeMinAttainablePower_Type(Integer32):
    """Custom type tnWaveKeyEncodeMinAttainablePower based on Integer32"""
    defaultValue = 0


_TnWaveKeyEncodeMinAttainablePower_Type.__name__ = "Integer32"
_TnWaveKeyEncodeMinAttainablePower_Object = MibTableColumn
tnWaveKeyEncodeMinAttainablePower = _TnWaveKeyEncodeMinAttainablePower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 4, 1, 8),
    _TnWaveKeyEncodeMinAttainablePower_Type()
)
tnWaveKeyEncodeMinAttainablePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyEncodeMinAttainablePower.setStatus("current")
if mibBuilder.loadTexts:
    tnWaveKeyEncodeMinAttainablePower.setUnits("mBm")


class _TnWaveKeyEncodePowerUpperMargin_Type(Unsigned32):
    """Custom type tnWaveKeyEncodePowerUpperMargin based on Unsigned32"""
    defaultValue = 0


_TnWaveKeyEncodePowerUpperMargin_Type.__name__ = "Unsigned32"
_TnWaveKeyEncodePowerUpperMargin_Object = MibTableColumn
tnWaveKeyEncodePowerUpperMargin = _TnWaveKeyEncodePowerUpperMargin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 4, 1, 9),
    _TnWaveKeyEncodePowerUpperMargin_Type()
)
tnWaveKeyEncodePowerUpperMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyEncodePowerUpperMargin.setStatus("current")
if mibBuilder.loadTexts:
    tnWaveKeyEncodePowerUpperMargin.setUnits("mB")


class _TnWaveKeyEncodePowerLowerMargin_Type(Unsigned32):
    """Custom type tnWaveKeyEncodePowerLowerMargin based on Unsigned32"""
    defaultValue = 0


_TnWaveKeyEncodePowerLowerMargin_Type.__name__ = "Unsigned32"
_TnWaveKeyEncodePowerLowerMargin_Object = MibTableColumn
tnWaveKeyEncodePowerLowerMargin = _TnWaveKeyEncodePowerLowerMargin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 4, 1, 10),
    _TnWaveKeyEncodePowerLowerMargin_Type()
)
tnWaveKeyEncodePowerLowerMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyEncodePowerLowerMargin.setStatus("current")
if mibBuilder.loadTexts:
    tnWaveKeyEncodePowerLowerMargin.setUnits("mB")
_TnWaveKeyDecodeTable_Object = MibTable
tnWaveKeyDecodeTable = _TnWaveKeyDecodeTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnWaveKeyDecodeTable.setStatus("current")
_TnWaveKeyDecodeEntry_Object = MibTableRow
tnWaveKeyDecodeEntry = _TnWaveKeyDecodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1)
)
tnWaveKeyDecodeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnWaveKeyDecodeEntry.setStatus("current")


class _TnWaveKeyDecodeSupportedDirections_Type(Integer32):
    """Custom type tnWaveKeyDecodeSupportedDirections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2),
          ("both", 3))
    )


_TnWaveKeyDecodeSupportedDirections_Type.__name__ = "Integer32"
_TnWaveKeyDecodeSupportedDirections_Object = MibTableColumn
tnWaveKeyDecodeSupportedDirections = _TnWaveKeyDecodeSupportedDirections_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 1),
    _TnWaveKeyDecodeSupportedDirections_Type()
)
tnWaveKeyDecodeSupportedDirections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeSupportedDirections.setStatus("current")


class _TnWaveKeyDecodeMinPlannedLossIn_Type(Integer32):
    """Custom type tnWaveKeyDecodeMinPlannedLossIn based on Integer32"""
    defaultValue = -9900


_TnWaveKeyDecodeMinPlannedLossIn_Type.__name__ = "Integer32"
_TnWaveKeyDecodeMinPlannedLossIn_Object = MibTableColumn
tnWaveKeyDecodeMinPlannedLossIn = _TnWaveKeyDecodeMinPlannedLossIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 6),
    _TnWaveKeyDecodeMinPlannedLossIn_Type()
)
tnWaveKeyDecodeMinPlannedLossIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeMinPlannedLossIn.setStatus("current")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeMinPlannedLossIn.setUnits("mB")


class _TnWaveKeyDecodeMinPlannedLossOut_Type(Integer32):
    """Custom type tnWaveKeyDecodeMinPlannedLossOut based on Integer32"""
    defaultValue = -9900


_TnWaveKeyDecodeMinPlannedLossOut_Type.__name__ = "Integer32"
_TnWaveKeyDecodeMinPlannedLossOut_Object = MibTableColumn
tnWaveKeyDecodeMinPlannedLossOut = _TnWaveKeyDecodeMinPlannedLossOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 7),
    _TnWaveKeyDecodeMinPlannedLossOut_Type()
)
tnWaveKeyDecodeMinPlannedLossOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeMinPlannedLossOut.setStatus("current")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeMinPlannedLossOut.setUnits("mB")


class _TnWaveKeyDecodeMaxPlannedLossIn_Type(Integer32):
    """Custom type tnWaveKeyDecodeMaxPlannedLossIn based on Integer32"""
    defaultValue = -9900


_TnWaveKeyDecodeMaxPlannedLossIn_Type.__name__ = "Integer32"
_TnWaveKeyDecodeMaxPlannedLossIn_Object = MibTableColumn
tnWaveKeyDecodeMaxPlannedLossIn = _TnWaveKeyDecodeMaxPlannedLossIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 8),
    _TnWaveKeyDecodeMaxPlannedLossIn_Type()
)
tnWaveKeyDecodeMaxPlannedLossIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeMaxPlannedLossIn.setStatus("current")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeMaxPlannedLossIn.setUnits("mB")


class _TnWaveKeyDecodeMaxPlannedLossOut_Type(Integer32):
    """Custom type tnWaveKeyDecodeMaxPlannedLossOut based on Integer32"""
    defaultValue = -9900


_TnWaveKeyDecodeMaxPlannedLossOut_Type.__name__ = "Integer32"
_TnWaveKeyDecodeMaxPlannedLossOut_Object = MibTableColumn
tnWaveKeyDecodeMaxPlannedLossOut = _TnWaveKeyDecodeMaxPlannedLossOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 9),
    _TnWaveKeyDecodeMaxPlannedLossOut_Type()
)
tnWaveKeyDecodeMaxPlannedLossOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeMaxPlannedLossOut.setStatus("current")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeMaxPlannedLossOut.setUnits("mB")


class _TnWaveKeyDecodeTypicalPlannedLossIn_Type(Integer32):
    """Custom type tnWaveKeyDecodeTypicalPlannedLossIn based on Integer32"""
    defaultValue = -9900


_TnWaveKeyDecodeTypicalPlannedLossIn_Type.__name__ = "Integer32"
_TnWaveKeyDecodeTypicalPlannedLossIn_Object = MibTableColumn
tnWaveKeyDecodeTypicalPlannedLossIn = _TnWaveKeyDecodeTypicalPlannedLossIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 10),
    _TnWaveKeyDecodeTypicalPlannedLossIn_Type()
)
tnWaveKeyDecodeTypicalPlannedLossIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeTypicalPlannedLossIn.setStatus("current")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeTypicalPlannedLossIn.setUnits("mB")


class _TnWaveKeyDecodeTypicalPlannedLossOut_Type(Integer32):
    """Custom type tnWaveKeyDecodeTypicalPlannedLossOut based on Integer32"""
    defaultValue = -9900


_TnWaveKeyDecodeTypicalPlannedLossOut_Type.__name__ = "Integer32"
_TnWaveKeyDecodeTypicalPlannedLossOut_Object = MibTableColumn
tnWaveKeyDecodeTypicalPlannedLossOut = _TnWaveKeyDecodeTypicalPlannedLossOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 11),
    _TnWaveKeyDecodeTypicalPlannedLossOut_Type()
)
tnWaveKeyDecodeTypicalPlannedLossOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeTypicalPlannedLossOut.setStatus("current")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeTypicalPlannedLossOut.setUnits("mB")


class _TnWaveKeyDecodeUpstreamLossIn_Type(Integer32):
    """Custom type tnWaveKeyDecodeUpstreamLossIn based on Integer32"""
    defaultValue = -9900


_TnWaveKeyDecodeUpstreamLossIn_Type.__name__ = "Integer32"
_TnWaveKeyDecodeUpstreamLossIn_Object = MibTableColumn
tnWaveKeyDecodeUpstreamLossIn = _TnWaveKeyDecodeUpstreamLossIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 12),
    _TnWaveKeyDecodeUpstreamLossIn_Type()
)
tnWaveKeyDecodeUpstreamLossIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeUpstreamLossIn.setStatus("current")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeUpstreamLossIn.setUnits("mB")


class _TnWaveKeyDecodeUpstreamLossOut_Type(Integer32):
    """Custom type tnWaveKeyDecodeUpstreamLossOut based on Integer32"""
    defaultValue = -9900


_TnWaveKeyDecodeUpstreamLossOut_Type.__name__ = "Integer32"
_TnWaveKeyDecodeUpstreamLossOut_Object = MibTableColumn
tnWaveKeyDecodeUpstreamLossOut = _TnWaveKeyDecodeUpstreamLossOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 13),
    _TnWaveKeyDecodeUpstreamLossOut_Type()
)
tnWaveKeyDecodeUpstreamLossOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeUpstreamLossOut.setStatus("current")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeUpstreamLossOut.setUnits("mB")
_TnWaveKeyDecodeUpstreamDetectIfIndexIn_Type = InterfaceIndex
_TnWaveKeyDecodeUpstreamDetectIfIndexIn_Object = MibTableColumn
tnWaveKeyDecodeUpstreamDetectIfIndexIn = _TnWaveKeyDecodeUpstreamDetectIfIndexIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 14),
    _TnWaveKeyDecodeUpstreamDetectIfIndexIn_Type()
)
tnWaveKeyDecodeUpstreamDetectIfIndexIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeUpstreamDetectIfIndexIn.setStatus("current")
_TnWaveKeyDecodeUpstreamDetectIfIndexOut_Type = InterfaceIndex
_TnWaveKeyDecodeUpstreamDetectIfIndexOut_Object = MibTableColumn
tnWaveKeyDecodeUpstreamDetectIfIndexOut = _TnWaveKeyDecodeUpstreamDetectIfIndexOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 15),
    _TnWaveKeyDecodeUpstreamDetectIfIndexOut_Type()
)
tnWaveKeyDecodeUpstreamDetectIfIndexOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeUpstreamDetectIfIndexOut.setStatus("current")
_TnWaveKeyDecodeInferredIn_Type = TruthValue
_TnWaveKeyDecodeInferredIn_Object = MibTableColumn
tnWaveKeyDecodeInferredIn = _TnWaveKeyDecodeInferredIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 16),
    _TnWaveKeyDecodeInferredIn_Type()
)
tnWaveKeyDecodeInferredIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeInferredIn.setStatus("current")
_TnWaveKeyDecodeInferredOut_Type = TruthValue
_TnWaveKeyDecodeInferredOut_Object = MibTableColumn
tnWaveKeyDecodeInferredOut = _TnWaveKeyDecodeInferredOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 17),
    _TnWaveKeyDecodeInferredOut_Type()
)
tnWaveKeyDecodeInferredOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeInferredOut.setStatus("current")
_TnWaveKeyDecodeModifyPowerIn_Type = TruthValue
_TnWaveKeyDecodeModifyPowerIn_Object = MibTableColumn
tnWaveKeyDecodeModifyPowerIn = _TnWaveKeyDecodeModifyPowerIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 18),
    _TnWaveKeyDecodeModifyPowerIn_Type()
)
tnWaveKeyDecodeModifyPowerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeModifyPowerIn.setStatus("current")
_TnWaveKeyDecodeModifyPowerOut_Type = TruthValue
_TnWaveKeyDecodeModifyPowerOut_Object = MibTableColumn
tnWaveKeyDecodeModifyPowerOut = _TnWaveKeyDecodeModifyPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 19),
    _TnWaveKeyDecodeModifyPowerOut_Type()
)
tnWaveKeyDecodeModifyPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeModifyPowerOut.setStatus("current")


class _TnWaveKeyDecodeCurrentUpstreamLossIn_Type(Integer32):
    """Custom type tnWaveKeyDecodeCurrentUpstreamLossIn based on Integer32"""
    defaultValue = -9900


_TnWaveKeyDecodeCurrentUpstreamLossIn_Type.__name__ = "Integer32"
_TnWaveKeyDecodeCurrentUpstreamLossIn_Object = MibTableColumn
tnWaveKeyDecodeCurrentUpstreamLossIn = _TnWaveKeyDecodeCurrentUpstreamLossIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 20),
    _TnWaveKeyDecodeCurrentUpstreamLossIn_Type()
)
tnWaveKeyDecodeCurrentUpstreamLossIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeCurrentUpstreamLossIn.setStatus("current")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeCurrentUpstreamLossIn.setUnits("mB")


class _TnWaveKeyDecodeCurrentUpstreamLossOut_Type(Integer32):
    """Custom type tnWaveKeyDecodeCurrentUpstreamLossOut based on Integer32"""
    defaultValue = -9900


_TnWaveKeyDecodeCurrentUpstreamLossOut_Type.__name__ = "Integer32"
_TnWaveKeyDecodeCurrentUpstreamLossOut_Object = MibTableColumn
tnWaveKeyDecodeCurrentUpstreamLossOut = _TnWaveKeyDecodeCurrentUpstreamLossOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 5, 1, 21),
    _TnWaveKeyDecodeCurrentUpstreamLossOut_Type()
)
tnWaveKeyDecodeCurrentUpstreamLossOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeCurrentUpstreamLossOut.setStatus("current")
if mibBuilder.loadTexts:
    tnWaveKeyDecodeCurrentUpstreamLossOut.setUnits("mB")
_TnWtEncodePortCapabilityTable_Object = MibTable
tnWtEncodePortCapabilityTable = _TnWtEncodePortCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tnWtEncodePortCapabilityTable.setStatus("current")
_TnWtEncodePortCapabilityEntry_Object = MibTableRow
tnWtEncodePortCapabilityEntry = _TnWtEncodePortCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 8, 1)
)
tnWtEncodePortCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnWtEncodePortCapabilityEntry.setStatus("current")
_TnWtEncodePortCapabilityProgrammed_Type = TruthValue
_TnWtEncodePortCapabilityProgrammed_Object = MibTableColumn
tnWtEncodePortCapabilityProgrammed = _TnWtEncodePortCapabilityProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 8, 1, 1),
    _TnWtEncodePortCapabilityProgrammed_Type()
)
tnWtEncodePortCapabilityProgrammed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWtEncodePortCapabilityProgrammed.setStatus("current")
_TnWtEncodePortCapabilityPresent_Type = TruthValue
_TnWtEncodePortCapabilityPresent_Object = MibTableColumn
tnWtEncodePortCapabilityPresent = _TnWtEncodePortCapabilityPresent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 8, 1, 2),
    _TnWtEncodePortCapabilityPresent_Type()
)
tnWtEncodePortCapabilityPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtEncodePortCapabilityPresent.setStatus("current")
_TnWtEncodePortCapabilityInUse_Type = TruthValue
_TnWtEncodePortCapabilityInUse_Object = MibTableColumn
tnWtEncodePortCapabilityInUse = _TnWtEncodePortCapabilityInUse_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 8, 1, 3),
    _TnWtEncodePortCapabilityInUse_Type()
)
tnWtEncodePortCapabilityInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtEncodePortCapabilityInUse.setStatus("current")
_TnWtEncodeCardTable_Object = MibTable
tnWtEncodeCardTable = _TnWtEncodeCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 9)
)
if mibBuilder.loadTexts:
    tnWtEncodeCardTable.setStatus("current")
_TnWtEncodeCardEntry_Object = MibTableRow
tnWtEncodeCardEntry = _TnWtEncodeCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 9, 1)
)
tnWtEncodeCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnWtEncodeCardEntry.setStatus("current")


class _TnWtEncodeCardExpectedPowerDev_Type(Unsigned32):
    """Custom type tnWtEncodeCardExpectedPowerDev based on Unsigned32"""
    defaultValue = 100


_TnWtEncodeCardExpectedPowerDev_Type.__name__ = "Unsigned32"
_TnWtEncodeCardExpectedPowerDev_Object = MibTableColumn
tnWtEncodeCardExpectedPowerDev = _TnWtEncodeCardExpectedPowerDev_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 9, 1, 1),
    _TnWtEncodeCardExpectedPowerDev_Type()
)
tnWtEncodeCardExpectedPowerDev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWtEncodeCardExpectedPowerDev.setStatus("current")
if mibBuilder.loadTexts:
    tnWtEncodeCardExpectedPowerDev.setUnits("mB")


class _TnWtEncodeCardExpectedPowerTolerance_Type(Unsigned32):
    """Custom type tnWtEncodeCardExpectedPowerTolerance based on Unsigned32"""
    defaultValue = 0


_TnWtEncodeCardExpectedPowerTolerance_Type.__name__ = "Unsigned32"
_TnWtEncodeCardExpectedPowerTolerance_Object = MibTableColumn
tnWtEncodeCardExpectedPowerTolerance = _TnWtEncodeCardExpectedPowerTolerance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 9, 1, 2),
    _TnWtEncodeCardExpectedPowerTolerance_Type()
)
tnWtEncodeCardExpectedPowerTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWtEncodeCardExpectedPowerTolerance.setStatus("current")
if mibBuilder.loadTexts:
    tnWtEncodeCardExpectedPowerTolerance.setUnits("mB")
_TnWtEncodeCardCapabilityTable_Object = MibTable
tnWtEncodeCardCapabilityTable = _TnWtEncodeCardCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 10)
)
if mibBuilder.loadTexts:
    tnWtEncodeCardCapabilityTable.setStatus("current")
_TnWtEncodeCardCapabilityEntry_Object = MibTableRow
tnWtEncodeCardCapabilityEntry = _TnWtEncodeCardCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 10, 1)
)
tnWtEncodeCardCapabilityEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnWtEncodeCardCapabilityEntry.setStatus("current")
_TnWtEncodeCardCapabilityProgrammed_Type = TruthValue
_TnWtEncodeCardCapabilityProgrammed_Object = MibTableColumn
tnWtEncodeCardCapabilityProgrammed = _TnWtEncodeCardCapabilityProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 10, 1, 1),
    _TnWtEncodeCardCapabilityProgrammed_Type()
)
tnWtEncodeCardCapabilityProgrammed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtEncodeCardCapabilityProgrammed.setStatus("current")
_TnWtEncodeCardCapabilityPresent_Type = TruthValue
_TnWtEncodeCardCapabilityPresent_Object = MibTableColumn
tnWtEncodeCardCapabilityPresent = _TnWtEncodeCardCapabilityPresent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 10, 1, 2),
    _TnWtEncodeCardCapabilityPresent_Type()
)
tnWtEncodeCardCapabilityPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtEncodeCardCapabilityPresent.setStatus("current")
_TnWtEncodeCardCapabilityInUse_Type = TruthValue
_TnWtEncodeCardCapabilityInUse_Object = MibTableColumn
tnWtEncodeCardCapabilityInUse = _TnWtEncodeCardCapabilityInUse_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 10, 1, 3),
    _TnWtEncodeCardCapabilityInUse_Type()
)
tnWtEncodeCardCapabilityInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtEncodeCardCapabilityInUse.setStatus("current")
_TnWtKeyTable_Object = MibTable
tnWtKeyTable = _TnWtKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 11)
)
if mibBuilder.loadTexts:
    tnWtKeyTable.setStatus("current")
_TnWtKeyEntry_Object = MibTableRow
tnWtKeyEntry = _TnWtKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 11, 1)
)
tnWtKeyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-WAVEKEY-MIB", "tnDirection"),
    (0, "TROPIC-WAVEKEY-MIB", "tnChannel"),
)
if mibBuilder.loadTexts:
    tnWtKeyEntry.setStatus("current")


class _TnDirection_Type(Integer32):
    """Custom type tnDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("out", 1),
          ("in", 2))
    )


_TnDirection_Type.__name__ = "Integer32"
_TnDirection_Object = MibTableColumn
tnDirection = _TnDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 11, 1, 1),
    _TnDirection_Type()
)
tnDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDirection.setStatus("current")
_TnChannel_Type = Unsigned32
_TnChannel_Object = MibTableColumn
tnChannel = _TnChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 11, 1, 2),
    _TnChannel_Type()
)
tnChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnChannel.setStatus("current")


class _TnWtKeyExpectedWK1_Type(Unsigned32):
    """Custom type tnWtKeyExpectedWK1 based on Unsigned32"""
    defaultValue = 0


_TnWtKeyExpectedWK1_Type.__name__ = "Unsigned32"
_TnWtKeyExpectedWK1_Object = MibTableColumn
tnWtKeyExpectedWK1 = _TnWtKeyExpectedWK1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 11, 1, 3),
    _TnWtKeyExpectedWK1_Type()
)
tnWtKeyExpectedWK1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWtKeyExpectedWK1.setStatus("current")


class _TnWtKeyExpectedWK2_Type(Unsigned32):
    """Custom type tnWtKeyExpectedWK2 based on Unsigned32"""
    defaultValue = 0


_TnWtKeyExpectedWK2_Type.__name__ = "Unsigned32"
_TnWtKeyExpectedWK2_Object = MibTableColumn
tnWtKeyExpectedWK2 = _TnWtKeyExpectedWK2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 11, 1, 4),
    _TnWtKeyExpectedWK2_Type()
)
tnWtKeyExpectedWK2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWtKeyExpectedWK2.setStatus("current")


class _TnWtKeyExpectedPower_Type(Integer32):
    """Custom type tnWtKeyExpectedPower based on Integer32"""
    defaultValue = -9900


_TnWtKeyExpectedPower_Type.__name__ = "Integer32"
_TnWtKeyExpectedPower_Object = MibTableColumn
tnWtKeyExpectedPower = _TnWtKeyExpectedPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 11, 1, 5),
    _TnWtKeyExpectedPower_Type()
)
tnWtKeyExpectedPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWtKeyExpectedPower.setStatus("current")
if mibBuilder.loadTexts:
    tnWtKeyExpectedPower.setUnits("mBm")


class _TnWtKeyExpectedPowerDev_Type(Unsigned32):
    """Custom type tnWtKeyExpectedPowerDev based on Unsigned32"""
    defaultValue = 250


_TnWtKeyExpectedPowerDev_Type.__name__ = "Unsigned32"
_TnWtKeyExpectedPowerDev_Object = MibTableColumn
tnWtKeyExpectedPowerDev = _TnWtKeyExpectedPowerDev_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 11, 1, 6),
    _TnWtKeyExpectedPowerDev_Type()
)
tnWtKeyExpectedPowerDev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWtKeyExpectedPowerDev.setStatus("current")
if mibBuilder.loadTexts:
    tnWtKeyExpectedPowerDev.setUnits("mB")


class _TnWtKeyPresentPower_Type(Integer32):
    """Custom type tnWtKeyPresentPower based on Integer32"""
    defaultValue = -9900


_TnWtKeyPresentPower_Type.__name__ = "Integer32"
_TnWtKeyPresentPower_Object = MibTableColumn
tnWtKeyPresentPower = _TnWtKeyPresentPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 11, 1, 7),
    _TnWtKeyPresentPower_Type()
)
tnWtKeyPresentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeyPresentPower.setStatus("current")
if mibBuilder.loadTexts:
    tnWtKeyPresentPower.setUnits("mBm")
_TnWtKeyReceived_Type = TruthValue
_TnWtKeyReceived_Object = MibTableColumn
tnWtKeyReceived = _TnWtKeyReceived_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 11, 1, 8),
    _TnWtKeyReceived_Type()
)
tnWtKeyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeyReceived.setStatus("current")


class _TnWtKeyExpectedPowerTol_Type(Unsigned32):
    """Custom type tnWtKeyExpectedPowerTol based on Unsigned32"""
    defaultValue = 0


_TnWtKeyExpectedPowerTol_Type.__name__ = "Unsigned32"
_TnWtKeyExpectedPowerTol_Object = MibTableColumn
tnWtKeyExpectedPowerTol = _TnWtKeyExpectedPowerTol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 11, 1, 9),
    _TnWtKeyExpectedPowerTol_Type()
)
tnWtKeyExpectedPowerTol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWtKeyExpectedPowerTol.setStatus("current")
if mibBuilder.loadTexts:
    tnWtKeyExpectedPowerTol.setUnits("mB")
_TnWtKeySynchronizePower_Type = TnCommand
_TnWtKeySynchronizePower_Object = MibTableColumn
tnWtKeySynchronizePower = _TnWtKeySynchronizePower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 11, 1, 10),
    _TnWtKeySynchronizePower_Type()
)
tnWtKeySynchronizePower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWtKeySynchronizePower.setStatus("current")


class _TnWtKeyTrailName_Type(SnmpAdminString):
    """Custom type tnWtKeyTrailName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TnWtKeyTrailName_Type.__name__ = "SnmpAdminString"
_TnWtKeyTrailName_Object = MibTableColumn
tnWtKeyTrailName = _TnWtKeyTrailName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 11, 1, 11),
    _TnWtKeyTrailName_Type()
)
tnWtKeyTrailName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeyTrailName.setStatus("current")


class _TnWtKeyStatus_Type(TnOchStatus):
    """Custom type tnWtKeyStatus based on TnOchStatus"""
    defaultValue = 4


_TnWtKeyStatus_Type.__name__ = "TnOchStatus"
_TnWtKeyStatus_Object = MibTableColumn
tnWtKeyStatus = _TnWtKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 11, 1, 12),
    _TnWtKeyStatus_Type()
)
tnWtKeyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeyStatus.setStatus("current")


class _TnWtKeyApplicability_Type(Integer32):
    """Custom type tnWtKeyApplicability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("applicableAndAvailable", 2),
          ("applicableAndUnavailable", 3))
    )


_TnWtKeyApplicability_Type.__name__ = "Integer32"
_TnWtKeyApplicability_Object = MibTableColumn
tnWtKeyApplicability = _TnWtKeyApplicability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 11, 1, 13),
    _TnWtKeyApplicability_Type()
)
tnWtKeyApplicability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeyApplicability.setStatus("current")
_TnUnexpectedWtKeyTable_Object = MibTable
tnUnexpectedWtKeyTable = _TnUnexpectedWtKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 12)
)
if mibBuilder.loadTexts:
    tnUnexpectedWtKeyTable.setStatus("current")
_TnUnexpectedWtKeyEntry_Object = MibTableRow
tnUnexpectedWtKeyEntry = _TnUnexpectedWtKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 12, 1)
)
tnUnexpectedWtKeyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-WAVEKEY-MIB", "tnDirection"),
    (0, "TROPIC-WAVEKEY-MIB", "tnChannel"),
    (0, "TROPIC-WAVEKEY-MIB", "tnUnexpectedWtKeyIndex"),
)
if mibBuilder.loadTexts:
    tnUnexpectedWtKeyEntry.setStatus("current")
_TnUnexpectedWtKeyIndex_Type = Unsigned32
_TnUnexpectedWtKeyIndex_Object = MibTableColumn
tnUnexpectedWtKeyIndex = _TnUnexpectedWtKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 12, 1, 1),
    _TnUnexpectedWtKeyIndex_Type()
)
tnUnexpectedWtKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnUnexpectedWtKeyIndex.setStatus("current")
_TnUnexpectedWtKey_Type = Unsigned32
_TnUnexpectedWtKey_Object = MibTableColumn
tnUnexpectedWtKey = _TnUnexpectedWtKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 12, 1, 2),
    _TnUnexpectedWtKey_Type()
)
tnUnexpectedWtKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUnexpectedWtKey.setStatus("current")
_TnUnexpectedWtKeyPower_Type = Integer32
_TnUnexpectedWtKeyPower_Object = MibTableColumn
tnUnexpectedWtKeyPower = _TnUnexpectedWtKeyPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 12, 1, 3),
    _TnUnexpectedWtKeyPower_Type()
)
tnUnexpectedWtKeyPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUnexpectedWtKeyPower.setStatus("current")
if mibBuilder.loadTexts:
    tnUnexpectedWtKeyPower.setUnits("mBm")
_TnWtKeySummaryTable_Object = MibTable
tnWtKeySummaryTable = _TnWtKeySummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 13)
)
if mibBuilder.loadTexts:
    tnWtKeySummaryTable.setStatus("current")
_TnWtKeySummaryEntry_Object = MibTableRow
tnWtKeySummaryEntry = _TnWtKeySummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 13, 1)
)
tnWtKeySummaryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnWtKeySummaryEntry.setStatus("current")
_TnWtKeySummaryExpectedWKMaskIn_Type = OctetString
_TnWtKeySummaryExpectedWKMaskIn_Object = MibTableColumn
tnWtKeySummaryExpectedWKMaskIn = _TnWtKeySummaryExpectedWKMaskIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 13, 1, 1),
    _TnWtKeySummaryExpectedWKMaskIn_Type()
)
tnWtKeySummaryExpectedWKMaskIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeySummaryExpectedWKMaskIn.setStatus("current")
_TnWtKeySummaryExpectedWKMaskOut_Type = OctetString
_TnWtKeySummaryExpectedWKMaskOut_Object = MibTableColumn
tnWtKeySummaryExpectedWKMaskOut = _TnWtKeySummaryExpectedWKMaskOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 13, 1, 2),
    _TnWtKeySummaryExpectedWKMaskOut_Type()
)
tnWtKeySummaryExpectedWKMaskOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeySummaryExpectedWKMaskOut.setStatus("current")
_TnWtKeySummaryReceivedWKMaskIn_Type = OctetString
_TnWtKeySummaryReceivedWKMaskIn_Object = MibTableColumn
tnWtKeySummaryReceivedWKMaskIn = _TnWtKeySummaryReceivedWKMaskIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 13, 1, 3),
    _TnWtKeySummaryReceivedWKMaskIn_Type()
)
tnWtKeySummaryReceivedWKMaskIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeySummaryReceivedWKMaskIn.setStatus("current")
_TnWtKeySummaryReceivedWKMaskOut_Type = OctetString
_TnWtKeySummaryReceivedWKMaskOut_Object = MibTableColumn
tnWtKeySummaryReceivedWKMaskOut = _TnWtKeySummaryReceivedWKMaskOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 13, 1, 4),
    _TnWtKeySummaryReceivedWKMaskOut_Type()
)
tnWtKeySummaryReceivedWKMaskOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeySummaryReceivedWKMaskOut.setStatus("current")
_TnWtKeySummaryUnexpectedWKMaskIn_Type = OctetString
_TnWtKeySummaryUnexpectedWKMaskIn_Object = MibTableColumn
tnWtKeySummaryUnexpectedWKMaskIn = _TnWtKeySummaryUnexpectedWKMaskIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 13, 1, 5),
    _TnWtKeySummaryUnexpectedWKMaskIn_Type()
)
tnWtKeySummaryUnexpectedWKMaskIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeySummaryUnexpectedWKMaskIn.setStatus("current")
_TnWtKeySummaryUnexpectedWKMaskOut_Type = OctetString
_TnWtKeySummaryUnexpectedWKMaskOut_Object = MibTableColumn
tnWtKeySummaryUnexpectedWKMaskOut = _TnWtKeySummaryUnexpectedWKMaskOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 13, 1, 6),
    _TnWtKeySummaryUnexpectedWKMaskOut_Type()
)
tnWtKeySummaryUnexpectedWKMaskOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeySummaryUnexpectedWKMaskOut.setStatus("current")


class _TnWtKeySummarySupportedDirections_Type(Integer32):
    """Custom type tnWtKeySummarySupportedDirections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2),
          ("both", 3))
    )


_TnWtKeySummarySupportedDirections_Type.__name__ = "Integer32"
_TnWtKeySummarySupportedDirections_Object = MibTableColumn
tnWtKeySummarySupportedDirections = _TnWtKeySummarySupportedDirections_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 13, 1, 7),
    _TnWtKeySummarySupportedDirections_Type()
)
tnWtKeySummarySupportedDirections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeySummarySupportedDirections.setStatus("current")
_TnWtKeyDecodeInfoTable_Object = MibTable
tnWtKeyDecodeInfoTable = _TnWtKeyDecodeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 14)
)
if mibBuilder.loadTexts:
    tnWtKeyDecodeInfoTable.setStatus("current")
_TnWtKeyDecodeInfoEntry_Object = MibTableRow
tnWtKeyDecodeInfoEntry = _TnWtKeyDecodeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 14, 1)
)
tnWtKeyDecodeInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnWtKeyDecodeInfoEntry.setStatus("current")


class _TnWtKeyDecodeInfoSupportedDirections_Type(Integer32):
    """Custom type tnWtKeyDecodeInfoSupportedDirections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2),
          ("both", 3))
    )


_TnWtKeyDecodeInfoSupportedDirections_Type.__name__ = "Integer32"
_TnWtKeyDecodeInfoSupportedDirections_Object = MibTableColumn
tnWtKeyDecodeInfoSupportedDirections = _TnWtKeyDecodeInfoSupportedDirections_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 14, 1, 1),
    _TnWtKeyDecodeInfoSupportedDirections_Type()
)
tnWtKeyDecodeInfoSupportedDirections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeyDecodeInfoSupportedDirections.setStatus("current")
_TnWtKeyDecodeInfoMaxSupportedExpectedPowerIn_Type = Integer32
_TnWtKeyDecodeInfoMaxSupportedExpectedPowerIn_Object = MibTableColumn
tnWtKeyDecodeInfoMaxSupportedExpectedPowerIn = _TnWtKeyDecodeInfoMaxSupportedExpectedPowerIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 14, 1, 2),
    _TnWtKeyDecodeInfoMaxSupportedExpectedPowerIn_Type()
)
tnWtKeyDecodeInfoMaxSupportedExpectedPowerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeyDecodeInfoMaxSupportedExpectedPowerIn.setStatus("current")
if mibBuilder.loadTexts:
    tnWtKeyDecodeInfoMaxSupportedExpectedPowerIn.setUnits("mBm")
_TnWtKeyDecodeInfoMaxSupportedExpectedPowerOut_Type = Integer32
_TnWtKeyDecodeInfoMaxSupportedExpectedPowerOut_Object = MibTableColumn
tnWtKeyDecodeInfoMaxSupportedExpectedPowerOut = _TnWtKeyDecodeInfoMaxSupportedExpectedPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 14, 1, 3),
    _TnWtKeyDecodeInfoMaxSupportedExpectedPowerOut_Type()
)
tnWtKeyDecodeInfoMaxSupportedExpectedPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeyDecodeInfoMaxSupportedExpectedPowerOut.setStatus("current")
if mibBuilder.loadTexts:
    tnWtKeyDecodeInfoMaxSupportedExpectedPowerOut.setUnits("mBm")
_TnWtKeyDecodeInfoMinSupportedExpectedPowerIn_Type = Integer32
_TnWtKeyDecodeInfoMinSupportedExpectedPowerIn_Object = MibTableColumn
tnWtKeyDecodeInfoMinSupportedExpectedPowerIn = _TnWtKeyDecodeInfoMinSupportedExpectedPowerIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 14, 1, 4),
    _TnWtKeyDecodeInfoMinSupportedExpectedPowerIn_Type()
)
tnWtKeyDecodeInfoMinSupportedExpectedPowerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeyDecodeInfoMinSupportedExpectedPowerIn.setStatus("current")
if mibBuilder.loadTexts:
    tnWtKeyDecodeInfoMinSupportedExpectedPowerIn.setUnits("mBm")
_TnWtKeyDecodeInfoMinSupportedExpectedPowerOut_Type = Integer32
_TnWtKeyDecodeInfoMinSupportedExpectedPowerOut_Object = MibTableColumn
tnWtKeyDecodeInfoMinSupportedExpectedPowerOut = _TnWtKeyDecodeInfoMinSupportedExpectedPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 14, 1, 5),
    _TnWtKeyDecodeInfoMinSupportedExpectedPowerOut_Type()
)
tnWtKeyDecodeInfoMinSupportedExpectedPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtKeyDecodeInfoMinSupportedExpectedPowerOut.setStatus("current")
if mibBuilder.loadTexts:
    tnWtKeyDecodeInfoMinSupportedExpectedPowerOut.setUnits("mBm")
_TnWtocmChanInfoTable_Object = MibTable
tnWtocmChanInfoTable = _TnWtocmChanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 15)
)
if mibBuilder.loadTexts:
    tnWtocmChanInfoTable.setStatus("current")
_TnWtocmChanInfoEntry_Object = MibTableRow
tnWtocmChanInfoEntry = _TnWtocmChanInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 15, 1)
)
tnWtocmChanInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-WAVEKEY-MIB", "tnChannel"),
)
if mibBuilder.loadTexts:
    tnWtocmChanInfoEntry.setStatus("current")


class _TnWtocmChanInfoExpectedWK1_Type(Unsigned32):
    """Custom type tnWtocmChanInfoExpectedWK1 based on Unsigned32"""
    defaultValue = 0


_TnWtocmChanInfoExpectedWK1_Type.__name__ = "Unsigned32"
_TnWtocmChanInfoExpectedWK1_Object = MibTableColumn
tnWtocmChanInfoExpectedWK1 = _TnWtocmChanInfoExpectedWK1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 15, 1, 1),
    _TnWtocmChanInfoExpectedWK1_Type()
)
tnWtocmChanInfoExpectedWK1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmChanInfoExpectedWK1.setStatus("current")


class _TnWtocmChanInfoExpectedWK2_Type(Unsigned32):
    """Custom type tnWtocmChanInfoExpectedWK2 based on Unsigned32"""
    defaultValue = 0


_TnWtocmChanInfoExpectedWK2_Type.__name__ = "Unsigned32"
_TnWtocmChanInfoExpectedWK2_Object = MibTableColumn
tnWtocmChanInfoExpectedWK2 = _TnWtocmChanInfoExpectedWK2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 15, 1, 2),
    _TnWtocmChanInfoExpectedWK2_Type()
)
tnWtocmChanInfoExpectedWK2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmChanInfoExpectedWK2.setStatus("current")


class _TnWtocmChanInfoPresentPower_Type(Integer32):
    """Custom type tnWtocmChanInfoPresentPower based on Integer32"""
    defaultValue = -9900


_TnWtocmChanInfoPresentPower_Type.__name__ = "Integer32"
_TnWtocmChanInfoPresentPower_Object = MibTableColumn
tnWtocmChanInfoPresentPower = _TnWtocmChanInfoPresentPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 15, 1, 3),
    _TnWtocmChanInfoPresentPower_Type()
)
tnWtocmChanInfoPresentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmChanInfoPresentPower.setStatus("current")
if mibBuilder.loadTexts:
    tnWtocmChanInfoPresentPower.setUnits("mBm")


class _TnWtocmChanInfoPresentPowerMonitoredPort_Type(Integer32):
    """Custom type tnWtocmChanInfoPresentPowerMonitoredPort based on Integer32"""
    defaultValue = -9900


_TnWtocmChanInfoPresentPowerMonitoredPort_Type.__name__ = "Integer32"
_TnWtocmChanInfoPresentPowerMonitoredPort_Object = MibTableColumn
tnWtocmChanInfoPresentPowerMonitoredPort = _TnWtocmChanInfoPresentPowerMonitoredPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 15, 1, 4),
    _TnWtocmChanInfoPresentPowerMonitoredPort_Type()
)
tnWtocmChanInfoPresentPowerMonitoredPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmChanInfoPresentPowerMonitoredPort.setStatus("current")
if mibBuilder.loadTexts:
    tnWtocmChanInfoPresentPowerMonitoredPort.setUnits("mBm")


class _TnWtocmChanInfoProcessingState_Type(Integer32):
    """Custom type tnWtocmChanInfoProcessingState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("notProvisionedAndNotPresent", 1),
          ("notProvisionedAndUnconfirmed", 2),
          ("notProvisionedAndChannelPresentNoKeys", 3),
          ("notProvisionedAndUnexpected", 4),
          ("notProvisionedAndHardwareFault", 5),
          ("provisionedAndNotPresent", 6),
          ("provisionedAndUnconfirmed", 7),
          ("provisionedAndChannelPresentNoKeys", 8),
          ("provisionedAndUnexpected", 9),
          ("provisionedWithExpectedAndUnexpected", 10),
          ("provisionedAndConfirmed", 11),
          ("provisionedAndHardwareFault", 12))
    )


_TnWtocmChanInfoProcessingState_Type.__name__ = "Integer32"
_TnWtocmChanInfoProcessingState_Object = MibTableColumn
tnWtocmChanInfoProcessingState = _TnWtocmChanInfoProcessingState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 15, 1, 6),
    _TnWtocmChanInfoProcessingState_Type()
)
tnWtocmChanInfoProcessingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmChanInfoProcessingState.setStatus("current")


class _TnWtocmChanInfoPresentOSNR_Type(Integer32):
    """Custom type tnWtocmChanInfoPresentOSNR based on Integer32"""
    defaultValue = -9900


_TnWtocmChanInfoPresentOSNR_Type.__name__ = "Integer32"
_TnWtocmChanInfoPresentOSNR_Object = MibTableColumn
tnWtocmChanInfoPresentOSNR = _TnWtocmChanInfoPresentOSNR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 15, 1, 7),
    _TnWtocmChanInfoPresentOSNR_Type()
)
tnWtocmChanInfoPresentOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmChanInfoPresentOSNR.setStatus("current")
if mibBuilder.loadTexts:
    tnWtocmChanInfoPresentOSNR.setUnits("mB")


class _TnWtocmChanInfoOSNRTimeStamp_Type(TimeStamp):
    """Custom type tnWtocmChanInfoOSNRTimeStamp based on TimeStamp"""
    defaultValue = 0


_TnWtocmChanInfoOSNRTimeStamp_Type.__name__ = "TimeStamp"
_TnWtocmChanInfoOSNRTimeStamp_Object = MibTableColumn
tnWtocmChanInfoOSNRTimeStamp = _TnWtocmChanInfoOSNRTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 15, 1, 8),
    _TnWtocmChanInfoOSNRTimeStamp_Type()
)
tnWtocmChanInfoOSNRTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmChanInfoOSNRTimeStamp.setStatus("current")
_TnWtocmChanInfoSummaryTable_Object = MibTable
tnWtocmChanInfoSummaryTable = _TnWtocmChanInfoSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 17)
)
if mibBuilder.loadTexts:
    tnWtocmChanInfoSummaryTable.setStatus("current")
_TnWtocmChanInfoSummaryEntry_Object = MibTableRow
tnWtocmChanInfoSummaryEntry = _TnWtocmChanInfoSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 17, 1)
)
tnWtocmChanInfoSummaryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnWtocmChanInfoSummaryEntry.setStatus("current")


class _TnWtocmChanInfoSummaryExpectedWKMask_Type(OctetString):
    """Custom type tnWtocmChanInfoSummaryExpectedWKMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TnWtocmChanInfoSummaryExpectedWKMask_Type.__name__ = "OctetString"
_TnWtocmChanInfoSummaryExpectedWKMask_Object = MibTableColumn
tnWtocmChanInfoSummaryExpectedWKMask = _TnWtocmChanInfoSummaryExpectedWKMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 17, 1, 1),
    _TnWtocmChanInfoSummaryExpectedWKMask_Type()
)
tnWtocmChanInfoSummaryExpectedWKMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmChanInfoSummaryExpectedWKMask.setStatus("current")


class _TnWtocmChanInfoSummaryNoLosWKMask_Type(OctetString):
    """Custom type tnWtocmChanInfoSummaryNoLosWKMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TnWtocmChanInfoSummaryNoLosWKMask_Type.__name__ = "OctetString"
_TnWtocmChanInfoSummaryNoLosWKMask_Object = MibTableColumn
tnWtocmChanInfoSummaryNoLosWKMask = _TnWtocmChanInfoSummaryNoLosWKMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 17, 1, 2),
    _TnWtocmChanInfoSummaryNoLosWKMask_Type()
)
tnWtocmChanInfoSummaryNoLosWKMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmChanInfoSummaryNoLosWKMask.setStatus("current")


class _TnWtocmChanInfoSummaryConfirmWKMask_Type(OctetString):
    """Custom type tnWtocmChanInfoSummaryConfirmWKMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TnWtocmChanInfoSummaryConfirmWKMask_Type.__name__ = "OctetString"
_TnWtocmChanInfoSummaryConfirmWKMask_Object = MibTableColumn
tnWtocmChanInfoSummaryConfirmWKMask = _TnWtocmChanInfoSummaryConfirmWKMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 17, 1, 3),
    _TnWtocmChanInfoSummaryConfirmWKMask_Type()
)
tnWtocmChanInfoSummaryConfirmWKMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmChanInfoSummaryConfirmWKMask.setStatus("current")


class _TnWtocmChanInfoSummaryUnexpectedWKMask_Type(OctetString):
    """Custom type tnWtocmChanInfoSummaryUnexpectedWKMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TnWtocmChanInfoSummaryUnexpectedWKMask_Type.__name__ = "OctetString"
_TnWtocmChanInfoSummaryUnexpectedWKMask_Object = MibTableColumn
tnWtocmChanInfoSummaryUnexpectedWKMask = _TnWtocmChanInfoSummaryUnexpectedWKMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 17, 1, 4),
    _TnWtocmChanInfoSummaryUnexpectedWKMask_Type()
)
tnWtocmChanInfoSummaryUnexpectedWKMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmChanInfoSummaryUnexpectedWKMask.setStatus("current")


class _TnWtocmChanInfoSummaryProcessedWKMask_Type(OctetString):
    """Custom type tnWtocmChanInfoSummaryProcessedWKMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TnWtocmChanInfoSummaryProcessedWKMask_Type.__name__ = "OctetString"
_TnWtocmChanInfoSummaryProcessedWKMask_Object = MibTableColumn
tnWtocmChanInfoSummaryProcessedWKMask = _TnWtocmChanInfoSummaryProcessedWKMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 17, 1, 5),
    _TnWtocmChanInfoSummaryProcessedWKMask_Type()
)
tnWtocmChanInfoSummaryProcessedWKMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmChanInfoSummaryProcessedWKMask.setStatus("current")
_TnWtocmUnexpectedChannelInfoTable_Object = MibTable
tnWtocmUnexpectedChannelInfoTable = _TnWtocmUnexpectedChannelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 18)
)
if mibBuilder.loadTexts:
    tnWtocmUnexpectedChannelInfoTable.setStatus("current")
_TnWtocmUnexpectedChannelInfoEntry_Object = MibTableRow
tnWtocmUnexpectedChannelInfoEntry = _TnWtocmUnexpectedChannelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 18, 1)
)
tnWtocmUnexpectedChannelInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-WAVEKEY-MIB", "tnChannel"),
    (0, "TROPIC-WAVEKEY-MIB", "tnUnexpectedWtKeyIndex"),
)
if mibBuilder.loadTexts:
    tnWtocmUnexpectedChannelInfoEntry.setStatus("current")
_TnWtocmUnexpectedChannelInfoUnexpectedWtKey_Type = Unsigned32
_TnWtocmUnexpectedChannelInfoUnexpectedWtKey_Object = MibTableColumn
tnWtocmUnexpectedChannelInfoUnexpectedWtKey = _TnWtocmUnexpectedChannelInfoUnexpectedWtKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 18, 1, 1),
    _TnWtocmUnexpectedChannelInfoUnexpectedWtKey_Type()
)
tnWtocmUnexpectedChannelInfoUnexpectedWtKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmUnexpectedChannelInfoUnexpectedWtKey.setStatus("current")
_TnWtocmaChanConfigTable_Object = MibTable
tnWtocmaChanConfigTable = _TnWtocmaChanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 19)
)
if mibBuilder.loadTexts:
    tnWtocmaChanConfigTable.setStatus("current")
_TnWtocmaChanConfigEntry_Object = MibTableRow
tnWtocmaChanConfigEntry = _TnWtocmaChanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 19, 1)
)
tnWtocmaChanConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-WAVEKEY-MIB", "tnChannel"),
)
if mibBuilder.loadTexts:
    tnWtocmaChanConfigEntry.setStatus("current")


class _TnWtocmaChanConfigOndemandScan_Type(TruthValue):
    """Custom type tnWtocmaChanConfigOndemandScan based on TruthValue"""
    defaultValue = 2


_TnWtocmaChanConfigOndemandScan_Type.__name__ = "TruthValue"
_TnWtocmaChanConfigOndemandScan_Object = MibTableColumn
tnWtocmaChanConfigOndemandScan = _TnWtocmaChanConfigOndemandScan_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 19, 1, 1),
    _TnWtocmaChanConfigOndemandScan_Type()
)
tnWtocmaChanConfigOndemandScan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWtocmaChanConfigOndemandScan.setStatus("current")
_TnDomainWaveKeyTable_Object = MibTable
tnDomainWaveKeyTable = _TnDomainWaveKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 20)
)
if mibBuilder.loadTexts:
    tnDomainWaveKeyTable.setStatus("current")
_TnDomainWaveKeyEntry_Object = MibTableRow
tnDomainWaveKeyEntry = _TnDomainWaveKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 20, 1)
)
tnDomainWaveKeyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-WAVEKEY-MIB", "tnChannel"),
)
if mibBuilder.loadTexts:
    tnDomainWaveKeyEntry.setStatus("current")


class _TnDomainWaveKeyOchKeysUsedPercent_Type(Unsigned32):
    """Custom type tnDomainWaveKeyOchKeysUsedPercent based on Unsigned32"""
    defaultValue = 0


_TnDomainWaveKeyOchKeysUsedPercent_Type.__name__ = "Unsigned32"
_TnDomainWaveKeyOchKeysUsedPercent_Object = MibTableColumn
tnDomainWaveKeyOchKeysUsedPercent = _TnDomainWaveKeyOchKeysUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 20, 1, 1),
    _TnDomainWaveKeyOchKeysUsedPercent_Type()
)
tnDomainWaveKeyOchKeysUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDomainWaveKeyOchKeysUsedPercent.setStatus("current")


class _TnDomainWaveKeyOchUnlockedForDuplicates_Type(TruthValue):
    """Custom type tnDomainWaveKeyOchUnlockedForDuplicates based on TruthValue"""
    defaultValue = 2


_TnDomainWaveKeyOchUnlockedForDuplicates_Type.__name__ = "TruthValue"
_TnDomainWaveKeyOchUnlockedForDuplicates_Object = MibTableColumn
tnDomainWaveKeyOchUnlockedForDuplicates = _TnDomainWaveKeyOchUnlockedForDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 2, 1, 20, 1, 2),
    _TnDomainWaveKeyOchUnlockedForDuplicates_Type()
)
tnDomainWaveKeyOchUnlockedForDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDomainWaveKeyOchUnlockedForDuplicates.setStatus("current")

# Managed Objects groups

tnWaveKeyEncodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 1, 4)
)
tnWaveKeyEncodeGroup.setObjects(
      *(("TROPIC-WAVEKEY-MIB", "tnWaveKeyEncodeProgrammedWK1"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyEncodeProgrammedWK2"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyEncodeTransmitState"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyEncodeTrailName"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyEncodeProgrammedNwOutputPower"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyEncodePresentNwOutputPower"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyEncodeMaxAttainablePower"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyEncodeMinAttainablePower"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyEncodePowerUpperMargin"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyEncodePowerLowerMargin"))
)
if mibBuilder.loadTexts:
    tnWaveKeyEncodeGroup.setStatus("current")

tnWaveKeyDecodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 1, 5)
)
tnWaveKeyDecodeGroup.setObjects(
      *(("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeSupportedDirections"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeMinPlannedLossIn"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeMinPlannedLossOut"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeMaxPlannedLossIn"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeMaxPlannedLossOut"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeTypicalPlannedLossIn"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeTypicalPlannedLossOut"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeUpstreamLossIn"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeUpstreamLossOut"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeUpstreamDetectIfIndexIn"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeUpstreamDetectIfIndexOut"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeInferredIn"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeInferredOut"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeModifyPowerIn"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeModifyPowerOut"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeCurrentUpstreamLossIn"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeCurrentUpstreamLossOut"))
)
if mibBuilder.loadTexts:
    tnWaveKeyDecodeGroup.setStatus("current")

tnWtEncodePortCapabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 1, 8)
)
tnWtEncodePortCapabilityGroup.setObjects(
      *(("TROPIC-WAVEKEY-MIB", "tnWtEncodePortCapabilityProgrammed"),
        ("TROPIC-WAVEKEY-MIB", "tnWtEncodePortCapabilityPresent"),
        ("TROPIC-WAVEKEY-MIB", "tnWtEncodePortCapabilityInUse"))
)
if mibBuilder.loadTexts:
    tnWtEncodePortCapabilityGroup.setStatus("current")

tnWtEncodeCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 1, 9)
)
tnWtEncodeCardGroup.setObjects(
      *(("TROPIC-WAVEKEY-MIB", "tnWtEncodeCardExpectedPowerDev"),
        ("TROPIC-WAVEKEY-MIB", "tnWtEncodeCardExpectedPowerTolerance"))
)
if mibBuilder.loadTexts:
    tnWtEncodeCardGroup.setStatus("current")

tnWtEncodeCardCapabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 1, 10)
)
tnWtEncodeCardCapabilityGroup.setObjects(
      *(("TROPIC-WAVEKEY-MIB", "tnWtEncodeCardCapabilityProgrammed"),
        ("TROPIC-WAVEKEY-MIB", "tnWtEncodeCardCapabilityPresent"),
        ("TROPIC-WAVEKEY-MIB", "tnWtEncodeCardCapabilityInUse"))
)
if mibBuilder.loadTexts:
    tnWtEncodeCardCapabilityGroup.setStatus("current")

tnWtKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 1, 11)
)
tnWtKeyGroup.setObjects(
      *(("TROPIC-WAVEKEY-MIB", "tnWtKeyExpectedWK1"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeyExpectedWK2"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeyExpectedPower"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeyExpectedPowerDev"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeyPresentPower"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeyReceived"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeyExpectedPowerTol"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeySynchronizePower"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeyTrailName"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeyStatus"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeyApplicability"))
)
if mibBuilder.loadTexts:
    tnWtKeyGroup.setStatus("current")

tnUnexpectedWtKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 1, 12)
)
tnUnexpectedWtKeyGroup.setObjects(
      *(("TROPIC-WAVEKEY-MIB", "tnUnexpectedWtKey"),
        ("TROPIC-WAVEKEY-MIB", "tnUnexpectedWtKeyPower"))
)
if mibBuilder.loadTexts:
    tnUnexpectedWtKeyGroup.setStatus("current")

tnWtKeySummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 1, 13)
)
tnWtKeySummaryGroup.setObjects(
      *(("TROPIC-WAVEKEY-MIB", "tnWtKeySummaryExpectedWKMaskIn"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeySummaryExpectedWKMaskOut"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeySummaryReceivedWKMaskIn"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeySummaryReceivedWKMaskOut"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeySummaryUnexpectedWKMaskIn"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeySummaryUnexpectedWKMaskOut"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeySummarySupportedDirections"))
)
if mibBuilder.loadTexts:
    tnWtKeySummaryGroup.setStatus("current")

tnWtKeyDecodeInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 1, 14)
)
tnWtKeyDecodeInfoGroup.setObjects(
      *(("TROPIC-WAVEKEY-MIB", "tnWtKeyDecodeInfoSupportedDirections"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeyDecodeInfoMaxSupportedExpectedPowerIn"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeyDecodeInfoMaxSupportedExpectedPowerOut"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeyDecodeInfoMinSupportedExpectedPowerIn"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeyDecodeInfoMinSupportedExpectedPowerOut"))
)
if mibBuilder.loadTexts:
    tnWtKeyDecodeInfoGroup.setStatus("current")

tnWtocmChanInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 1, 15)
)
tnWtocmChanInfoGroup.setObjects(
      *(("TROPIC-WAVEKEY-MIB", "tnWtocmChanInfoExpectedWK1"),
        ("TROPIC-WAVEKEY-MIB", "tnWtocmChanInfoExpectedWK2"),
        ("TROPIC-WAVEKEY-MIB", "tnWtocmChanInfoPresentPower"),
        ("TROPIC-WAVEKEY-MIB", "tnWtocmChanInfoPresentPowerMonitoredPort"),
        ("TROPIC-WAVEKEY-MIB", "tnWtocmChanInfoProcessingState"),
        ("TROPIC-WAVEKEY-MIB", "tnWtocmChanInfoPresentOSNR"),
        ("TROPIC-WAVEKEY-MIB", "tnWtocmChanInfoOSNRTimeStamp"))
)
if mibBuilder.loadTexts:
    tnWtocmChanInfoGroup.setStatus("current")

tnWtocmChanInfoSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 1, 17)
)
tnWtocmChanInfoSummaryGroup.setObjects(
      *(("TROPIC-WAVEKEY-MIB", "tnWtocmChanInfoSummaryExpectedWKMask"),
        ("TROPIC-WAVEKEY-MIB", "tnWtocmChanInfoSummaryNoLosWKMask"),
        ("TROPIC-WAVEKEY-MIB", "tnWtocmChanInfoSummaryConfirmWKMask"),
        ("TROPIC-WAVEKEY-MIB", "tnWtocmChanInfoSummaryUnexpectedWKMask"),
        ("TROPIC-WAVEKEY-MIB", "tnWtocmChanInfoSummaryProcessedWKMask"))
)
if mibBuilder.loadTexts:
    tnWtocmChanInfoSummaryGroup.setStatus("current")

tnWtocmUnexpectedChannelInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 1, 18)
)
tnWtocmUnexpectedChannelInfoGroup.setObjects(
    ("TROPIC-WAVEKEY-MIB", "tnWtocmUnexpectedChannelInfoUnexpectedWtKey")
)
if mibBuilder.loadTexts:
    tnWtocmUnexpectedChannelInfoGroup.setStatus("current")

tnWtocmaChanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 1, 19)
)
tnWtocmaChanConfigGroup.setObjects(
    ("TROPIC-WAVEKEY-MIB", "tnWtocmaChanConfigOndemandScan")
)
if mibBuilder.loadTexts:
    tnWtocmaChanConfigGroup.setStatus("current")

tnDomainWaveKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 1, 20)
)
tnDomainWaveKeyGroup.setObjects(
      *(("TROPIC-WAVEKEY-MIB", "tnDomainWaveKeyOchKeysUsedPercent"),
        ("TROPIC-WAVEKEY-MIB", "tnDomainWaveKeyOchUnlockedForDuplicates"))
)
if mibBuilder.loadTexts:
    tnDomainWaveKeyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnWaveKeyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2, 1, 2, 1)
)
tnWaveKeyCompliance.setObjects(
      *(("TROPIC-WAVEKEY-MIB", "tnWaveKeyEncodeGroup"),
        ("TROPIC-WAVEKEY-MIB", "tnWaveKeyDecodeGroup"),
        ("TROPIC-WAVEKEY-MIB", "tnWtEncodePortCapabilityGroup"),
        ("TROPIC-WAVEKEY-MIB", "tnWtEncodeCardGroup"),
        ("TROPIC-WAVEKEY-MIB", "tnWtEncodeCardCapabilityGroup"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeyGroup"),
        ("TROPIC-WAVEKEY-MIB", "tnUnexpectedWtKeyGroup"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeySummaryGroup"),
        ("TROPIC-WAVEKEY-MIB", "tnWtKeyDecodeInfoGroup"),
        ("TROPIC-WAVEKEY-MIB", "tnWtocmChanInfoGroup"),
        ("TROPIC-WAVEKEY-MIB", "tnWtocmChanInfoSummaryGroup"),
        ("TROPIC-WAVEKEY-MIB", "tnWtocmUnexpectedChannelInfoGroup"),
        ("TROPIC-WAVEKEY-MIB", "tnWtocmaChanConfigGroup"),
        ("TROPIC-WAVEKEY-MIB", "tnDomainWaveKeyGroup"))
)
if mibBuilder.loadTexts:
    tnWaveKeyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-WAVEKEY-MIB",
    **{"tnWaveKeyMibModule": tnWaveKeyMibModule,
       "tnWaveKeyConf": tnWaveKeyConf,
       "tnWaveKeyGroups": tnWaveKeyGroups,
       "tnWaveKeyEncodeGroup": tnWaveKeyEncodeGroup,
       "tnWaveKeyDecodeGroup": tnWaveKeyDecodeGroup,
       "tnWtEncodePortCapabilityGroup": tnWtEncodePortCapabilityGroup,
       "tnWtEncodeCardGroup": tnWtEncodeCardGroup,
       "tnWtEncodeCardCapabilityGroup": tnWtEncodeCardCapabilityGroup,
       "tnWtKeyGroup": tnWtKeyGroup,
       "tnUnexpectedWtKeyGroup": tnUnexpectedWtKeyGroup,
       "tnWtKeySummaryGroup": tnWtKeySummaryGroup,
       "tnWtKeyDecodeInfoGroup": tnWtKeyDecodeInfoGroup,
       "tnWtocmChanInfoGroup": tnWtocmChanInfoGroup,
       "tnWtocmChanInfoSummaryGroup": tnWtocmChanInfoSummaryGroup,
       "tnWtocmUnexpectedChannelInfoGroup": tnWtocmUnexpectedChannelInfoGroup,
       "tnWtocmaChanConfigGroup": tnWtocmaChanConfigGroup,
       "tnDomainWaveKeyGroup": tnDomainWaveKeyGroup,
       "tnWaveKeyCompliances": tnWaveKeyCompliances,
       "tnWaveKeyCompliance": tnWaveKeyCompliance,
       "tnWaveKeyObjs": tnWaveKeyObjs,
       "tnWaveKeyBasics": tnWaveKeyBasics,
       "tnWaveKeyEncodeTable": tnWaveKeyEncodeTable,
       "tnWaveKeyEncodeEntry": tnWaveKeyEncodeEntry,
       "tnWaveKeyEncodeProgrammedWK1": tnWaveKeyEncodeProgrammedWK1,
       "tnWaveKeyEncodeProgrammedWK2": tnWaveKeyEncodeProgrammedWK2,
       "tnWaveKeyEncodeTransmitState": tnWaveKeyEncodeTransmitState,
       "tnWaveKeyEncodeTrailName": tnWaveKeyEncodeTrailName,
       "tnWaveKeyEncodeProgrammedNwOutputPower": tnWaveKeyEncodeProgrammedNwOutputPower,
       "tnWaveKeyEncodePresentNwOutputPower": tnWaveKeyEncodePresentNwOutputPower,
       "tnWaveKeyEncodeMaxAttainablePower": tnWaveKeyEncodeMaxAttainablePower,
       "tnWaveKeyEncodeMinAttainablePower": tnWaveKeyEncodeMinAttainablePower,
       "tnWaveKeyEncodePowerUpperMargin": tnWaveKeyEncodePowerUpperMargin,
       "tnWaveKeyEncodePowerLowerMargin": tnWaveKeyEncodePowerLowerMargin,
       "tnWaveKeyDecodeTable": tnWaveKeyDecodeTable,
       "tnWaveKeyDecodeEntry": tnWaveKeyDecodeEntry,
       "tnWaveKeyDecodeSupportedDirections": tnWaveKeyDecodeSupportedDirections,
       "tnWaveKeyDecodeMinPlannedLossIn": tnWaveKeyDecodeMinPlannedLossIn,
       "tnWaveKeyDecodeMinPlannedLossOut": tnWaveKeyDecodeMinPlannedLossOut,
       "tnWaveKeyDecodeMaxPlannedLossIn": tnWaveKeyDecodeMaxPlannedLossIn,
       "tnWaveKeyDecodeMaxPlannedLossOut": tnWaveKeyDecodeMaxPlannedLossOut,
       "tnWaveKeyDecodeTypicalPlannedLossIn": tnWaveKeyDecodeTypicalPlannedLossIn,
       "tnWaveKeyDecodeTypicalPlannedLossOut": tnWaveKeyDecodeTypicalPlannedLossOut,
       "tnWaveKeyDecodeUpstreamLossIn": tnWaveKeyDecodeUpstreamLossIn,
       "tnWaveKeyDecodeUpstreamLossOut": tnWaveKeyDecodeUpstreamLossOut,
       "tnWaveKeyDecodeUpstreamDetectIfIndexIn": tnWaveKeyDecodeUpstreamDetectIfIndexIn,
       "tnWaveKeyDecodeUpstreamDetectIfIndexOut": tnWaveKeyDecodeUpstreamDetectIfIndexOut,
       "tnWaveKeyDecodeInferredIn": tnWaveKeyDecodeInferredIn,
       "tnWaveKeyDecodeInferredOut": tnWaveKeyDecodeInferredOut,
       "tnWaveKeyDecodeModifyPowerIn": tnWaveKeyDecodeModifyPowerIn,
       "tnWaveKeyDecodeModifyPowerOut": tnWaveKeyDecodeModifyPowerOut,
       "tnWaveKeyDecodeCurrentUpstreamLossIn": tnWaveKeyDecodeCurrentUpstreamLossIn,
       "tnWaveKeyDecodeCurrentUpstreamLossOut": tnWaveKeyDecodeCurrentUpstreamLossOut,
       "tnWtEncodePortCapabilityTable": tnWtEncodePortCapabilityTable,
       "tnWtEncodePortCapabilityEntry": tnWtEncodePortCapabilityEntry,
       "tnWtEncodePortCapabilityProgrammed": tnWtEncodePortCapabilityProgrammed,
       "tnWtEncodePortCapabilityPresent": tnWtEncodePortCapabilityPresent,
       "tnWtEncodePortCapabilityInUse": tnWtEncodePortCapabilityInUse,
       "tnWtEncodeCardTable": tnWtEncodeCardTable,
       "tnWtEncodeCardEntry": tnWtEncodeCardEntry,
       "tnWtEncodeCardExpectedPowerDev": tnWtEncodeCardExpectedPowerDev,
       "tnWtEncodeCardExpectedPowerTolerance": tnWtEncodeCardExpectedPowerTolerance,
       "tnWtEncodeCardCapabilityTable": tnWtEncodeCardCapabilityTable,
       "tnWtEncodeCardCapabilityEntry": tnWtEncodeCardCapabilityEntry,
       "tnWtEncodeCardCapabilityProgrammed": tnWtEncodeCardCapabilityProgrammed,
       "tnWtEncodeCardCapabilityPresent": tnWtEncodeCardCapabilityPresent,
       "tnWtEncodeCardCapabilityInUse": tnWtEncodeCardCapabilityInUse,
       "tnWtKeyTable": tnWtKeyTable,
       "tnWtKeyEntry": tnWtKeyEntry,
       "tnDirection": tnDirection,
       "tnChannel": tnChannel,
       "tnWtKeyExpectedWK1": tnWtKeyExpectedWK1,
       "tnWtKeyExpectedWK2": tnWtKeyExpectedWK2,
       "tnWtKeyExpectedPower": tnWtKeyExpectedPower,
       "tnWtKeyExpectedPowerDev": tnWtKeyExpectedPowerDev,
       "tnWtKeyPresentPower": tnWtKeyPresentPower,
       "tnWtKeyReceived": tnWtKeyReceived,
       "tnWtKeyExpectedPowerTol": tnWtKeyExpectedPowerTol,
       "tnWtKeySynchronizePower": tnWtKeySynchronizePower,
       "tnWtKeyTrailName": tnWtKeyTrailName,
       "tnWtKeyStatus": tnWtKeyStatus,
       "tnWtKeyApplicability": tnWtKeyApplicability,
       "tnUnexpectedWtKeyTable": tnUnexpectedWtKeyTable,
       "tnUnexpectedWtKeyEntry": tnUnexpectedWtKeyEntry,
       "tnUnexpectedWtKeyIndex": tnUnexpectedWtKeyIndex,
       "tnUnexpectedWtKey": tnUnexpectedWtKey,
       "tnUnexpectedWtKeyPower": tnUnexpectedWtKeyPower,
       "tnWtKeySummaryTable": tnWtKeySummaryTable,
       "tnWtKeySummaryEntry": tnWtKeySummaryEntry,
       "tnWtKeySummaryExpectedWKMaskIn": tnWtKeySummaryExpectedWKMaskIn,
       "tnWtKeySummaryExpectedWKMaskOut": tnWtKeySummaryExpectedWKMaskOut,
       "tnWtKeySummaryReceivedWKMaskIn": tnWtKeySummaryReceivedWKMaskIn,
       "tnWtKeySummaryReceivedWKMaskOut": tnWtKeySummaryReceivedWKMaskOut,
       "tnWtKeySummaryUnexpectedWKMaskIn": tnWtKeySummaryUnexpectedWKMaskIn,
       "tnWtKeySummaryUnexpectedWKMaskOut": tnWtKeySummaryUnexpectedWKMaskOut,
       "tnWtKeySummarySupportedDirections": tnWtKeySummarySupportedDirections,
       "tnWtKeyDecodeInfoTable": tnWtKeyDecodeInfoTable,
       "tnWtKeyDecodeInfoEntry": tnWtKeyDecodeInfoEntry,
       "tnWtKeyDecodeInfoSupportedDirections": tnWtKeyDecodeInfoSupportedDirections,
       "tnWtKeyDecodeInfoMaxSupportedExpectedPowerIn": tnWtKeyDecodeInfoMaxSupportedExpectedPowerIn,
       "tnWtKeyDecodeInfoMaxSupportedExpectedPowerOut": tnWtKeyDecodeInfoMaxSupportedExpectedPowerOut,
       "tnWtKeyDecodeInfoMinSupportedExpectedPowerIn": tnWtKeyDecodeInfoMinSupportedExpectedPowerIn,
       "tnWtKeyDecodeInfoMinSupportedExpectedPowerOut": tnWtKeyDecodeInfoMinSupportedExpectedPowerOut,
       "tnWtocmChanInfoTable": tnWtocmChanInfoTable,
       "tnWtocmChanInfoEntry": tnWtocmChanInfoEntry,
       "tnWtocmChanInfoExpectedWK1": tnWtocmChanInfoExpectedWK1,
       "tnWtocmChanInfoExpectedWK2": tnWtocmChanInfoExpectedWK2,
       "tnWtocmChanInfoPresentPower": tnWtocmChanInfoPresentPower,
       "tnWtocmChanInfoPresentPowerMonitoredPort": tnWtocmChanInfoPresentPowerMonitoredPort,
       "tnWtocmChanInfoProcessingState": tnWtocmChanInfoProcessingState,
       "tnWtocmChanInfoPresentOSNR": tnWtocmChanInfoPresentOSNR,
       "tnWtocmChanInfoOSNRTimeStamp": tnWtocmChanInfoOSNRTimeStamp,
       "tnWtocmChanInfoSummaryTable": tnWtocmChanInfoSummaryTable,
       "tnWtocmChanInfoSummaryEntry": tnWtocmChanInfoSummaryEntry,
       "tnWtocmChanInfoSummaryExpectedWKMask": tnWtocmChanInfoSummaryExpectedWKMask,
       "tnWtocmChanInfoSummaryNoLosWKMask": tnWtocmChanInfoSummaryNoLosWKMask,
       "tnWtocmChanInfoSummaryConfirmWKMask": tnWtocmChanInfoSummaryConfirmWKMask,
       "tnWtocmChanInfoSummaryUnexpectedWKMask": tnWtocmChanInfoSummaryUnexpectedWKMask,
       "tnWtocmChanInfoSummaryProcessedWKMask": tnWtocmChanInfoSummaryProcessedWKMask,
       "tnWtocmUnexpectedChannelInfoTable": tnWtocmUnexpectedChannelInfoTable,
       "tnWtocmUnexpectedChannelInfoEntry": tnWtocmUnexpectedChannelInfoEntry,
       "tnWtocmUnexpectedChannelInfoUnexpectedWtKey": tnWtocmUnexpectedChannelInfoUnexpectedWtKey,
       "tnWtocmaChanConfigTable": tnWtocmaChanConfigTable,
       "tnWtocmaChanConfigEntry": tnWtocmaChanConfigEntry,
       "tnWtocmaChanConfigOndemandScan": tnWtocmaChanConfigOndemandScan,
       "tnDomainWaveKeyTable": tnDomainWaveKeyTable,
       "tnDomainWaveKeyEntry": tnDomainWaveKeyEntry,
       "tnDomainWaveKeyOchKeysUsedPercent": tnDomainWaveKeyOchKeysUsedPercent,
       "tnDomainWaveKeyOchUnlockedForDuplicates": tnDomainWaveKeyOchUnlockedForDuplicates}
)
