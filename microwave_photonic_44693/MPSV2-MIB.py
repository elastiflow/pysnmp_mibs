# SNMP MIB module (MPSV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/microwave_photonic_44693/MPSV2-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:32:12 2025
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

mpsMIBv2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 44693, 1)
)
if mibBuilder.loadTexts:
    mpsMIBv2.setRevisions(
        ("2014-12-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpsStatus_ObjectIdentity = ObjectIdentity
mpsStatus = _MpsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1)
)
if mibBuilder.loadTexts:
    mpsStatus.setStatus("current")
_MpsSystem_ObjectIdentity = ObjectIdentity
mpsSystem = _MpsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 0)
)
if mibBuilder.loadTexts:
    mpsSystem.setStatus("current")


class _MpsSystemSlotID_Type(Integer32):
    """Custom type mpsSystemSlotID based on Integer32"""
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
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("mp2320RXI", 1),
          ("mp2320TXF", 2),
          ("mp2320PRE", 3),
          ("mp2320ASW", 4),
          ("mpEthernet", 5),
          ("mpU5KRX", 6),
          ("mpU5KTX", 7),
          ("mp2320TXE", 8),
          ("mp2320RXE", 9),
          ("mp2320TX", 10),
          ("mp2320RX", 11),
          ("mp2320SW", 12),
          ("mp3080RX", 13),
          ("mpU5KTXRX", 14),
          ("mp2320TXL", 15),
          ("mp2320RXL", 16),
          ("controller", 255))
    )


_MpsSystemSlotID_Type.__name__ = "Integer32"
_MpsSystemSlotID_Object = MibScalar
mpsSystemSlotID = _MpsSystemSlotID_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 0, 1),
    _MpsSystemSlotID_Type()
)
mpsSystemSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSystemSlotID.setStatus("current")


class _MpsSystemPN_Type(DisplayString):
    """Custom type mpsSystemPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpsSystemPN_Type.__name__ = "DisplayString"
_MpsSystemPN_Object = MibScalar
mpsSystemPN = _MpsSystemPN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 0, 2),
    _MpsSystemPN_Type()
)
mpsSystemPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSystemPN.setStatus("current")
_MpsSystemSN_Type = Integer32
_MpsSystemSN_Object = MibScalar
mpsSystemSN = _MpsSystemSN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 0, 3),
    _MpsSystemSN_Type()
)
mpsSystemSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSystemSN.setStatus("current")
_MpsSystemTemp_Type = Integer32
_MpsSystemTemp_Object = MibScalar
mpsSystemTemp = _MpsSystemTemp_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 0, 15),
    _MpsSystemTemp_Type()
)
mpsSystemTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSystemTemp.setStatus("current")
_MpsSystemFan1Current_Type = Integer32
_MpsSystemFan1Current_Object = MibScalar
mpsSystemFan1Current = _MpsSystemFan1Current_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 0, 16),
    _MpsSystemFan1Current_Type()
)
mpsSystemFan1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSystemFan1Current.setStatus("current")
_MpsSystemFan2Current_Type = Integer32
_MpsSystemFan2Current_Object = MibScalar
mpsSystemFan2Current = _MpsSystemFan2Current_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 0, 17),
    _MpsSystemFan2Current_Type()
)
mpsSystemFan2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSystemFan2Current.setStatus("current")
_MpsSystemStatus_Type = Integer32
_MpsSystemStatus_Object = MibScalar
mpsSystemStatus = _MpsSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 0, 18),
    _MpsSystemStatus_Type()
)
mpsSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSystemStatus.setStatus("current")
_MpsSlot1_ObjectIdentity = ObjectIdentity
mpsSlot1 = _MpsSlot1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpsSlot1.setStatus("current")


class _MpsSlot1ID_Type(Integer32):
    """Custom type mpsSlot1ID based on Integer32"""
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
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("mp2320RXI", 1),
          ("mp2320TXF", 2),
          ("mp2320PRE", 3),
          ("mp2320ASW", 4),
          ("mpEthernet", 5),
          ("mpU5KRX", 6),
          ("mpU5KTX", 7),
          ("mp2320TXE", 8),
          ("mp2320RXE", 9),
          ("mp2320TX", 10),
          ("mp2320RX", 11),
          ("mp2320SW", 12),
          ("mp3080RX", 13),
          ("mpU5KTXRX", 14),
          ("mp2320TXL", 15),
          ("mp2320RXL", 16),
          ("controller", 255))
    )


_MpsSlot1ID_Type.__name__ = "Integer32"
_MpsSlot1ID_Object = MibScalar
mpsSlot1ID = _MpsSlot1ID_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 1),
    _MpsSlot1ID_Type()
)
mpsSlot1ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1ID.setStatus("current")


class _MpsSlot1PN_Type(DisplayString):
    """Custom type mpsSlot1PN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpsSlot1PN_Type.__name__ = "DisplayString"
_MpsSlot1PN_Object = MibScalar
mpsSlot1PN = _MpsSlot1PN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 2),
    _MpsSlot1PN_Type()
)
mpsSlot1PN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1PN.setStatus("current")
_MpsSlot1SN_Type = Integer32
_MpsSlot1SN_Object = MibScalar
mpsSlot1SN = _MpsSlot1SN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 3),
    _MpsSlot1SN_Type()
)
mpsSlot1SN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1SN.setStatus("current")
_MpsSlot1OptPwrTX_Type = Integer32
_MpsSlot1OptPwrTX_Object = MibScalar
mpsSlot1OptPwrTX = _MpsSlot1OptPwrTX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 4),
    _MpsSlot1OptPwrTX_Type()
)
mpsSlot1OptPwrTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1OptPwrTX.setStatus("current")
_MpsSlot1OptPwrRX_Type = Integer32
_MpsSlot1OptPwrRX_Object = MibScalar
mpsSlot1OptPwrRX = _MpsSlot1OptPwrRX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 5),
    _MpsSlot1OptPwrRX_Type()
)
mpsSlot1OptPwrRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1OptPwrRX.setStatus("current")
_MpsSlot1Attn1_Type = Integer32
_MpsSlot1Attn1_Object = MibScalar
mpsSlot1Attn1 = _MpsSlot1Attn1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 6),
    _MpsSlot1Attn1_Type()
)
mpsSlot1Attn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1Attn1.setStatus("current")
_MpsSlot1Attn2_Type = Integer32
_MpsSlot1Attn2_Object = MibScalar
mpsSlot1Attn2 = _MpsSlot1Attn2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 7),
    _MpsSlot1Attn2_Type()
)
mpsSlot1Attn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1Attn2.setStatus("current")
_MpsSlot1SwitchState_Type = Integer32
_MpsSlot1SwitchState_Object = MibScalar
mpsSlot1SwitchState = _MpsSlot1SwitchState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 8),
    _MpsSlot1SwitchState_Type()
)
mpsSlot1SwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1SwitchState.setStatus("current")
_MpsSlot1TXLaserBias_Type = Integer32
_MpsSlot1TXLaserBias_Object = MibScalar
mpsSlot1TXLaserBias = _MpsSlot1TXLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 9),
    _MpsSlot1TXLaserBias_Type()
)
mpsSlot1TXLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1TXLaserBias.setStatus("current")
_MpsSlot1BiasTState_Type = Integer32
_MpsSlot1BiasTState_Object = MibScalar
mpsSlot1BiasTState = _MpsSlot1BiasTState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 10),
    _MpsSlot1BiasTState_Type()
)
mpsSlot1BiasTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1BiasTState.setStatus("current")
_MpsSlot1LNACurrent_Type = Integer32
_MpsSlot1LNACurrent_Object = MibScalar
mpsSlot1LNACurrent = _MpsSlot1LNACurrent_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 11),
    _MpsSlot1LNACurrent_Type()
)
mpsSlot1LNACurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1LNACurrent.setStatus("current")
_MpsSlot1VOA_Type = Integer32
_MpsSlot1VOA_Object = MibScalar
mpsSlot1VOA = _MpsSlot1VOA_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 12),
    _MpsSlot1VOA_Type()
)
mpsSlot1VOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1VOA.setStatus("current")
_MpsSlot1OptRXAGC_Type = Integer32
_MpsSlot1OptRXAGC_Object = MibScalar
mpsSlot1OptRXAGC = _MpsSlot1OptRXAGC_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 13),
    _MpsSlot1OptRXAGC_Type()
)
mpsSlot1OptRXAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1OptRXAGC.setStatus("current")
_MpsSlot1Duplex_Type = Integer32
_MpsSlot1Duplex_Object = MibScalar
mpsSlot1Duplex = _MpsSlot1Duplex_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 14),
    _MpsSlot1Duplex_Type()
)
mpsSlot1Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1Duplex.setStatus("current")
_MpsSlot1Temp_Type = Integer32
_MpsSlot1Temp_Object = MibScalar
mpsSlot1Temp = _MpsSlot1Temp_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 15),
    _MpsSlot1Temp_Type()
)
mpsSlot1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1Temp.setStatus("current")
_MpsSlot1AuxParameter1_Type = Integer32
_MpsSlot1AuxParameter1_Object = MibScalar
mpsSlot1AuxParameter1 = _MpsSlot1AuxParameter1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 16),
    _MpsSlot1AuxParameter1_Type()
)
mpsSlot1AuxParameter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1AuxParameter1.setStatus("current")
_MpsSlot1AuxParameter2_Type = Integer32
_MpsSlot1AuxParameter2_Object = MibScalar
mpsSlot1AuxParameter2 = _MpsSlot1AuxParameter2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 17),
    _MpsSlot1AuxParameter2_Type()
)
mpsSlot1AuxParameter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1AuxParameter2.setStatus("current")
_MpsSlot1Status_Type = Integer32
_MpsSlot1Status_Object = MibScalar
mpsSlot1Status = _MpsSlot1Status_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 1, 18),
    _MpsSlot1Status_Type()
)
mpsSlot1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot1Status.setStatus("current")
_MpsSlot2_ObjectIdentity = ObjectIdentity
mpsSlot2 = _MpsSlot2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mpsSlot2.setStatus("current")


class _MpsSlot2ID_Type(Integer32):
    """Custom type mpsSlot2ID based on Integer32"""
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
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("mp2320RXI", 1),
          ("mp2320TXF", 2),
          ("mp2320PRE", 3),
          ("mp2320ASW", 4),
          ("mpEthernet", 5),
          ("mpU5KRX", 6),
          ("mpU5KTX", 7),
          ("mp2320TXE", 8),
          ("mp2320RXE", 9),
          ("mp2320TX", 10),
          ("mp2320RX", 11),
          ("mp2320SW", 12),
          ("mp3080RX", 13),
          ("mpU5KTXRX", 14),
          ("mp2320TXL", 15),
          ("mp2320RXL", 16),
          ("controller", 255))
    )


_MpsSlot2ID_Type.__name__ = "Integer32"
_MpsSlot2ID_Object = MibScalar
mpsSlot2ID = _MpsSlot2ID_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 1),
    _MpsSlot2ID_Type()
)
mpsSlot2ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2ID.setStatus("current")


class _MpsSlot2PN_Type(DisplayString):
    """Custom type mpsSlot2PN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpsSlot2PN_Type.__name__ = "DisplayString"
_MpsSlot2PN_Object = MibScalar
mpsSlot2PN = _MpsSlot2PN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 2),
    _MpsSlot2PN_Type()
)
mpsSlot2PN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2PN.setStatus("current")
_MpsSlot2SN_Type = Integer32
_MpsSlot2SN_Object = MibScalar
mpsSlot2SN = _MpsSlot2SN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 3),
    _MpsSlot2SN_Type()
)
mpsSlot2SN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2SN.setStatus("current")
_MpsSlot2OptPwrTX_Type = Integer32
_MpsSlot2OptPwrTX_Object = MibScalar
mpsSlot2OptPwrTX = _MpsSlot2OptPwrTX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 4),
    _MpsSlot2OptPwrTX_Type()
)
mpsSlot2OptPwrTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2OptPwrTX.setStatus("current")
_MpsSlot2OptPwrRX_Type = Integer32
_MpsSlot2OptPwrRX_Object = MibScalar
mpsSlot2OptPwrRX = _MpsSlot2OptPwrRX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 5),
    _MpsSlot2OptPwrRX_Type()
)
mpsSlot2OptPwrRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2OptPwrRX.setStatus("current")
_MpsSlot2Attn1_Type = Integer32
_MpsSlot2Attn1_Object = MibScalar
mpsSlot2Attn1 = _MpsSlot2Attn1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 6),
    _MpsSlot2Attn1_Type()
)
mpsSlot2Attn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2Attn1.setStatus("current")
_MpsSlot2Attn2_Type = Integer32
_MpsSlot2Attn2_Object = MibScalar
mpsSlot2Attn2 = _MpsSlot2Attn2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 7),
    _MpsSlot2Attn2_Type()
)
mpsSlot2Attn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2Attn2.setStatus("current")
_MpsSlot2SwitchState_Type = Integer32
_MpsSlot2SwitchState_Object = MibScalar
mpsSlot2SwitchState = _MpsSlot2SwitchState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 8),
    _MpsSlot2SwitchState_Type()
)
mpsSlot2SwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2SwitchState.setStatus("current")
_MpsSlot2TXLaserBias_Type = Integer32
_MpsSlot2TXLaserBias_Object = MibScalar
mpsSlot2TXLaserBias = _MpsSlot2TXLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 9),
    _MpsSlot2TXLaserBias_Type()
)
mpsSlot2TXLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2TXLaserBias.setStatus("current")
_MpsSlot2BiasTState_Type = Integer32
_MpsSlot2BiasTState_Object = MibScalar
mpsSlot2BiasTState = _MpsSlot2BiasTState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 10),
    _MpsSlot2BiasTState_Type()
)
mpsSlot2BiasTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2BiasTState.setStatus("current")
_MpsSlot2LNACurrent_Type = Integer32
_MpsSlot2LNACurrent_Object = MibScalar
mpsSlot2LNACurrent = _MpsSlot2LNACurrent_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 11),
    _MpsSlot2LNACurrent_Type()
)
mpsSlot2LNACurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2LNACurrent.setStatus("current")
_MpsSlot2VOA_Type = Integer32
_MpsSlot2VOA_Object = MibScalar
mpsSlot2VOA = _MpsSlot2VOA_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 12),
    _MpsSlot2VOA_Type()
)
mpsSlot2VOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2VOA.setStatus("current")
_MpsSlot2OptRXAGC_Type = Integer32
_MpsSlot2OptRXAGC_Object = MibScalar
mpsSlot2OptRXAGC = _MpsSlot2OptRXAGC_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 13),
    _MpsSlot2OptRXAGC_Type()
)
mpsSlot2OptRXAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2OptRXAGC.setStatus("current")
_MpsSlot2Duplex_Type = Integer32
_MpsSlot2Duplex_Object = MibScalar
mpsSlot2Duplex = _MpsSlot2Duplex_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 14),
    _MpsSlot2Duplex_Type()
)
mpsSlot2Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2Duplex.setStatus("current")
_MpsSlot2Temp_Type = Integer32
_MpsSlot2Temp_Object = MibScalar
mpsSlot2Temp = _MpsSlot2Temp_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 15),
    _MpsSlot2Temp_Type()
)
mpsSlot2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2Temp.setStatus("current")
_MpsSlot2AuxParameter1_Type = Integer32
_MpsSlot2AuxParameter1_Object = MibScalar
mpsSlot2AuxParameter1 = _MpsSlot2AuxParameter1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 16),
    _MpsSlot2AuxParameter1_Type()
)
mpsSlot2AuxParameter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2AuxParameter1.setStatus("current")
_MpsSlot2AuxParameter2_Type = Integer32
_MpsSlot2AuxParameter2_Object = MibScalar
mpsSlot2AuxParameter2 = _MpsSlot2AuxParameter2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 17),
    _MpsSlot2AuxParameter2_Type()
)
mpsSlot2AuxParameter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2AuxParameter2.setStatus("current")
_MpsSlot2Status_Type = Integer32
_MpsSlot2Status_Object = MibScalar
mpsSlot2Status = _MpsSlot2Status_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 2, 18),
    _MpsSlot2Status_Type()
)
mpsSlot2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot2Status.setStatus("current")
_MpsSlot3_ObjectIdentity = ObjectIdentity
mpsSlot3 = _MpsSlot3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mpsSlot3.setStatus("current")


class _MpsSlot3ID_Type(Integer32):
    """Custom type mpsSlot3ID based on Integer32"""
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
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("mp2320RXI", 1),
          ("mp2320TXF", 2),
          ("mp2320PRE", 3),
          ("mp2320ASW", 4),
          ("mpEthernet", 5),
          ("mpU5KRX", 6),
          ("mpU5KTX", 7),
          ("mp2320TXE", 8),
          ("mp2320RXE", 9),
          ("mp2320TX", 10),
          ("mp2320RX", 11),
          ("mp2320SW", 12),
          ("mp3080RX", 13),
          ("mpU5KTXRX", 14),
          ("mp2320TXL", 15),
          ("mp2320RXL", 16),
          ("controller", 255))
    )


_MpsSlot3ID_Type.__name__ = "Integer32"
_MpsSlot3ID_Object = MibScalar
mpsSlot3ID = _MpsSlot3ID_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 1),
    _MpsSlot3ID_Type()
)
mpsSlot3ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3ID.setStatus("current")


class _MpsSlot3PN_Type(DisplayString):
    """Custom type mpsSlot3PN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpsSlot3PN_Type.__name__ = "DisplayString"
_MpsSlot3PN_Object = MibScalar
mpsSlot3PN = _MpsSlot3PN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 2),
    _MpsSlot3PN_Type()
)
mpsSlot3PN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3PN.setStatus("current")
_MpsSlot3SN_Type = Integer32
_MpsSlot3SN_Object = MibScalar
mpsSlot3SN = _MpsSlot3SN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 3),
    _MpsSlot3SN_Type()
)
mpsSlot3SN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3SN.setStatus("current")
_MpsSlot3OptPwrTX_Type = Integer32
_MpsSlot3OptPwrTX_Object = MibScalar
mpsSlot3OptPwrTX = _MpsSlot3OptPwrTX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 4),
    _MpsSlot3OptPwrTX_Type()
)
mpsSlot3OptPwrTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3OptPwrTX.setStatus("current")
_MpsSlot3OptPwrRX_Type = Integer32
_MpsSlot3OptPwrRX_Object = MibScalar
mpsSlot3OptPwrRX = _MpsSlot3OptPwrRX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 5),
    _MpsSlot3OptPwrRX_Type()
)
mpsSlot3OptPwrRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3OptPwrRX.setStatus("current")
_MpsSlot3Attn1_Type = Integer32
_MpsSlot3Attn1_Object = MibScalar
mpsSlot3Attn1 = _MpsSlot3Attn1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 6),
    _MpsSlot3Attn1_Type()
)
mpsSlot3Attn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3Attn1.setStatus("current")
_MpsSlot3Attn2_Type = Integer32
_MpsSlot3Attn2_Object = MibScalar
mpsSlot3Attn2 = _MpsSlot3Attn2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 7),
    _MpsSlot3Attn2_Type()
)
mpsSlot3Attn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3Attn2.setStatus("current")
_MpsSlot3SwitchState_Type = Integer32
_MpsSlot3SwitchState_Object = MibScalar
mpsSlot3SwitchState = _MpsSlot3SwitchState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 8),
    _MpsSlot3SwitchState_Type()
)
mpsSlot3SwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3SwitchState.setStatus("current")
_MpsSlot3TXLaserBias_Type = Integer32
_MpsSlot3TXLaserBias_Object = MibScalar
mpsSlot3TXLaserBias = _MpsSlot3TXLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 9),
    _MpsSlot3TXLaserBias_Type()
)
mpsSlot3TXLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3TXLaserBias.setStatus("current")
_MpsSlot3BiasTState_Type = Integer32
_MpsSlot3BiasTState_Object = MibScalar
mpsSlot3BiasTState = _MpsSlot3BiasTState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 10),
    _MpsSlot3BiasTState_Type()
)
mpsSlot3BiasTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3BiasTState.setStatus("current")
_MpsSlot3LNACurrent_Type = Integer32
_MpsSlot3LNACurrent_Object = MibScalar
mpsSlot3LNACurrent = _MpsSlot3LNACurrent_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 11),
    _MpsSlot3LNACurrent_Type()
)
mpsSlot3LNACurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3LNACurrent.setStatus("current")
_MpsSlot3VOA_Type = Integer32
_MpsSlot3VOA_Object = MibScalar
mpsSlot3VOA = _MpsSlot3VOA_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 12),
    _MpsSlot3VOA_Type()
)
mpsSlot3VOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3VOA.setStatus("current")
_MpsSlot3OptRXAGC_Type = Integer32
_MpsSlot3OptRXAGC_Object = MibScalar
mpsSlot3OptRXAGC = _MpsSlot3OptRXAGC_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 13),
    _MpsSlot3OptRXAGC_Type()
)
mpsSlot3OptRXAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3OptRXAGC.setStatus("current")
_MpsSlot3Duplex_Type = Integer32
_MpsSlot3Duplex_Object = MibScalar
mpsSlot3Duplex = _MpsSlot3Duplex_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 14),
    _MpsSlot3Duplex_Type()
)
mpsSlot3Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3Duplex.setStatus("current")
_MpsSlot3Temp_Type = Integer32
_MpsSlot3Temp_Object = MibScalar
mpsSlot3Temp = _MpsSlot3Temp_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 15),
    _MpsSlot3Temp_Type()
)
mpsSlot3Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3Temp.setStatus("current")
_MpsSlot3AuxParameter1_Type = Integer32
_MpsSlot3AuxParameter1_Object = MibScalar
mpsSlot3AuxParameter1 = _MpsSlot3AuxParameter1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 16),
    _MpsSlot3AuxParameter1_Type()
)
mpsSlot3AuxParameter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3AuxParameter1.setStatus("current")
_MpsSlot3AuxParameter2_Type = Integer32
_MpsSlot3AuxParameter2_Object = MibScalar
mpsSlot3AuxParameter2 = _MpsSlot3AuxParameter2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 17),
    _MpsSlot3AuxParameter2_Type()
)
mpsSlot3AuxParameter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3AuxParameter2.setStatus("current")
_MpsSlot3Status_Type = Integer32
_MpsSlot3Status_Object = MibScalar
mpsSlot3Status = _MpsSlot3Status_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 3, 18),
    _MpsSlot3Status_Type()
)
mpsSlot3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot3Status.setStatus("current")
_MpsSlot4_ObjectIdentity = ObjectIdentity
mpsSlot4 = _MpsSlot4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4)
)
if mibBuilder.loadTexts:
    mpsSlot4.setStatus("current")


class _MpsSlot4ID_Type(Integer32):
    """Custom type mpsSlot4ID based on Integer32"""
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
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("mp2320RXI", 1),
          ("mp2320TXF", 2),
          ("mp2320PRE", 3),
          ("mp2320ASW", 4),
          ("mpEthernet", 5),
          ("mpU5KRX", 6),
          ("mpU5KTX", 7),
          ("mp2320TXE", 8),
          ("mp2320RXE", 9),
          ("mp2320TX", 10),
          ("mp2320RX", 11),
          ("mp2320SW", 12),
          ("mp3080RX", 13),
          ("mpU5KTXRX", 14),
          ("mp2320TXL", 15),
          ("mp2320RXL", 16),
          ("controller", 255))
    )


_MpsSlot4ID_Type.__name__ = "Integer32"
_MpsSlot4ID_Object = MibScalar
mpsSlot4ID = _MpsSlot4ID_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 1),
    _MpsSlot4ID_Type()
)
mpsSlot4ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4ID.setStatus("current")


class _MpsSlot4PN_Type(DisplayString):
    """Custom type mpsSlot4PN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpsSlot4PN_Type.__name__ = "DisplayString"
_MpsSlot4PN_Object = MibScalar
mpsSlot4PN = _MpsSlot4PN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 2),
    _MpsSlot4PN_Type()
)
mpsSlot4PN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4PN.setStatus("current")
_MpsSlot4SN_Type = Integer32
_MpsSlot4SN_Object = MibScalar
mpsSlot4SN = _MpsSlot4SN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 3),
    _MpsSlot4SN_Type()
)
mpsSlot4SN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4SN.setStatus("current")
_MpsSlot4OptPwrTX_Type = Integer32
_MpsSlot4OptPwrTX_Object = MibScalar
mpsSlot4OptPwrTX = _MpsSlot4OptPwrTX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 4),
    _MpsSlot4OptPwrTX_Type()
)
mpsSlot4OptPwrTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4OptPwrTX.setStatus("current")
_MpsSlot4OptPwrRX_Type = Integer32
_MpsSlot4OptPwrRX_Object = MibScalar
mpsSlot4OptPwrRX = _MpsSlot4OptPwrRX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 5),
    _MpsSlot4OptPwrRX_Type()
)
mpsSlot4OptPwrRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4OptPwrRX.setStatus("current")
_MpsSlot4Attn1_Type = Integer32
_MpsSlot4Attn1_Object = MibScalar
mpsSlot4Attn1 = _MpsSlot4Attn1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 6),
    _MpsSlot4Attn1_Type()
)
mpsSlot4Attn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4Attn1.setStatus("current")
_MpsSlot4Attn2_Type = Integer32
_MpsSlot4Attn2_Object = MibScalar
mpsSlot4Attn2 = _MpsSlot4Attn2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 7),
    _MpsSlot4Attn2_Type()
)
mpsSlot4Attn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4Attn2.setStatus("current")
_MpsSlot4SwitchState_Type = Integer32
_MpsSlot4SwitchState_Object = MibScalar
mpsSlot4SwitchState = _MpsSlot4SwitchState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 8),
    _MpsSlot4SwitchState_Type()
)
mpsSlot4SwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4SwitchState.setStatus("current")
_MpsSlot4TXLaserBias_Type = Integer32
_MpsSlot4TXLaserBias_Object = MibScalar
mpsSlot4TXLaserBias = _MpsSlot4TXLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 9),
    _MpsSlot4TXLaserBias_Type()
)
mpsSlot4TXLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4TXLaserBias.setStatus("current")
_MpsSlot4BiasTState_Type = Integer32
_MpsSlot4BiasTState_Object = MibScalar
mpsSlot4BiasTState = _MpsSlot4BiasTState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 10),
    _MpsSlot4BiasTState_Type()
)
mpsSlot4BiasTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4BiasTState.setStatus("current")
_MpsSlot4LNACurrent_Type = Integer32
_MpsSlot4LNACurrent_Object = MibScalar
mpsSlot4LNACurrent = _MpsSlot4LNACurrent_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 11),
    _MpsSlot4LNACurrent_Type()
)
mpsSlot4LNACurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4LNACurrent.setStatus("current")
_MpsSlot4VOA_Type = Integer32
_MpsSlot4VOA_Object = MibScalar
mpsSlot4VOA = _MpsSlot4VOA_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 12),
    _MpsSlot4VOA_Type()
)
mpsSlot4VOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4VOA.setStatus("current")
_MpsSlot4OptRXAGC_Type = Integer32
_MpsSlot4OptRXAGC_Object = MibScalar
mpsSlot4OptRXAGC = _MpsSlot4OptRXAGC_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 13),
    _MpsSlot4OptRXAGC_Type()
)
mpsSlot4OptRXAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4OptRXAGC.setStatus("current")
_MpsSlot4Duplex_Type = Integer32
_MpsSlot4Duplex_Object = MibScalar
mpsSlot4Duplex = _MpsSlot4Duplex_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 14),
    _MpsSlot4Duplex_Type()
)
mpsSlot4Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4Duplex.setStatus("current")
_MpsSlot4Temp_Type = Integer32
_MpsSlot4Temp_Object = MibScalar
mpsSlot4Temp = _MpsSlot4Temp_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 15),
    _MpsSlot4Temp_Type()
)
mpsSlot4Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4Temp.setStatus("current")
_MpsSlot4AuxParameter1_Type = Integer32
_MpsSlot4AuxParameter1_Object = MibScalar
mpsSlot4AuxParameter1 = _MpsSlot4AuxParameter1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 16),
    _MpsSlot4AuxParameter1_Type()
)
mpsSlot4AuxParameter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4AuxParameter1.setStatus("current")
_MpsSlot4AuxParameter2_Type = Integer32
_MpsSlot4AuxParameter2_Object = MibScalar
mpsSlot4AuxParameter2 = _MpsSlot4AuxParameter2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 17),
    _MpsSlot4AuxParameter2_Type()
)
mpsSlot4AuxParameter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4AuxParameter2.setStatus("current")
_MpsSlot4Status_Type = Integer32
_MpsSlot4Status_Object = MibScalar
mpsSlot4Status = _MpsSlot4Status_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 4, 18),
    _MpsSlot4Status_Type()
)
mpsSlot4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot4Status.setStatus("current")
_MpsSlot5_ObjectIdentity = ObjectIdentity
mpsSlot5 = _MpsSlot5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5)
)
if mibBuilder.loadTexts:
    mpsSlot5.setStatus("current")


class _MpsSlot5ID_Type(Integer32):
    """Custom type mpsSlot5ID based on Integer32"""
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
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("mp2320RXI", 1),
          ("mp2320TXF", 2),
          ("mp2320PRE", 3),
          ("mp2320ASW", 4),
          ("mpEthernet", 5),
          ("mpU5KRX", 6),
          ("mpU5KTX", 7),
          ("mp2320TXE", 8),
          ("mp2320RXE", 9),
          ("mp2320TX", 10),
          ("mp2320RX", 11),
          ("mp2320SW", 12),
          ("mp3080RX", 13),
          ("mpU5KTXRX", 14),
          ("mp2320TXL", 15),
          ("mp2320RXL", 16),
          ("controller", 255))
    )


_MpsSlot5ID_Type.__name__ = "Integer32"
_MpsSlot5ID_Object = MibScalar
mpsSlot5ID = _MpsSlot5ID_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 1),
    _MpsSlot5ID_Type()
)
mpsSlot5ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5ID.setStatus("current")


class _MpsSlot5PN_Type(DisplayString):
    """Custom type mpsSlot5PN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpsSlot5PN_Type.__name__ = "DisplayString"
_MpsSlot5PN_Object = MibScalar
mpsSlot5PN = _MpsSlot5PN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 2),
    _MpsSlot5PN_Type()
)
mpsSlot5PN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5PN.setStatus("current")
_MpsSlot5SN_Type = Integer32
_MpsSlot5SN_Object = MibScalar
mpsSlot5SN = _MpsSlot5SN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 3),
    _MpsSlot5SN_Type()
)
mpsSlot5SN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5SN.setStatus("current")
_MpsSlot5OptPwrTX_Type = Integer32
_MpsSlot5OptPwrTX_Object = MibScalar
mpsSlot5OptPwrTX = _MpsSlot5OptPwrTX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 4),
    _MpsSlot5OptPwrTX_Type()
)
mpsSlot5OptPwrTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5OptPwrTX.setStatus("current")
_MpsSlot5OptPwrRX_Type = Integer32
_MpsSlot5OptPwrRX_Object = MibScalar
mpsSlot5OptPwrRX = _MpsSlot5OptPwrRX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 5),
    _MpsSlot5OptPwrRX_Type()
)
mpsSlot5OptPwrRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5OptPwrRX.setStatus("current")
_MpsSlot5Attn1_Type = Integer32
_MpsSlot5Attn1_Object = MibScalar
mpsSlot5Attn1 = _MpsSlot5Attn1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 6),
    _MpsSlot5Attn1_Type()
)
mpsSlot5Attn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5Attn1.setStatus("current")
_MpsSlot5Attn2_Type = Integer32
_MpsSlot5Attn2_Object = MibScalar
mpsSlot5Attn2 = _MpsSlot5Attn2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 7),
    _MpsSlot5Attn2_Type()
)
mpsSlot5Attn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5Attn2.setStatus("current")
_MpsSlot5SwitchState_Type = Integer32
_MpsSlot5SwitchState_Object = MibScalar
mpsSlot5SwitchState = _MpsSlot5SwitchState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 8),
    _MpsSlot5SwitchState_Type()
)
mpsSlot5SwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5SwitchState.setStatus("current")
_MpsSlot5TXLaserBias_Type = Integer32
_MpsSlot5TXLaserBias_Object = MibScalar
mpsSlot5TXLaserBias = _MpsSlot5TXLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 9),
    _MpsSlot5TXLaserBias_Type()
)
mpsSlot5TXLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5TXLaserBias.setStatus("current")
_MpsSlot5BiasTState_Type = Integer32
_MpsSlot5BiasTState_Object = MibScalar
mpsSlot5BiasTState = _MpsSlot5BiasTState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 10),
    _MpsSlot5BiasTState_Type()
)
mpsSlot5BiasTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5BiasTState.setStatus("current")
_MpsSlot5LNACurrent_Type = Integer32
_MpsSlot5LNACurrent_Object = MibScalar
mpsSlot5LNACurrent = _MpsSlot5LNACurrent_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 11),
    _MpsSlot5LNACurrent_Type()
)
mpsSlot5LNACurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5LNACurrent.setStatus("current")
_MpsSlot5VOA_Type = Integer32
_MpsSlot5VOA_Object = MibScalar
mpsSlot5VOA = _MpsSlot5VOA_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 12),
    _MpsSlot5VOA_Type()
)
mpsSlot5VOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5VOA.setStatus("current")
_MpsSlot5OptRXAGC_Type = Integer32
_MpsSlot5OptRXAGC_Object = MibScalar
mpsSlot5OptRXAGC = _MpsSlot5OptRXAGC_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 13),
    _MpsSlot5OptRXAGC_Type()
)
mpsSlot5OptRXAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5OptRXAGC.setStatus("current")
_MpsSlot5Duplex_Type = Integer32
_MpsSlot5Duplex_Object = MibScalar
mpsSlot5Duplex = _MpsSlot5Duplex_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 14),
    _MpsSlot5Duplex_Type()
)
mpsSlot5Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5Duplex.setStatus("current")
_MpsSlot5Temp_Type = Integer32
_MpsSlot5Temp_Object = MibScalar
mpsSlot5Temp = _MpsSlot5Temp_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 15),
    _MpsSlot5Temp_Type()
)
mpsSlot5Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5Temp.setStatus("current")
_MpsSlot5AuxParameter1_Type = Integer32
_MpsSlot5AuxParameter1_Object = MibScalar
mpsSlot5AuxParameter1 = _MpsSlot5AuxParameter1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 16),
    _MpsSlot5AuxParameter1_Type()
)
mpsSlot5AuxParameter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5AuxParameter1.setStatus("current")
_MpsSlot5AuxParameter2_Type = Integer32
_MpsSlot5AuxParameter2_Object = MibScalar
mpsSlot5AuxParameter2 = _MpsSlot5AuxParameter2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 17),
    _MpsSlot5AuxParameter2_Type()
)
mpsSlot5AuxParameter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5AuxParameter2.setStatus("current")
_MpsSlot5Status_Type = Integer32
_MpsSlot5Status_Object = MibScalar
mpsSlot5Status = _MpsSlot5Status_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 5, 18),
    _MpsSlot5Status_Type()
)
mpsSlot5Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot5Status.setStatus("current")
_MpsSlot6_ObjectIdentity = ObjectIdentity
mpsSlot6 = _MpsSlot6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6)
)
if mibBuilder.loadTexts:
    mpsSlot6.setStatus("current")


class _MpsSlot6ID_Type(Integer32):
    """Custom type mpsSlot6ID based on Integer32"""
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
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("mp2320RXI", 1),
          ("mp2320TXF", 2),
          ("mp2320PRE", 3),
          ("mp2320ASW", 4),
          ("mpEthernet", 5),
          ("mpU5KRX", 6),
          ("mpU5KTX", 7),
          ("mp2320TXE", 8),
          ("mp2320RXE", 9),
          ("mp2320TX", 10),
          ("mp2320RX", 11),
          ("mp2320SW", 12),
          ("mp3080RX", 13),
          ("mpU5KTXRX", 14),
          ("mp2320TXL", 15),
          ("mp2320RXL", 16),
          ("controller", 255))
    )


_MpsSlot6ID_Type.__name__ = "Integer32"
_MpsSlot6ID_Object = MibScalar
mpsSlot6ID = _MpsSlot6ID_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 1),
    _MpsSlot6ID_Type()
)
mpsSlot6ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6ID.setStatus("current")


class _MpsSlot6PN_Type(DisplayString):
    """Custom type mpsSlot6PN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpsSlot6PN_Type.__name__ = "DisplayString"
_MpsSlot6PN_Object = MibScalar
mpsSlot6PN = _MpsSlot6PN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 2),
    _MpsSlot6PN_Type()
)
mpsSlot6PN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6PN.setStatus("current")
_MpsSlot6SN_Type = Integer32
_MpsSlot6SN_Object = MibScalar
mpsSlot6SN = _MpsSlot6SN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 3),
    _MpsSlot6SN_Type()
)
mpsSlot6SN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6SN.setStatus("current")
_MpsSlot6OptPwrTX_Type = Integer32
_MpsSlot6OptPwrTX_Object = MibScalar
mpsSlot6OptPwrTX = _MpsSlot6OptPwrTX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 4),
    _MpsSlot6OptPwrTX_Type()
)
mpsSlot6OptPwrTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6OptPwrTX.setStatus("current")
_MpsSlot6OptPwrRX_Type = Integer32
_MpsSlot6OptPwrRX_Object = MibScalar
mpsSlot6OptPwrRX = _MpsSlot6OptPwrRX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 5),
    _MpsSlot6OptPwrRX_Type()
)
mpsSlot6OptPwrRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6OptPwrRX.setStatus("current")
_MpsSlot6Attn1_Type = Integer32
_MpsSlot6Attn1_Object = MibScalar
mpsSlot6Attn1 = _MpsSlot6Attn1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 6),
    _MpsSlot6Attn1_Type()
)
mpsSlot6Attn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6Attn1.setStatus("current")
_MpsSlot6Attn2_Type = Integer32
_MpsSlot6Attn2_Object = MibScalar
mpsSlot6Attn2 = _MpsSlot6Attn2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 7),
    _MpsSlot6Attn2_Type()
)
mpsSlot6Attn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6Attn2.setStatus("current")
_MpsSlot6SwitchState_Type = Integer32
_MpsSlot6SwitchState_Object = MibScalar
mpsSlot6SwitchState = _MpsSlot6SwitchState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 8),
    _MpsSlot6SwitchState_Type()
)
mpsSlot6SwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6SwitchState.setStatus("current")
_MpsSlot6TXLaserBias_Type = Integer32
_MpsSlot6TXLaserBias_Object = MibScalar
mpsSlot6TXLaserBias = _MpsSlot6TXLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 9),
    _MpsSlot6TXLaserBias_Type()
)
mpsSlot6TXLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6TXLaserBias.setStatus("current")
_MpsSlot6BiasTState_Type = Integer32
_MpsSlot6BiasTState_Object = MibScalar
mpsSlot6BiasTState = _MpsSlot6BiasTState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 10),
    _MpsSlot6BiasTState_Type()
)
mpsSlot6BiasTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6BiasTState.setStatus("current")
_MpsSlot6LNACurrent_Type = Integer32
_MpsSlot6LNACurrent_Object = MibScalar
mpsSlot6LNACurrent = _MpsSlot6LNACurrent_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 11),
    _MpsSlot6LNACurrent_Type()
)
mpsSlot6LNACurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6LNACurrent.setStatus("current")
_MpsSlot6VOA_Type = Integer32
_MpsSlot6VOA_Object = MibScalar
mpsSlot6VOA = _MpsSlot6VOA_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 12),
    _MpsSlot6VOA_Type()
)
mpsSlot6VOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6VOA.setStatus("current")
_MpsSlot6OptRXAGC_Type = Integer32
_MpsSlot6OptRXAGC_Object = MibScalar
mpsSlot6OptRXAGC = _MpsSlot6OptRXAGC_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 13),
    _MpsSlot6OptRXAGC_Type()
)
mpsSlot6OptRXAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6OptRXAGC.setStatus("current")
_MpsSlot6Duplex_Type = Integer32
_MpsSlot6Duplex_Object = MibScalar
mpsSlot6Duplex = _MpsSlot6Duplex_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 14),
    _MpsSlot6Duplex_Type()
)
mpsSlot6Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6Duplex.setStatus("current")
_MpsSlot6Temp_Type = Integer32
_MpsSlot6Temp_Object = MibScalar
mpsSlot6Temp = _MpsSlot6Temp_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 15),
    _MpsSlot6Temp_Type()
)
mpsSlot6Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6Temp.setStatus("current")
_MpsSlot6AuxParameter1_Type = Integer32
_MpsSlot6AuxParameter1_Object = MibScalar
mpsSlot6AuxParameter1 = _MpsSlot6AuxParameter1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 16),
    _MpsSlot6AuxParameter1_Type()
)
mpsSlot6AuxParameter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6AuxParameter1.setStatus("current")
_MpsSlot6AuxParameter2_Type = Integer32
_MpsSlot6AuxParameter2_Object = MibScalar
mpsSlot6AuxParameter2 = _MpsSlot6AuxParameter2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 17),
    _MpsSlot6AuxParameter2_Type()
)
mpsSlot6AuxParameter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6AuxParameter2.setStatus("current")
_MpsSlot6Status_Type = Integer32
_MpsSlot6Status_Object = MibScalar
mpsSlot6Status = _MpsSlot6Status_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 6, 18),
    _MpsSlot6Status_Type()
)
mpsSlot6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot6Status.setStatus("current")
_MpsSlot7_ObjectIdentity = ObjectIdentity
mpsSlot7 = _MpsSlot7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7)
)
if mibBuilder.loadTexts:
    mpsSlot7.setStatus("current")


class _MpsSlot7ID_Type(Integer32):
    """Custom type mpsSlot7ID based on Integer32"""
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
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("mp2320RXI", 1),
          ("mp2320TXF", 2),
          ("mp2320PRE", 3),
          ("mp2320ASW", 4),
          ("mpEthernet", 5),
          ("mpU5KRX", 6),
          ("mpU5KTX", 7),
          ("mp2320TXE", 8),
          ("mp2320RXE", 9),
          ("mp2320TX", 10),
          ("mp2320RX", 11),
          ("mp2320SW", 12),
          ("mp3080RX", 13),
          ("mpU5KTXRX", 14),
          ("mp2320TXL", 15),
          ("mp2320RXL", 16),
          ("controller", 255))
    )


_MpsSlot7ID_Type.__name__ = "Integer32"
_MpsSlot7ID_Object = MibScalar
mpsSlot7ID = _MpsSlot7ID_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 1),
    _MpsSlot7ID_Type()
)
mpsSlot7ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7ID.setStatus("current")


class _MpsSlot7PN_Type(DisplayString):
    """Custom type mpsSlot7PN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpsSlot7PN_Type.__name__ = "DisplayString"
_MpsSlot7PN_Object = MibScalar
mpsSlot7PN = _MpsSlot7PN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 2),
    _MpsSlot7PN_Type()
)
mpsSlot7PN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7PN.setStatus("current")
_MpsSlot7SN_Type = Integer32
_MpsSlot7SN_Object = MibScalar
mpsSlot7SN = _MpsSlot7SN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 3),
    _MpsSlot7SN_Type()
)
mpsSlot7SN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7SN.setStatus("current")
_MpsSlot7OptPwrTX_Type = Integer32
_MpsSlot7OptPwrTX_Object = MibScalar
mpsSlot7OptPwrTX = _MpsSlot7OptPwrTX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 4),
    _MpsSlot7OptPwrTX_Type()
)
mpsSlot7OptPwrTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7OptPwrTX.setStatus("current")
_MpsSlot7OptPwrRX_Type = Integer32
_MpsSlot7OptPwrRX_Object = MibScalar
mpsSlot7OptPwrRX = _MpsSlot7OptPwrRX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 5),
    _MpsSlot7OptPwrRX_Type()
)
mpsSlot7OptPwrRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7OptPwrRX.setStatus("current")
_MpsSlot7Attn1_Type = Integer32
_MpsSlot7Attn1_Object = MibScalar
mpsSlot7Attn1 = _MpsSlot7Attn1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 6),
    _MpsSlot7Attn1_Type()
)
mpsSlot7Attn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7Attn1.setStatus("current")
_MpsSlot7Attn2_Type = Integer32
_MpsSlot7Attn2_Object = MibScalar
mpsSlot7Attn2 = _MpsSlot7Attn2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 7),
    _MpsSlot7Attn2_Type()
)
mpsSlot7Attn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7Attn2.setStatus("current")
_MpsSlot7SwitchState_Type = Integer32
_MpsSlot7SwitchState_Object = MibScalar
mpsSlot7SwitchState = _MpsSlot7SwitchState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 8),
    _MpsSlot7SwitchState_Type()
)
mpsSlot7SwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7SwitchState.setStatus("current")
_MpsSlot7TXLaserBias_Type = Integer32
_MpsSlot7TXLaserBias_Object = MibScalar
mpsSlot7TXLaserBias = _MpsSlot7TXLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 9),
    _MpsSlot7TXLaserBias_Type()
)
mpsSlot7TXLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7TXLaserBias.setStatus("current")
_MpsSlot7BiasTState_Type = Integer32
_MpsSlot7BiasTState_Object = MibScalar
mpsSlot7BiasTState = _MpsSlot7BiasTState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 10),
    _MpsSlot7BiasTState_Type()
)
mpsSlot7BiasTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7BiasTState.setStatus("current")
_MpsSlot7LNACurrent_Type = Integer32
_MpsSlot7LNACurrent_Object = MibScalar
mpsSlot7LNACurrent = _MpsSlot7LNACurrent_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 11),
    _MpsSlot7LNACurrent_Type()
)
mpsSlot7LNACurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7LNACurrent.setStatus("current")
_MpsSlot7VOA_Type = Integer32
_MpsSlot7VOA_Object = MibScalar
mpsSlot7VOA = _MpsSlot7VOA_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 12),
    _MpsSlot7VOA_Type()
)
mpsSlot7VOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7VOA.setStatus("current")
_MpsSlot7OptRXAGC_Type = Integer32
_MpsSlot7OptRXAGC_Object = MibScalar
mpsSlot7OptRXAGC = _MpsSlot7OptRXAGC_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 13),
    _MpsSlot7OptRXAGC_Type()
)
mpsSlot7OptRXAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7OptRXAGC.setStatus("current")
_MpsSlot7Duplex_Type = Integer32
_MpsSlot7Duplex_Object = MibScalar
mpsSlot7Duplex = _MpsSlot7Duplex_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 14),
    _MpsSlot7Duplex_Type()
)
mpsSlot7Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7Duplex.setStatus("current")
_MpsSlot7Temp_Type = Integer32
_MpsSlot7Temp_Object = MibScalar
mpsSlot7Temp = _MpsSlot7Temp_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 15),
    _MpsSlot7Temp_Type()
)
mpsSlot7Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7Temp.setStatus("current")
_MpsSlot7AuxParameter1_Type = Integer32
_MpsSlot7AuxParameter1_Object = MibScalar
mpsSlot7AuxParameter1 = _MpsSlot7AuxParameter1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 16),
    _MpsSlot7AuxParameter1_Type()
)
mpsSlot7AuxParameter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7AuxParameter1.setStatus("current")
_MpsSlot7AuxParameter2_Type = Integer32
_MpsSlot7AuxParameter2_Object = MibScalar
mpsSlot7AuxParameter2 = _MpsSlot7AuxParameter2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 17),
    _MpsSlot7AuxParameter2_Type()
)
mpsSlot7AuxParameter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7AuxParameter2.setStatus("current")
_MpsSlot7Status_Type = Integer32
_MpsSlot7Status_Object = MibScalar
mpsSlot7Status = _MpsSlot7Status_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 7, 18),
    _MpsSlot7Status_Type()
)
mpsSlot7Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot7Status.setStatus("current")
_MpsSlot8_ObjectIdentity = ObjectIdentity
mpsSlot8 = _MpsSlot8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8)
)
if mibBuilder.loadTexts:
    mpsSlot8.setStatus("current")


class _MpsSlot8ID_Type(Integer32):
    """Custom type mpsSlot8ID based on Integer32"""
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
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("mp2320RXI", 1),
          ("mp2320TXF", 2),
          ("mp2320PRE", 3),
          ("mp2320ASW", 4),
          ("mpEthernet", 5),
          ("mpU5KRX", 6),
          ("mpU5KTX", 7),
          ("mp2320TXE", 8),
          ("mp2320RXE", 9),
          ("mp2320TX", 10),
          ("mp2320RX", 11),
          ("mp2320SW", 12),
          ("mp3080RX", 13),
          ("mpU5KTXRX", 14),
          ("mp2320TXL", 15),
          ("mp2320RXL", 16),
          ("controller", 255))
    )


_MpsSlot8ID_Type.__name__ = "Integer32"
_MpsSlot8ID_Object = MibScalar
mpsSlot8ID = _MpsSlot8ID_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 1),
    _MpsSlot8ID_Type()
)
mpsSlot8ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8ID.setStatus("current")


class _MpsSlot8PN_Type(DisplayString):
    """Custom type mpsSlot8PN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpsSlot8PN_Type.__name__ = "DisplayString"
_MpsSlot8PN_Object = MibScalar
mpsSlot8PN = _MpsSlot8PN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 2),
    _MpsSlot8PN_Type()
)
mpsSlot8PN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8PN.setStatus("current")
_MpsSlot8SN_Type = Integer32
_MpsSlot8SN_Object = MibScalar
mpsSlot8SN = _MpsSlot8SN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 3),
    _MpsSlot8SN_Type()
)
mpsSlot8SN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8SN.setStatus("current")
_MpsSlot8OptPwrTX_Type = Integer32
_MpsSlot8OptPwrTX_Object = MibScalar
mpsSlot8OptPwrTX = _MpsSlot8OptPwrTX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 4),
    _MpsSlot8OptPwrTX_Type()
)
mpsSlot8OptPwrTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8OptPwrTX.setStatus("current")
_MpsSlot8OptPwrRX_Type = Integer32
_MpsSlot8OptPwrRX_Object = MibScalar
mpsSlot8OptPwrRX = _MpsSlot8OptPwrRX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 5),
    _MpsSlot8OptPwrRX_Type()
)
mpsSlot8OptPwrRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8OptPwrRX.setStatus("current")
_MpsSlot8Attn1_Type = Integer32
_MpsSlot8Attn1_Object = MibScalar
mpsSlot8Attn1 = _MpsSlot8Attn1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 6),
    _MpsSlot8Attn1_Type()
)
mpsSlot8Attn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8Attn1.setStatus("current")
_MpsSlot8Attn2_Type = Integer32
_MpsSlot8Attn2_Object = MibScalar
mpsSlot8Attn2 = _MpsSlot8Attn2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 7),
    _MpsSlot8Attn2_Type()
)
mpsSlot8Attn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8Attn2.setStatus("current")
_MpsSlot8SwitchState_Type = Integer32
_MpsSlot8SwitchState_Object = MibScalar
mpsSlot8SwitchState = _MpsSlot8SwitchState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 8),
    _MpsSlot8SwitchState_Type()
)
mpsSlot8SwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8SwitchState.setStatus("current")
_MpsSlot8TXLaserBias_Type = Integer32
_MpsSlot8TXLaserBias_Object = MibScalar
mpsSlot8TXLaserBias = _MpsSlot8TXLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 9),
    _MpsSlot8TXLaserBias_Type()
)
mpsSlot8TXLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8TXLaserBias.setStatus("current")
_MpsSlot8BiasTState_Type = Integer32
_MpsSlot8BiasTState_Object = MibScalar
mpsSlot8BiasTState = _MpsSlot8BiasTState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 10),
    _MpsSlot8BiasTState_Type()
)
mpsSlot8BiasTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8BiasTState.setStatus("current")
_MpsSlot8LNACurrent_Type = Integer32
_MpsSlot8LNACurrent_Object = MibScalar
mpsSlot8LNACurrent = _MpsSlot8LNACurrent_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 11),
    _MpsSlot8LNACurrent_Type()
)
mpsSlot8LNACurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8LNACurrent.setStatus("current")
_MpsSlot8VOA_Type = Integer32
_MpsSlot8VOA_Object = MibScalar
mpsSlot8VOA = _MpsSlot8VOA_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 12),
    _MpsSlot8VOA_Type()
)
mpsSlot8VOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8VOA.setStatus("current")
_MpsSlot8OptRXAGC_Type = Integer32
_MpsSlot8OptRXAGC_Object = MibScalar
mpsSlot8OptRXAGC = _MpsSlot8OptRXAGC_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 13),
    _MpsSlot8OptRXAGC_Type()
)
mpsSlot8OptRXAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8OptRXAGC.setStatus("current")
_MpsSlot8Duplex_Type = Integer32
_MpsSlot8Duplex_Object = MibScalar
mpsSlot8Duplex = _MpsSlot8Duplex_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 14),
    _MpsSlot8Duplex_Type()
)
mpsSlot8Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8Duplex.setStatus("current")
_MpsSlot8Temp_Type = Integer32
_MpsSlot8Temp_Object = MibScalar
mpsSlot8Temp = _MpsSlot8Temp_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 15),
    _MpsSlot8Temp_Type()
)
mpsSlot8Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8Temp.setStatus("current")
_MpsSlot8AuxParameter1_Type = Integer32
_MpsSlot8AuxParameter1_Object = MibScalar
mpsSlot8AuxParameter1 = _MpsSlot8AuxParameter1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 16),
    _MpsSlot8AuxParameter1_Type()
)
mpsSlot8AuxParameter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8AuxParameter1.setStatus("current")
_MpsSlot8AuxParameter2_Type = Integer32
_MpsSlot8AuxParameter2_Object = MibScalar
mpsSlot8AuxParameter2 = _MpsSlot8AuxParameter2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 17),
    _MpsSlot8AuxParameter2_Type()
)
mpsSlot8AuxParameter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8AuxParameter2.setStatus("current")
_MpsSlot8Status_Type = Integer32
_MpsSlot8Status_Object = MibScalar
mpsSlot8Status = _MpsSlot8Status_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 8, 18),
    _MpsSlot8Status_Type()
)
mpsSlot8Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot8Status.setStatus("current")
_MpsSlot9_ObjectIdentity = ObjectIdentity
mpsSlot9 = _MpsSlot9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9)
)
if mibBuilder.loadTexts:
    mpsSlot9.setStatus("current")


class _MpsSlot9ID_Type(Integer32):
    """Custom type mpsSlot9ID based on Integer32"""
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
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("mp2320RXI", 1),
          ("mp2320TXF", 2),
          ("mp2320PRE", 3),
          ("mp2320ASW", 4),
          ("mpEthernet", 5),
          ("mpU5KRX", 6),
          ("mpU5KTX", 7),
          ("mp2320TXE", 8),
          ("mp2320RXE", 9),
          ("mp2320TX", 10),
          ("mp2320RX", 11),
          ("mp2320SW", 12),
          ("mp3080RX", 13),
          ("mpU5KTXRX", 14),
          ("mp2320TXL", 15),
          ("mp2320RXL", 16),
          ("controller", 255))
    )


_MpsSlot9ID_Type.__name__ = "Integer32"
_MpsSlot9ID_Object = MibScalar
mpsSlot9ID = _MpsSlot9ID_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 1),
    _MpsSlot9ID_Type()
)
mpsSlot9ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9ID.setStatus("current")


class _MpsSlot9PN_Type(DisplayString):
    """Custom type mpsSlot9PN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpsSlot9PN_Type.__name__ = "DisplayString"
_MpsSlot9PN_Object = MibScalar
mpsSlot9PN = _MpsSlot9PN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 2),
    _MpsSlot9PN_Type()
)
mpsSlot9PN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9PN.setStatus("current")
_MpsSlot9SN_Type = Integer32
_MpsSlot9SN_Object = MibScalar
mpsSlot9SN = _MpsSlot9SN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 3),
    _MpsSlot9SN_Type()
)
mpsSlot9SN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9SN.setStatus("current")
_MpsSlot9OptPwrTX_Type = Integer32
_MpsSlot9OptPwrTX_Object = MibScalar
mpsSlot9OptPwrTX = _MpsSlot9OptPwrTX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 4),
    _MpsSlot9OptPwrTX_Type()
)
mpsSlot9OptPwrTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9OptPwrTX.setStatus("current")
_MpsSlot9OptPwrRX_Type = Integer32
_MpsSlot9OptPwrRX_Object = MibScalar
mpsSlot9OptPwrRX = _MpsSlot9OptPwrRX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 5),
    _MpsSlot9OptPwrRX_Type()
)
mpsSlot9OptPwrRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9OptPwrRX.setStatus("current")
_MpsSlot9Attn1_Type = Integer32
_MpsSlot9Attn1_Object = MibScalar
mpsSlot9Attn1 = _MpsSlot9Attn1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 6),
    _MpsSlot9Attn1_Type()
)
mpsSlot9Attn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9Attn1.setStatus("current")
_MpsSlot9Attn2_Type = Integer32
_MpsSlot9Attn2_Object = MibScalar
mpsSlot9Attn2 = _MpsSlot9Attn2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 7),
    _MpsSlot9Attn2_Type()
)
mpsSlot9Attn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9Attn2.setStatus("current")
_MpsSlot9SwitchState_Type = Integer32
_MpsSlot9SwitchState_Object = MibScalar
mpsSlot9SwitchState = _MpsSlot9SwitchState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 8),
    _MpsSlot9SwitchState_Type()
)
mpsSlot9SwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9SwitchState.setStatus("current")
_MpsSlot9TXLaserBias_Type = Integer32
_MpsSlot9TXLaserBias_Object = MibScalar
mpsSlot9TXLaserBias = _MpsSlot9TXLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 9),
    _MpsSlot9TXLaserBias_Type()
)
mpsSlot9TXLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9TXLaserBias.setStatus("current")
_MpsSlot9BiasTState_Type = Integer32
_MpsSlot9BiasTState_Object = MibScalar
mpsSlot9BiasTState = _MpsSlot9BiasTState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 10),
    _MpsSlot9BiasTState_Type()
)
mpsSlot9BiasTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9BiasTState.setStatus("current")
_MpsSlot9LNACurrent_Type = Integer32
_MpsSlot9LNACurrent_Object = MibScalar
mpsSlot9LNACurrent = _MpsSlot9LNACurrent_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 11),
    _MpsSlot9LNACurrent_Type()
)
mpsSlot9LNACurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9LNACurrent.setStatus("current")
_MpsSlot9VOA_Type = Integer32
_MpsSlot9VOA_Object = MibScalar
mpsSlot9VOA = _MpsSlot9VOA_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 12),
    _MpsSlot9VOA_Type()
)
mpsSlot9VOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9VOA.setStatus("current")
_MpsSlot9OptRXAGC_Type = Integer32
_MpsSlot9OptRXAGC_Object = MibScalar
mpsSlot9OptRXAGC = _MpsSlot9OptRXAGC_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 13),
    _MpsSlot9OptRXAGC_Type()
)
mpsSlot9OptRXAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9OptRXAGC.setStatus("current")
_MpsSlot9Duplex_Type = Integer32
_MpsSlot9Duplex_Object = MibScalar
mpsSlot9Duplex = _MpsSlot9Duplex_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 14),
    _MpsSlot9Duplex_Type()
)
mpsSlot9Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9Duplex.setStatus("current")
_MpsSlot9Temp_Type = Integer32
_MpsSlot9Temp_Object = MibScalar
mpsSlot9Temp = _MpsSlot9Temp_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 15),
    _MpsSlot9Temp_Type()
)
mpsSlot9Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9Temp.setStatus("current")
_MpsSlot9AuxParameter1_Type = Integer32
_MpsSlot9AuxParameter1_Object = MibScalar
mpsSlot9AuxParameter1 = _MpsSlot9AuxParameter1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 16),
    _MpsSlot9AuxParameter1_Type()
)
mpsSlot9AuxParameter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9AuxParameter1.setStatus("current")
_MpsSlot9AuxParameter2_Type = Integer32
_MpsSlot9AuxParameter2_Object = MibScalar
mpsSlot9AuxParameter2 = _MpsSlot9AuxParameter2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 17),
    _MpsSlot9AuxParameter2_Type()
)
mpsSlot9AuxParameter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9AuxParameter2.setStatus("current")
_MpsSlot9Status_Type = Integer32
_MpsSlot9Status_Object = MibScalar
mpsSlot9Status = _MpsSlot9Status_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 9, 18),
    _MpsSlot9Status_Type()
)
mpsSlot9Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot9Status.setStatus("current")
_MpsSlot10_ObjectIdentity = ObjectIdentity
mpsSlot10 = _MpsSlot10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10)
)
if mibBuilder.loadTexts:
    mpsSlot10.setStatus("current")


class _MpsSlot10ID_Type(Integer32):
    """Custom type mpsSlot10ID based on Integer32"""
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
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("mp2320RXI", 1),
          ("mp2320TXF", 2),
          ("mp2320PRE", 3),
          ("mp2320ASW", 4),
          ("mpEthernet", 5),
          ("mpU5KRX", 6),
          ("mpU5KTX", 7),
          ("mp2320TXE", 8),
          ("mp2320RXE", 9),
          ("mp2320TX", 10),
          ("mp2320RX", 11),
          ("mp2320SW", 12),
          ("mp3080RX", 13),
          ("mpU5KTXRX", 14),
          ("mp2320TXL", 15),
          ("mp2320RXL", 16),
          ("controller", 255))
    )


_MpsSlot10ID_Type.__name__ = "Integer32"
_MpsSlot10ID_Object = MibScalar
mpsSlot10ID = _MpsSlot10ID_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 1),
    _MpsSlot10ID_Type()
)
mpsSlot10ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10ID.setStatus("current")


class _MpsSlot10PN_Type(DisplayString):
    """Custom type mpsSlot10PN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpsSlot10PN_Type.__name__ = "DisplayString"
_MpsSlot10PN_Object = MibScalar
mpsSlot10PN = _MpsSlot10PN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 2),
    _MpsSlot10PN_Type()
)
mpsSlot10PN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10PN.setStatus("current")
_MpsSlot10SN_Type = Integer32
_MpsSlot10SN_Object = MibScalar
mpsSlot10SN = _MpsSlot10SN_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 3),
    _MpsSlot10SN_Type()
)
mpsSlot10SN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10SN.setStatus("current")
_MpsSlot10OptPwrTX_Type = Integer32
_MpsSlot10OptPwrTX_Object = MibScalar
mpsSlot10OptPwrTX = _MpsSlot10OptPwrTX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 4),
    _MpsSlot10OptPwrTX_Type()
)
mpsSlot10OptPwrTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10OptPwrTX.setStatus("current")
_MpsSlot10OptPwrRX_Type = Integer32
_MpsSlot10OptPwrRX_Object = MibScalar
mpsSlot10OptPwrRX = _MpsSlot10OptPwrRX_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 5),
    _MpsSlot10OptPwrRX_Type()
)
mpsSlot10OptPwrRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10OptPwrRX.setStatus("current")
_MpsSlot10Attn1_Type = Integer32
_MpsSlot10Attn1_Object = MibScalar
mpsSlot10Attn1 = _MpsSlot10Attn1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 6),
    _MpsSlot10Attn1_Type()
)
mpsSlot10Attn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10Attn1.setStatus("current")
_MpsSlot10Attn2_Type = Integer32
_MpsSlot10Attn2_Object = MibScalar
mpsSlot10Attn2 = _MpsSlot10Attn2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 7),
    _MpsSlot10Attn2_Type()
)
mpsSlot10Attn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10Attn2.setStatus("current")
_MpsSlot10SwitchState_Type = Integer32
_MpsSlot10SwitchState_Object = MibScalar
mpsSlot10SwitchState = _MpsSlot10SwitchState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 8),
    _MpsSlot10SwitchState_Type()
)
mpsSlot10SwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10SwitchState.setStatus("current")
_MpsSlot10TXLaserBias_Type = Integer32
_MpsSlot10TXLaserBias_Object = MibScalar
mpsSlot10TXLaserBias = _MpsSlot10TXLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 9),
    _MpsSlot10TXLaserBias_Type()
)
mpsSlot10TXLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10TXLaserBias.setStatus("current")
_MpsSlot10BiasTState_Type = Integer32
_MpsSlot10BiasTState_Object = MibScalar
mpsSlot10BiasTState = _MpsSlot10BiasTState_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 10),
    _MpsSlot10BiasTState_Type()
)
mpsSlot10BiasTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10BiasTState.setStatus("current")
_MpsSlot10LNACurrent_Type = Integer32
_MpsSlot10LNACurrent_Object = MibScalar
mpsSlot10LNACurrent = _MpsSlot10LNACurrent_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 11),
    _MpsSlot10LNACurrent_Type()
)
mpsSlot10LNACurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10LNACurrent.setStatus("current")
_MpsSlot10VOA_Type = Integer32
_MpsSlot10VOA_Object = MibScalar
mpsSlot10VOA = _MpsSlot10VOA_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 12),
    _MpsSlot10VOA_Type()
)
mpsSlot10VOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10VOA.setStatus("current")
_MpsSlot10OptRXAGC_Type = Integer32
_MpsSlot10OptRXAGC_Object = MibScalar
mpsSlot10OptRXAGC = _MpsSlot10OptRXAGC_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 13),
    _MpsSlot10OptRXAGC_Type()
)
mpsSlot10OptRXAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10OptRXAGC.setStatus("current")
_MpsSlot10Duplex_Type = Integer32
_MpsSlot10Duplex_Object = MibScalar
mpsSlot10Duplex = _MpsSlot10Duplex_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 14),
    _MpsSlot10Duplex_Type()
)
mpsSlot10Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10Duplex.setStatus("current")
_MpsSlot10Temp_Type = Integer32
_MpsSlot10Temp_Object = MibScalar
mpsSlot10Temp = _MpsSlot10Temp_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 15),
    _MpsSlot10Temp_Type()
)
mpsSlot10Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10Temp.setStatus("current")
_MpsSlot10AuxParameter1_Type = Integer32
_MpsSlot10AuxParameter1_Object = MibScalar
mpsSlot10AuxParameter1 = _MpsSlot10AuxParameter1_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 16),
    _MpsSlot10AuxParameter1_Type()
)
mpsSlot10AuxParameter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10AuxParameter1.setStatus("current")
_MpsSlot10AuxParameter2_Type = Integer32
_MpsSlot10AuxParameter2_Object = MibScalar
mpsSlot10AuxParameter2 = _MpsSlot10AuxParameter2_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 17),
    _MpsSlot10AuxParameter2_Type()
)
mpsSlot10AuxParameter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10AuxParameter2.setStatus("current")
_MpsSlot10Status_Type = Integer32
_MpsSlot10Status_Object = MibScalar
mpsSlot10Status = _MpsSlot10Status_Object(
    (1, 3, 6, 1, 4, 1, 44693, 1, 1, 10, 18),
    _MpsSlot10Status_Type()
)
mpsSlot10Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsSlot10Status.setStatus("current")
_MpsParameterGroups_ObjectIdentity = ObjectIdentity
mpsParameterGroups = _MpsParameterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2)
)
if mibBuilder.loadTexts:
    mpsParameterGroups.setStatus("current")
_MpsModuleCompliance_ObjectIdentity = ObjectIdentity
mpsModuleCompliance = _MpsModuleCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3)
)
if mibBuilder.loadTexts:
    mpsModuleCompliance.setStatus("current")

# Managed Objects groups

mpsID = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 1)
)
mpsID.setObjects(
      *(("MPSV2-MIB", "mpsSystemSlotID"),
        ("MPSV2-MIB", "mpsSlot1ID"),
        ("MPSV2-MIB", "mpsSlot2ID"),
        ("MPSV2-MIB", "mpsSlot3ID"),
        ("MPSV2-MIB", "mpsSlot4ID"),
        ("MPSV2-MIB", "mpsSlot5ID"),
        ("MPSV2-MIB", "mpsSlot6ID"),
        ("MPSV2-MIB", "mpsSlot7ID"),
        ("MPSV2-MIB", "mpsSlot8ID"),
        ("MPSV2-MIB", "mpsSlot9ID"),
        ("MPSV2-MIB", "mpsSlot10ID"))
)
if mibBuilder.loadTexts:
    mpsID.setStatus("current")

mpsPN = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 2)
)
mpsPN.setObjects(
      *(("MPSV2-MIB", "mpsSystemPN"),
        ("MPSV2-MIB", "mpsSlot1PN"),
        ("MPSV2-MIB", "mpsSlot2PN"),
        ("MPSV2-MIB", "mpsSlot3PN"),
        ("MPSV2-MIB", "mpsSlot4PN"),
        ("MPSV2-MIB", "mpsSlot5PN"),
        ("MPSV2-MIB", "mpsSlot6PN"),
        ("MPSV2-MIB", "mpsSlot7PN"),
        ("MPSV2-MIB", "mpsSlot8PN"),
        ("MPSV2-MIB", "mpsSlot9PN"),
        ("MPSV2-MIB", "mpsSlot10PN"))
)
if mibBuilder.loadTexts:
    mpsPN.setStatus("current")

mpsSN = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 3)
)
mpsSN.setObjects(
      *(("MPSV2-MIB", "mpsSystemSN"),
        ("MPSV2-MIB", "mpsSlot1SN"),
        ("MPSV2-MIB", "mpsSlot2SN"),
        ("MPSV2-MIB", "mpsSlot3SN"),
        ("MPSV2-MIB", "mpsSlot4SN"),
        ("MPSV2-MIB", "mpsSlot5SN"),
        ("MPSV2-MIB", "mpsSlot6SN"),
        ("MPSV2-MIB", "mpsSlot7SN"),
        ("MPSV2-MIB", "mpsSlot8SN"),
        ("MPSV2-MIB", "mpsSlot9SN"),
        ("MPSV2-MIB", "mpsSlot10SN"))
)
if mibBuilder.loadTexts:
    mpsSN.setStatus("current")

mpsOptPwrTX = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 4)
)
mpsOptPwrTX.setObjects(
      *(("MPSV2-MIB", "mpsSlot1OptPwrTX"),
        ("MPSV2-MIB", "mpsSlot2OptPwrTX"),
        ("MPSV2-MIB", "mpsSlot3OptPwrTX"),
        ("MPSV2-MIB", "mpsSlot4OptPwrTX"),
        ("MPSV2-MIB", "mpsSlot5OptPwrTX"),
        ("MPSV2-MIB", "mpsSlot6OptPwrTX"),
        ("MPSV2-MIB", "mpsSlot7OptPwrTX"),
        ("MPSV2-MIB", "mpsSlot8OptPwrTX"),
        ("MPSV2-MIB", "mpsSlot9OptPwrTX"),
        ("MPSV2-MIB", "mpsSlot10OptPwrTX"))
)
if mibBuilder.loadTexts:
    mpsOptPwrTX.setStatus("current")

mpsOptPwrRX = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 5)
)
mpsOptPwrRX.setObjects(
      *(("MPSV2-MIB", "mpsSlot1OptPwrRX"),
        ("MPSV2-MIB", "mpsSlot2OptPwrRX"),
        ("MPSV2-MIB", "mpsSlot3OptPwrRX"),
        ("MPSV2-MIB", "mpsSlot4OptPwrRX"),
        ("MPSV2-MIB", "mpsSlot5OptPwrRX"),
        ("MPSV2-MIB", "mpsSlot6OptPwrRX"),
        ("MPSV2-MIB", "mpsSlot7OptPwrRX"),
        ("MPSV2-MIB", "mpsSlot8OptPwrRX"),
        ("MPSV2-MIB", "mpsSlot9OptPwrRX"),
        ("MPSV2-MIB", "mpsSlot10OptPwrRX"))
)
if mibBuilder.loadTexts:
    mpsOptPwrRX.setStatus("current")

mpsAttn1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 6)
)
mpsAttn1.setObjects(
      *(("MPSV2-MIB", "mpsSlot1Attn1"),
        ("MPSV2-MIB", "mpsSlot2Attn1"),
        ("MPSV2-MIB", "mpsSlot3Attn1"),
        ("MPSV2-MIB", "mpsSlot4Attn1"),
        ("MPSV2-MIB", "mpsSlot5Attn1"),
        ("MPSV2-MIB", "mpsSlot6Attn1"),
        ("MPSV2-MIB", "mpsSlot7Attn1"),
        ("MPSV2-MIB", "mpsSlot8Attn1"),
        ("MPSV2-MIB", "mpsSlot9Attn1"),
        ("MPSV2-MIB", "mpsSlot10Attn1"))
)
if mibBuilder.loadTexts:
    mpsAttn1.setStatus("current")

mpsAttn2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 7)
)
mpsAttn2.setObjects(
      *(("MPSV2-MIB", "mpsSlot1Attn2"),
        ("MPSV2-MIB", "mpsSlot2Attn2"),
        ("MPSV2-MIB", "mpsSlot3Attn2"),
        ("MPSV2-MIB", "mpsSlot4Attn2"),
        ("MPSV2-MIB", "mpsSlot5Attn2"),
        ("MPSV2-MIB", "mpsSlot6Attn2"),
        ("MPSV2-MIB", "mpsSlot7Attn2"),
        ("MPSV2-MIB", "mpsSlot8Attn2"),
        ("MPSV2-MIB", "mpsSlot9Attn2"),
        ("MPSV2-MIB", "mpsSlot10Attn2"))
)
if mibBuilder.loadTexts:
    mpsAttn2.setStatus("current")

mpsSwitchState = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 8)
)
mpsSwitchState.setObjects(
      *(("MPSV2-MIB", "mpsSlot1SwitchState"),
        ("MPSV2-MIB", "mpsSlot2SwitchState"),
        ("MPSV2-MIB", "mpsSlot3SwitchState"),
        ("MPSV2-MIB", "mpsSlot4SwitchState"),
        ("MPSV2-MIB", "mpsSlot5SwitchState"),
        ("MPSV2-MIB", "mpsSlot6SwitchState"),
        ("MPSV2-MIB", "mpsSlot7SwitchState"),
        ("MPSV2-MIB", "mpsSlot8SwitchState"),
        ("MPSV2-MIB", "mpsSlot9SwitchState"),
        ("MPSV2-MIB", "mpsSlot10SwitchState"))
)
if mibBuilder.loadTexts:
    mpsSwitchState.setStatus("current")

mpsTXLaserBias = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 9)
)
mpsTXLaserBias.setObjects(
      *(("MPSV2-MIB", "mpsSlot1TXLaserBias"),
        ("MPSV2-MIB", "mpsSlot2TXLaserBias"),
        ("MPSV2-MIB", "mpsSlot3TXLaserBias"),
        ("MPSV2-MIB", "mpsSlot4TXLaserBias"),
        ("MPSV2-MIB", "mpsSlot5TXLaserBias"),
        ("MPSV2-MIB", "mpsSlot6TXLaserBias"),
        ("MPSV2-MIB", "mpsSlot7TXLaserBias"),
        ("MPSV2-MIB", "mpsSlot8TXLaserBias"),
        ("MPSV2-MIB", "mpsSlot9TXLaserBias"),
        ("MPSV2-MIB", "mpsSlot10TXLaserBias"))
)
if mibBuilder.loadTexts:
    mpsTXLaserBias.setStatus("current")

mpsBiasTState = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 10)
)
mpsBiasTState.setObjects(
      *(("MPSV2-MIB", "mpsSlot1BiasTState"),
        ("MPSV2-MIB", "mpsSlot2BiasTState"),
        ("MPSV2-MIB", "mpsSlot3BiasTState"),
        ("MPSV2-MIB", "mpsSlot4BiasTState"),
        ("MPSV2-MIB", "mpsSlot5BiasTState"),
        ("MPSV2-MIB", "mpsSlot6BiasTState"),
        ("MPSV2-MIB", "mpsSlot7BiasTState"),
        ("MPSV2-MIB", "mpsSlot8BiasTState"),
        ("MPSV2-MIB", "mpsSlot9BiasTState"),
        ("MPSV2-MIB", "mpsSlot10BiasTState"))
)
if mibBuilder.loadTexts:
    mpsBiasTState.setStatus("current")

mpsLNACurrent = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 11)
)
mpsLNACurrent.setObjects(
      *(("MPSV2-MIB", "mpsSlot1LNACurrent"),
        ("MPSV2-MIB", "mpsSlot2LNACurrent"),
        ("MPSV2-MIB", "mpsSlot3LNACurrent"),
        ("MPSV2-MIB", "mpsSlot4LNACurrent"),
        ("MPSV2-MIB", "mpsSlot5LNACurrent"),
        ("MPSV2-MIB", "mpsSlot6LNACurrent"),
        ("MPSV2-MIB", "mpsSlot7LNACurrent"),
        ("MPSV2-MIB", "mpsSlot8LNACurrent"),
        ("MPSV2-MIB", "mpsSlot9LNACurrent"),
        ("MPSV2-MIB", "mpsSlot10LNACurrent"))
)
if mibBuilder.loadTexts:
    mpsLNACurrent.setStatus("current")

mpsVOA = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 12)
)
mpsVOA.setObjects(
      *(("MPSV2-MIB", "mpsSlot1VOA"),
        ("MPSV2-MIB", "mpsSlot2VOA"),
        ("MPSV2-MIB", "mpsSlot3VOA"),
        ("MPSV2-MIB", "mpsSlot4VOA"),
        ("MPSV2-MIB", "mpsSlot5VOA"),
        ("MPSV2-MIB", "mpsSlot6VOA"),
        ("MPSV2-MIB", "mpsSlot7VOA"),
        ("MPSV2-MIB", "mpsSlot8VOA"),
        ("MPSV2-MIB", "mpsSlot9VOA"),
        ("MPSV2-MIB", "mpsSlot10VOA"))
)
if mibBuilder.loadTexts:
    mpsVOA.setStatus("current")

mpsOptRXAGC = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 13)
)
mpsOptRXAGC.setObjects(
      *(("MPSV2-MIB", "mpsSlot1OptRXAGC"),
        ("MPSV2-MIB", "mpsSlot2OptRXAGC"),
        ("MPSV2-MIB", "mpsSlot3OptRXAGC"),
        ("MPSV2-MIB", "mpsSlot4OptRXAGC"),
        ("MPSV2-MIB", "mpsSlot5OptRXAGC"),
        ("MPSV2-MIB", "mpsSlot6OptRXAGC"),
        ("MPSV2-MIB", "mpsSlot7OptRXAGC"),
        ("MPSV2-MIB", "mpsSlot8OptRXAGC"),
        ("MPSV2-MIB", "mpsSlot9OptRXAGC"),
        ("MPSV2-MIB", "mpsSlot10OptRXAGC"))
)
if mibBuilder.loadTexts:
    mpsOptRXAGC.setStatus("current")

mpsDuplex = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 14)
)
mpsDuplex.setObjects(
      *(("MPSV2-MIB", "mpsSlot1Duplex"),
        ("MPSV2-MIB", "mpsSlot2Duplex"),
        ("MPSV2-MIB", "mpsSlot3Duplex"),
        ("MPSV2-MIB", "mpsSlot4Duplex"),
        ("MPSV2-MIB", "mpsSlot5Duplex"),
        ("MPSV2-MIB", "mpsSlot6Duplex"),
        ("MPSV2-MIB", "mpsSlot7Duplex"),
        ("MPSV2-MIB", "mpsSlot8Duplex"),
        ("MPSV2-MIB", "mpsSlot9Duplex"),
        ("MPSV2-MIB", "mpsSlot10Duplex"))
)
if mibBuilder.loadTexts:
    mpsDuplex.setStatus("current")

mpsTemp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 15)
)
mpsTemp.setObjects(
      *(("MPSV2-MIB", "mpsSystemTemp"),
        ("MPSV2-MIB", "mpsSlot1Temp"),
        ("MPSV2-MIB", "mpsSlot2Temp"),
        ("MPSV2-MIB", "mpsSlot3Temp"),
        ("MPSV2-MIB", "mpsSlot4Temp"),
        ("MPSV2-MIB", "mpsSlot5Temp"),
        ("MPSV2-MIB", "mpsSlot6Temp"),
        ("MPSV2-MIB", "mpsSlot7Temp"),
        ("MPSV2-MIB", "mpsSlot8Temp"),
        ("MPSV2-MIB", "mpsSlot9Temp"),
        ("MPSV2-MIB", "mpsSlot10Temp"))
)
if mibBuilder.loadTexts:
    mpsTemp.setStatus("current")

mpsAuxParameter1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 16)
)
mpsAuxParameter1.setObjects(
      *(("MPSV2-MIB", "mpsSystemFan1Current"),
        ("MPSV2-MIB", "mpsSlot1AuxParameter1"),
        ("MPSV2-MIB", "mpsSlot2AuxParameter1"),
        ("MPSV2-MIB", "mpsSlot3AuxParameter1"),
        ("MPSV2-MIB", "mpsSlot4AuxParameter1"),
        ("MPSV2-MIB", "mpsSlot5AuxParameter1"),
        ("MPSV2-MIB", "mpsSlot6AuxParameter1"),
        ("MPSV2-MIB", "mpsSlot7AuxParameter1"),
        ("MPSV2-MIB", "mpsSlot8AuxParameter1"),
        ("MPSV2-MIB", "mpsSlot9AuxParameter1"),
        ("MPSV2-MIB", "mpsSlot10AuxParameter1"))
)
if mibBuilder.loadTexts:
    mpsAuxParameter1.setStatus("current")

mpsAuxParameter2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 17)
)
mpsAuxParameter2.setObjects(
      *(("MPSV2-MIB", "mpsSystemFan2Current"),
        ("MPSV2-MIB", "mpsSlot1AuxParameter2"),
        ("MPSV2-MIB", "mpsSlot2AuxParameter2"),
        ("MPSV2-MIB", "mpsSlot3AuxParameter2"),
        ("MPSV2-MIB", "mpsSlot4AuxParameter2"),
        ("MPSV2-MIB", "mpsSlot5AuxParameter2"),
        ("MPSV2-MIB", "mpsSlot6AuxParameter2"),
        ("MPSV2-MIB", "mpsSlot7AuxParameter2"),
        ("MPSV2-MIB", "mpsSlot8AuxParameter2"),
        ("MPSV2-MIB", "mpsSlot9AuxParameter2"),
        ("MPSV2-MIB", "mpsSlot10AuxParameter2"))
)
if mibBuilder.loadTexts:
    mpsAuxParameter2.setStatus("current")

mpsModuleStatus = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44693, 1, 2, 18)
)
mpsModuleStatus.setObjects(
      *(("MPSV2-MIB", "mpsSystemStatus"),
        ("MPSV2-MIB", "mpsSlot1Status"),
        ("MPSV2-MIB", "mpsSlot2Status"),
        ("MPSV2-MIB", "mpsSlot3Status"),
        ("MPSV2-MIB", "mpsSlot4Status"),
        ("MPSV2-MIB", "mpsSlot5Status"),
        ("MPSV2-MIB", "mpsSlot6Status"),
        ("MPSV2-MIB", "mpsSlot7Status"),
        ("MPSV2-MIB", "mpsSlot8Status"),
        ("MPSV2-MIB", "mpsSlot9Status"),
        ("MPSV2-MIB", "mpsSlot10Status"))
)
if mibBuilder.loadTexts:
    mpsModuleStatus.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mp2320RXI = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 1)
)
mp2320RXI.setObjects(
      *(("MPSV2-MIB", "mpsID"),
        ("MPSV2-MIB", "mpsPN"),
        ("MPSV2-MIB", "mpsSN"),
        ("MPSV2-MIB", "mpsOptPwrRX"),
        ("MPSV2-MIB", "mpsAttn1"),
        ("MPSV2-MIB", "mpsAttn2"),
        ("MPSV2-MIB", "mpsTemp"),
        ("MPSV2-MIB", "mpsModuleStatus"))
)
if mibBuilder.loadTexts:
    mp2320RXI.setStatus(
        "current"
    )

mp2320TXF = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 2)
)
mp2320TXF.setObjects(
      *(("MPSV2-MIB", "mpsID"),
        ("MPSV2-MIB", "mpsPN"),
        ("MPSV2-MIB", "mpsSN"),
        ("MPSV2-MIB", "mpsOptPwrTX"),
        ("MPSV2-MIB", "mpsAttn1"),
        ("MPSV2-MIB", "mpsAttn2"),
        ("MPSV2-MIB", "mpsTXLaserBias"),
        ("MPSV2-MIB", "mpsBiasTState"),
        ("MPSV2-MIB", "mpsLNACurrent"),
        ("MPSV2-MIB", "mpsTemp"),
        ("MPSV2-MIB", "mpsModuleStatus"))
)
if mibBuilder.loadTexts:
    mp2320TXF.setStatus(
        "current"
    )

mp2320PRE = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 3)
)
mp2320PRE.setObjects(
      *(("MPSV2-MIB", "mpsID"),
        ("MPSV2-MIB", "mpsPN"),
        ("MPSV2-MIB", "mpsSN"),
        ("MPSV2-MIB", "mpsAttn1"),
        ("MPSV2-MIB", "mpsTemp"),
        ("MPSV2-MIB", "mpsModuleStatus"))
)
if mibBuilder.loadTexts:
    mp2320PRE.setStatus(
        "current"
    )

mp2320ASW = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 4)
)
mp2320ASW.setObjects(
      *(("MPSV2-MIB", "mpsID"),
        ("MPSV2-MIB", "mpsPN"),
        ("MPSV2-MIB", "mpsSN"),
        ("MPSV2-MIB", "mpsSwitchState"),
        ("MPSV2-MIB", "mpsTemp"),
        ("MPSV2-MIB", "mpsModuleStatus"))
)
if mibBuilder.loadTexts:
    mp2320ASW.setStatus(
        "current"
    )

mpEthernet = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 5)
)
mpEthernet.setObjects(
    ("MPSV2-MIB", "mpsID")
)
if mibBuilder.loadTexts:
    mpEthernet.setStatus(
        "current"
    )

mpU5KRX = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 6)
)
mpU5KRX.setObjects(
      *(("MPSV2-MIB", "mpsID"),
        ("MPSV2-MIB", "mpsPN"),
        ("MPSV2-MIB", "mpsSN"),
        ("MPSV2-MIB", "mpsOptPwrRX"),
        ("MPSV2-MIB", "mpsAuxParameter1"),
        ("MPSV2-MIB", "mpsAuxParameter2"),
        ("MPSV2-MIB", "mpsTemp"),
        ("MPSV2-MIB", "mpsModuleStatus"))
)
if mibBuilder.loadTexts:
    mpU5KRX.setStatus(
        "current"
    )

mpU5KTX = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 7)
)
mpU5KTX.setObjects(
      *(("MPSV2-MIB", "mpsID"),
        ("MPSV2-MIB", "mpsPN"),
        ("MPSV2-MIB", "mpsSN"),
        ("MPSV2-MIB", "mpsOptPwrTX"),
        ("MPSV2-MIB", "mpsAuxParameter1"),
        ("MPSV2-MIB", "mpsAuxParameter2"),
        ("MPSV2-MIB", "mpsTXLaserBias"),
        ("MPSV2-MIB", "mpsDuplex"),
        ("MPSV2-MIB", "mpsLNACurrent"),
        ("MPSV2-MIB", "mpsTemp"),
        ("MPSV2-MIB", "mpsModuleStatus"))
)
if mibBuilder.loadTexts:
    mpU5KTX.setStatus(
        "current"
    )

mp2320TXE = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 8)
)
mp2320TXE.setObjects(
      *(("MPSV2-MIB", "mpsID"),
        ("MPSV2-MIB", "mpsPN"),
        ("MPSV2-MIB", "mpsSN"),
        ("MPSV2-MIB", "mpsOptPwrTX"),
        ("MPSV2-MIB", "mpsTXLaserBias"),
        ("MPSV2-MIB", "mpsDuplex"),
        ("MPSV2-MIB", "mpsLNACurrent"),
        ("MPSV2-MIB", "mpsTemp"),
        ("MPSV2-MIB", "mpsModuleStatus"))
)
if mibBuilder.loadTexts:
    mp2320TXE.setStatus(
        "current"
    )

mp2320RXE = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 9)
)
mp2320RXE.setObjects(
      *(("MPSV2-MIB", "mpsID"),
        ("MPSV2-MIB", "mpsPN"),
        ("MPSV2-MIB", "mpsSN"),
        ("MPSV2-MIB", "mpsOptPwrRX"),
        ("MPSV2-MIB", "mpsTemp"),
        ("MPSV2-MIB", "mpsModuleStatus"))
)
if mibBuilder.loadTexts:
    mp2320RXE.setStatus(
        "current"
    )

mp2320TX = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 10)
)
mp2320TX.setObjects(
    ("MPSV2-MIB", "mpsID")
)
if mibBuilder.loadTexts:
    mp2320TX.setStatus(
        "current"
    )

mp2320RX = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 11)
)
mp2320RX.setObjects(
    ("MPSV2-MIB", "mpsID")
)
if mibBuilder.loadTexts:
    mp2320RX.setStatus(
        "current"
    )

mp2320SW = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 12)
)
mp2320SW.setObjects(
      *(("MPSV2-MIB", "mpsID"),
        ("MPSV2-MIB", "mpsPN"),
        ("MPSV2-MIB", "mpsSN"),
        ("MPSV2-MIB", "mpsSwitchState"),
        ("MPSV2-MIB", "mpsTemp"),
        ("MPSV2-MIB", "mpsModuleStatus"))
)
if mibBuilder.loadTexts:
    mp2320SW.setStatus(
        "current"
    )

mp3080RX = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 13)
)
mp3080RX.setObjects(
      *(("MPSV2-MIB", "mpsID"),
        ("MPSV2-MIB", "mpsPN"),
        ("MPSV2-MIB", "mpsSN"),
        ("MPSV2-MIB", "mpsOptPwrRX"),
        ("MPSV2-MIB", "mpsAttn1"),
        ("MPSV2-MIB", "mpsAttn2"),
        ("MPSV2-MIB", "mpsVOA"),
        ("MPSV2-MIB", "mpsOptRXAGC"),
        ("MPSV2-MIB", "mpsDuplex"),
        ("MPSV2-MIB", "mpsTemp"),
        ("MPSV2-MIB", "mpsModuleStatus"))
)
if mibBuilder.loadTexts:
    mp3080RX.setStatus(
        "current"
    )

mpU5KTXRX = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 14)
)
mpU5KTXRX.setObjects(
      *(("MPSV2-MIB", "mpsID"),
        ("MPSV2-MIB", "mpsPN"),
        ("MPSV2-MIB", "mpsSN"),
        ("MPSV2-MIB", "mpsOptPwrTX"),
        ("MPSV2-MIB", "mpsOptPwrRX"),
        ("MPSV2-MIB", "mpsTXLaserBias"),
        ("MPSV2-MIB", "mpsLNACurrent"),
        ("MPSV2-MIB", "mpsAuxParameter1"),
        ("MPSV2-MIB", "mpsAuxParameter2"),
        ("MPSV2-MIB", "mpsDuplex"),
        ("MPSV2-MIB", "mpsTemp"),
        ("MPSV2-MIB", "mpsModuleStatus"))
)
if mibBuilder.loadTexts:
    mpU5KTXRX.setStatus(
        "current"
    )

mp2320TXL = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 15)
)
mp2320TXL.setObjects(
      *(("MPSV2-MIB", "mpsID"),
        ("MPSV2-MIB", "mpsPN"),
        ("MPSV2-MIB", "mpsSN"),
        ("MPSV2-MIB", "mpsOptPwrTX"),
        ("MPSV2-MIB", "mpsAttn1"),
        ("MPSV2-MIB", "mpsTXLaserBias"),
        ("MPSV2-MIB", "mpsLNACurrent"),
        ("MPSV2-MIB", "mpsAuxParameter1"),
        ("MPSV2-MIB", "mpsTemp"),
        ("MPSV2-MIB", "mpsModuleStatus"))
)
if mibBuilder.loadTexts:
    mp2320TXL.setStatus(
        "current"
    )

mp2320RXL = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 16)
)
mp2320RXL.setObjects(
      *(("MPSV2-MIB", "mpsID"),
        ("MPSV2-MIB", "mpsPN"),
        ("MPSV2-MIB", "mpsSN"),
        ("MPSV2-MIB", "mpsOptPwrRX"),
        ("MPSV2-MIB", "mpsAttn1"),
        ("MPSV2-MIB", "mpsLNACurrent"),
        ("MPSV2-MIB", "mpsTemp"),
        ("MPSV2-MIB", "mpsModuleStatus"))
)
if mibBuilder.loadTexts:
    mp2320RXL.setStatus(
        "current"
    )

controller = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44693, 1, 3, 17)
)
controller.setObjects(
      *(("MPSV2-MIB", "mpsID"),
        ("MPSV2-MIB", "mpsPN"),
        ("MPSV2-MIB", "mpsSN"),
        ("MPSV2-MIB", "mpsAuxParameter1"),
        ("MPSV2-MIB", "mpsAuxParameter2"),
        ("MPSV2-MIB", "mpsTemp"),
        ("MPSV2-MIB", "mpsModuleStatus"))
)
if mibBuilder.loadTexts:
    controller.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPSV2-MIB",
    **{"mpsMIBv2": mpsMIBv2,
       "mpsStatus": mpsStatus,
       "mpsSystem": mpsSystem,
       "mpsSystemSlotID": mpsSystemSlotID,
       "mpsSystemPN": mpsSystemPN,
       "mpsSystemSN": mpsSystemSN,
       "mpsSystemTemp": mpsSystemTemp,
       "mpsSystemFan1Current": mpsSystemFan1Current,
       "mpsSystemFan2Current": mpsSystemFan2Current,
       "mpsSystemStatus": mpsSystemStatus,
       "mpsSlot1": mpsSlot1,
       "mpsSlot1ID": mpsSlot1ID,
       "mpsSlot1PN": mpsSlot1PN,
       "mpsSlot1SN": mpsSlot1SN,
       "mpsSlot1OptPwrTX": mpsSlot1OptPwrTX,
       "mpsSlot1OptPwrRX": mpsSlot1OptPwrRX,
       "mpsSlot1Attn1": mpsSlot1Attn1,
       "mpsSlot1Attn2": mpsSlot1Attn2,
       "mpsSlot1SwitchState": mpsSlot1SwitchState,
       "mpsSlot1TXLaserBias": mpsSlot1TXLaserBias,
       "mpsSlot1BiasTState": mpsSlot1BiasTState,
       "mpsSlot1LNACurrent": mpsSlot1LNACurrent,
       "mpsSlot1VOA": mpsSlot1VOA,
       "mpsSlot1OptRXAGC": mpsSlot1OptRXAGC,
       "mpsSlot1Duplex": mpsSlot1Duplex,
       "mpsSlot1Temp": mpsSlot1Temp,
       "mpsSlot1AuxParameter1": mpsSlot1AuxParameter1,
       "mpsSlot1AuxParameter2": mpsSlot1AuxParameter2,
       "mpsSlot1Status": mpsSlot1Status,
       "mpsSlot2": mpsSlot2,
       "mpsSlot2ID": mpsSlot2ID,
       "mpsSlot2PN": mpsSlot2PN,
       "mpsSlot2SN": mpsSlot2SN,
       "mpsSlot2OptPwrTX": mpsSlot2OptPwrTX,
       "mpsSlot2OptPwrRX": mpsSlot2OptPwrRX,
       "mpsSlot2Attn1": mpsSlot2Attn1,
       "mpsSlot2Attn2": mpsSlot2Attn2,
       "mpsSlot2SwitchState": mpsSlot2SwitchState,
       "mpsSlot2TXLaserBias": mpsSlot2TXLaserBias,
       "mpsSlot2BiasTState": mpsSlot2BiasTState,
       "mpsSlot2LNACurrent": mpsSlot2LNACurrent,
       "mpsSlot2VOA": mpsSlot2VOA,
       "mpsSlot2OptRXAGC": mpsSlot2OptRXAGC,
       "mpsSlot2Duplex": mpsSlot2Duplex,
       "mpsSlot2Temp": mpsSlot2Temp,
       "mpsSlot2AuxParameter1": mpsSlot2AuxParameter1,
       "mpsSlot2AuxParameter2": mpsSlot2AuxParameter2,
       "mpsSlot2Status": mpsSlot2Status,
       "mpsSlot3": mpsSlot3,
       "mpsSlot3ID": mpsSlot3ID,
       "mpsSlot3PN": mpsSlot3PN,
       "mpsSlot3SN": mpsSlot3SN,
       "mpsSlot3OptPwrTX": mpsSlot3OptPwrTX,
       "mpsSlot3OptPwrRX": mpsSlot3OptPwrRX,
       "mpsSlot3Attn1": mpsSlot3Attn1,
       "mpsSlot3Attn2": mpsSlot3Attn2,
       "mpsSlot3SwitchState": mpsSlot3SwitchState,
       "mpsSlot3TXLaserBias": mpsSlot3TXLaserBias,
       "mpsSlot3BiasTState": mpsSlot3BiasTState,
       "mpsSlot3LNACurrent": mpsSlot3LNACurrent,
       "mpsSlot3VOA": mpsSlot3VOA,
       "mpsSlot3OptRXAGC": mpsSlot3OptRXAGC,
       "mpsSlot3Duplex": mpsSlot3Duplex,
       "mpsSlot3Temp": mpsSlot3Temp,
       "mpsSlot3AuxParameter1": mpsSlot3AuxParameter1,
       "mpsSlot3AuxParameter2": mpsSlot3AuxParameter2,
       "mpsSlot3Status": mpsSlot3Status,
       "mpsSlot4": mpsSlot4,
       "mpsSlot4ID": mpsSlot4ID,
       "mpsSlot4PN": mpsSlot4PN,
       "mpsSlot4SN": mpsSlot4SN,
       "mpsSlot4OptPwrTX": mpsSlot4OptPwrTX,
       "mpsSlot4OptPwrRX": mpsSlot4OptPwrRX,
       "mpsSlot4Attn1": mpsSlot4Attn1,
       "mpsSlot4Attn2": mpsSlot4Attn2,
       "mpsSlot4SwitchState": mpsSlot4SwitchState,
       "mpsSlot4TXLaserBias": mpsSlot4TXLaserBias,
       "mpsSlot4BiasTState": mpsSlot4BiasTState,
       "mpsSlot4LNACurrent": mpsSlot4LNACurrent,
       "mpsSlot4VOA": mpsSlot4VOA,
       "mpsSlot4OptRXAGC": mpsSlot4OptRXAGC,
       "mpsSlot4Duplex": mpsSlot4Duplex,
       "mpsSlot4Temp": mpsSlot4Temp,
       "mpsSlot4AuxParameter1": mpsSlot4AuxParameter1,
       "mpsSlot4AuxParameter2": mpsSlot4AuxParameter2,
       "mpsSlot4Status": mpsSlot4Status,
       "mpsSlot5": mpsSlot5,
       "mpsSlot5ID": mpsSlot5ID,
       "mpsSlot5PN": mpsSlot5PN,
       "mpsSlot5SN": mpsSlot5SN,
       "mpsSlot5OptPwrTX": mpsSlot5OptPwrTX,
       "mpsSlot5OptPwrRX": mpsSlot5OptPwrRX,
       "mpsSlot5Attn1": mpsSlot5Attn1,
       "mpsSlot5Attn2": mpsSlot5Attn2,
       "mpsSlot5SwitchState": mpsSlot5SwitchState,
       "mpsSlot5TXLaserBias": mpsSlot5TXLaserBias,
       "mpsSlot5BiasTState": mpsSlot5BiasTState,
       "mpsSlot5LNACurrent": mpsSlot5LNACurrent,
       "mpsSlot5VOA": mpsSlot5VOA,
       "mpsSlot5OptRXAGC": mpsSlot5OptRXAGC,
       "mpsSlot5Duplex": mpsSlot5Duplex,
       "mpsSlot5Temp": mpsSlot5Temp,
       "mpsSlot5AuxParameter1": mpsSlot5AuxParameter1,
       "mpsSlot5AuxParameter2": mpsSlot5AuxParameter2,
       "mpsSlot5Status": mpsSlot5Status,
       "mpsSlot6": mpsSlot6,
       "mpsSlot6ID": mpsSlot6ID,
       "mpsSlot6PN": mpsSlot6PN,
       "mpsSlot6SN": mpsSlot6SN,
       "mpsSlot6OptPwrTX": mpsSlot6OptPwrTX,
       "mpsSlot6OptPwrRX": mpsSlot6OptPwrRX,
       "mpsSlot6Attn1": mpsSlot6Attn1,
       "mpsSlot6Attn2": mpsSlot6Attn2,
       "mpsSlot6SwitchState": mpsSlot6SwitchState,
       "mpsSlot6TXLaserBias": mpsSlot6TXLaserBias,
       "mpsSlot6BiasTState": mpsSlot6BiasTState,
       "mpsSlot6LNACurrent": mpsSlot6LNACurrent,
       "mpsSlot6VOA": mpsSlot6VOA,
       "mpsSlot6OptRXAGC": mpsSlot6OptRXAGC,
       "mpsSlot6Duplex": mpsSlot6Duplex,
       "mpsSlot6Temp": mpsSlot6Temp,
       "mpsSlot6AuxParameter1": mpsSlot6AuxParameter1,
       "mpsSlot6AuxParameter2": mpsSlot6AuxParameter2,
       "mpsSlot6Status": mpsSlot6Status,
       "mpsSlot7": mpsSlot7,
       "mpsSlot7ID": mpsSlot7ID,
       "mpsSlot7PN": mpsSlot7PN,
       "mpsSlot7SN": mpsSlot7SN,
       "mpsSlot7OptPwrTX": mpsSlot7OptPwrTX,
       "mpsSlot7OptPwrRX": mpsSlot7OptPwrRX,
       "mpsSlot7Attn1": mpsSlot7Attn1,
       "mpsSlot7Attn2": mpsSlot7Attn2,
       "mpsSlot7SwitchState": mpsSlot7SwitchState,
       "mpsSlot7TXLaserBias": mpsSlot7TXLaserBias,
       "mpsSlot7BiasTState": mpsSlot7BiasTState,
       "mpsSlot7LNACurrent": mpsSlot7LNACurrent,
       "mpsSlot7VOA": mpsSlot7VOA,
       "mpsSlot7OptRXAGC": mpsSlot7OptRXAGC,
       "mpsSlot7Duplex": mpsSlot7Duplex,
       "mpsSlot7Temp": mpsSlot7Temp,
       "mpsSlot7AuxParameter1": mpsSlot7AuxParameter1,
       "mpsSlot7AuxParameter2": mpsSlot7AuxParameter2,
       "mpsSlot7Status": mpsSlot7Status,
       "mpsSlot8": mpsSlot8,
       "mpsSlot8ID": mpsSlot8ID,
       "mpsSlot8PN": mpsSlot8PN,
       "mpsSlot8SN": mpsSlot8SN,
       "mpsSlot8OptPwrTX": mpsSlot8OptPwrTX,
       "mpsSlot8OptPwrRX": mpsSlot8OptPwrRX,
       "mpsSlot8Attn1": mpsSlot8Attn1,
       "mpsSlot8Attn2": mpsSlot8Attn2,
       "mpsSlot8SwitchState": mpsSlot8SwitchState,
       "mpsSlot8TXLaserBias": mpsSlot8TXLaserBias,
       "mpsSlot8BiasTState": mpsSlot8BiasTState,
       "mpsSlot8LNACurrent": mpsSlot8LNACurrent,
       "mpsSlot8VOA": mpsSlot8VOA,
       "mpsSlot8OptRXAGC": mpsSlot8OptRXAGC,
       "mpsSlot8Duplex": mpsSlot8Duplex,
       "mpsSlot8Temp": mpsSlot8Temp,
       "mpsSlot8AuxParameter1": mpsSlot8AuxParameter1,
       "mpsSlot8AuxParameter2": mpsSlot8AuxParameter2,
       "mpsSlot8Status": mpsSlot8Status,
       "mpsSlot9": mpsSlot9,
       "mpsSlot9ID": mpsSlot9ID,
       "mpsSlot9PN": mpsSlot9PN,
       "mpsSlot9SN": mpsSlot9SN,
       "mpsSlot9OptPwrTX": mpsSlot9OptPwrTX,
       "mpsSlot9OptPwrRX": mpsSlot9OptPwrRX,
       "mpsSlot9Attn1": mpsSlot9Attn1,
       "mpsSlot9Attn2": mpsSlot9Attn2,
       "mpsSlot9SwitchState": mpsSlot9SwitchState,
       "mpsSlot9TXLaserBias": mpsSlot9TXLaserBias,
       "mpsSlot9BiasTState": mpsSlot9BiasTState,
       "mpsSlot9LNACurrent": mpsSlot9LNACurrent,
       "mpsSlot9VOA": mpsSlot9VOA,
       "mpsSlot9OptRXAGC": mpsSlot9OptRXAGC,
       "mpsSlot9Duplex": mpsSlot9Duplex,
       "mpsSlot9Temp": mpsSlot9Temp,
       "mpsSlot9AuxParameter1": mpsSlot9AuxParameter1,
       "mpsSlot9AuxParameter2": mpsSlot9AuxParameter2,
       "mpsSlot9Status": mpsSlot9Status,
       "mpsSlot10": mpsSlot10,
       "mpsSlot10ID": mpsSlot10ID,
       "mpsSlot10PN": mpsSlot10PN,
       "mpsSlot10SN": mpsSlot10SN,
       "mpsSlot10OptPwrTX": mpsSlot10OptPwrTX,
       "mpsSlot10OptPwrRX": mpsSlot10OptPwrRX,
       "mpsSlot10Attn1": mpsSlot10Attn1,
       "mpsSlot10Attn2": mpsSlot10Attn2,
       "mpsSlot10SwitchState": mpsSlot10SwitchState,
       "mpsSlot10TXLaserBias": mpsSlot10TXLaserBias,
       "mpsSlot10BiasTState": mpsSlot10BiasTState,
       "mpsSlot10LNACurrent": mpsSlot10LNACurrent,
       "mpsSlot10VOA": mpsSlot10VOA,
       "mpsSlot10OptRXAGC": mpsSlot10OptRXAGC,
       "mpsSlot10Duplex": mpsSlot10Duplex,
       "mpsSlot10Temp": mpsSlot10Temp,
       "mpsSlot10AuxParameter1": mpsSlot10AuxParameter1,
       "mpsSlot10AuxParameter2": mpsSlot10AuxParameter2,
       "mpsSlot10Status": mpsSlot10Status,
       "mpsParameterGroups": mpsParameterGroups,
       "mpsID": mpsID,
       "mpsPN": mpsPN,
       "mpsSN": mpsSN,
       "mpsOptPwrTX": mpsOptPwrTX,
       "mpsOptPwrRX": mpsOptPwrRX,
       "mpsAttn1": mpsAttn1,
       "mpsAttn2": mpsAttn2,
       "mpsSwitchState": mpsSwitchState,
       "mpsTXLaserBias": mpsTXLaserBias,
       "mpsBiasTState": mpsBiasTState,
       "mpsLNACurrent": mpsLNACurrent,
       "mpsVOA": mpsVOA,
       "mpsOptRXAGC": mpsOptRXAGC,
       "mpsDuplex": mpsDuplex,
       "mpsTemp": mpsTemp,
       "mpsAuxParameter1": mpsAuxParameter1,
       "mpsAuxParameter2": mpsAuxParameter2,
       "mpsModuleStatus": mpsModuleStatus,
       "mpsModuleCompliance": mpsModuleCompliance,
       "mp2320RXI": mp2320RXI,
       "mp2320TXF": mp2320TXF,
       "mp2320PRE": mp2320PRE,
       "mp2320ASW": mp2320ASW,
       "mpEthernet": mpEthernet,
       "mpU5KRX": mpU5KRX,
       "mpU5KTX": mpU5KTX,
       "mp2320TXE": mp2320TXE,
       "mp2320RXE": mp2320RXE,
       "mp2320TX": mp2320TX,
       "mp2320RX": mp2320RX,
       "mp2320SW": mp2320SW,
       "mp3080RX": mp3080RX,
       "mpU5KTXRX": mpU5KTXRX,
       "mp2320TXL": mp2320TXL,
       "mp2320RXL": mp2320RXL,
       "controller": controller}
)
