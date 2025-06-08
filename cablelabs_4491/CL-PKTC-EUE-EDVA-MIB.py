# SNMP MIB module (CL-PKTC-EUE-EDVA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/CL-PKTC-EUE-EDVA-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:37:34 2025
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

(pktcEUEDeviceMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcEUEDeviceMibs")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pktcEDVAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    pktcEDVAMIB.setRevisions(
        ("2010-04-26 00:00",
         "2008-07-10 00:00",
         "2007-11-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PktcEUETCLocInfoType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locInfoCivic", 1),
          ("locInfoGeo", 2))
    )



class PktcEUETCLocInfo(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_PktcEDVANotification_ObjectIdentity = ObjectIdentity
pktcEDVANotification = _PktcEDVANotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 0)
)
_PktcEDVAObjects_ObjectIdentity = ObjectIdentity
pktcEDVAObjects = _PktcEDVAObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1)
)
_PktcEDVAProfile_ObjectIdentity = ObjectIdentity
pktcEDVAProfile = _PktcEDVAProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 1)
)


class _PktcEDVAProfileVersion_Type(SnmpAdminString):
    """Custom type pktcEDVAProfileVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_PktcEDVAProfileVersion_Type.__name__ = "SnmpAdminString"
_PktcEDVAProfileVersion_Object = MibScalar
pktcEDVAProfileVersion = _PktcEDVAProfileVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 1, 1),
    _PktcEDVAProfileVersion_Type()
)
pktcEDVAProfileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEDVAProfileVersion.setStatus("current")
_PktcEDVALineNumberCount_Type = Unsigned32
_PktcEDVALineNumberCount_Object = MibScalar
pktcEDVALineNumberCount = _PktcEDVALineNumberCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 2),
    _PktcEDVALineNumberCount_Type()
)
pktcEDVALineNumberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEDVALineNumberCount.setStatus("current")
_PktcEDVANetDiscProfile_ObjectIdentity = ObjectIdentity
pktcEDVANetDiscProfile = _PktcEDVANetDiscProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 3)
)
_PktcEDVANetDiscTable_Object = MibTable
pktcEDVANetDiscTable = _PktcEDVANetDiscTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pktcEDVANetDiscTable.setStatus("current")
_PktcEDVANetDiscEntry_Object = MibTableRow
pktcEDVANetDiscEntry = _PktcEDVANetDiscEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 3, 1, 1)
)
pktcEDVANetDiscEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcEDVANetDiscEntry.setStatus("current")


class _PktcEDVANetDisc_Type(Integer32):
    """Custom type pktcEDVANetDisc based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_PktcEDVANetDisc_Type.__name__ = "Integer32"
_PktcEDVANetDisc_Object = MibTableColumn
pktcEDVANetDisc = _PktcEDVANetDisc_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 3, 1, 1, 1),
    _PktcEDVANetDisc_Type()
)
pktcEDVANetDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVANetDisc.setStatus("current")
if mibBuilder.loadTexts:
    pktcEDVANetDisc.setUnits("milliseconds")
_PktcEDVAAnsSupProfile_ObjectIdentity = ObjectIdentity
pktcEDVAAnsSupProfile = _PktcEDVAAnsSupProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 4)
)
_PktcEDVAAnsSupTable_Object = MibTable
pktcEDVAAnsSupTable = _PktcEDVAAnsSupTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    pktcEDVAAnsSupTable.setStatus("current")
_PktcEDVAAnsSupEntry_Object = MibTableRow
pktcEDVAAnsSupEntry = _PktcEDVAAnsSupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 4, 1, 1)
)
pktcEDVAAnsSupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcEDVAAnsSupEntry.setStatus("current")


class _PktcEDVAAnsSup_Type(TruthValue):
    """Custom type pktcEDVAAnsSup based on TruthValue"""
    defaultValue = 2


_PktcEDVAAnsSup_Type.__name__ = "TruthValue"
_PktcEDVAAnsSup_Object = MibTableColumn
pktcEDVAAnsSup = _PktcEDVAAnsSup_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 4, 1, 1, 1),
    _PktcEDVAAnsSup_Type()
)
pktcEDVAAnsSup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVAAnsSup.setStatus("current")
_PktcEDVADtmfProfile_ObjectIdentity = ObjectIdentity
pktcEDVADtmfProfile = _PktcEDVADtmfProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 5)
)


class _PktcEDVADtmfRelay_Type(TruthValue):
    """Custom type pktcEDVADtmfRelay based on TruthValue"""
    defaultValue = 1


_PktcEDVADtmfRelay_Type.__name__ = "TruthValue"
_PktcEDVADtmfRelay_Object = MibScalar
pktcEDVADtmfRelay = _PktcEDVADtmfRelay_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 5, 1),
    _PktcEDVADtmfRelay_Type()
)
pktcEDVADtmfRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVADtmfRelay.setStatus("current")
_PktcEDVAEndPointCfgProfile_ObjectIdentity = ObjectIdentity
pktcEDVAEndPointCfgProfile = _PktcEDVAEndPointCfgProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 6)
)
_PktcEDVAEndPntConfigTable_Object = MibTable
pktcEDVAEndPntConfigTable = _PktcEDVAEndPntConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    pktcEDVAEndPntConfigTable.setStatus("current")
_PktcEDVAEndPntConfigEntry_Object = MibTableRow
pktcEDVAEndPntConfigEntry = _PktcEDVAEndPntConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 6, 1, 1)
)
pktcEDVAEndPntConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcEDVAEndPntConfigEntry.setStatus("current")


class _PktcEDVAEndPntDtmfMinPlayout_Type(Unsigned32):
    """Custom type pktcEDVAEndPntDtmfMinPlayout based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 100),
    )


_PktcEDVAEndPntDtmfMinPlayout_Type.__name__ = "Unsigned32"
_PktcEDVAEndPntDtmfMinPlayout_Object = MibTableColumn
pktcEDVAEndPntDtmfMinPlayout = _PktcEDVAEndPntDtmfMinPlayout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 6, 1, 1, 1),
    _PktcEDVAEndPntDtmfMinPlayout_Type()
)
pktcEDVAEndPntDtmfMinPlayout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVAEndPntDtmfMinPlayout.setStatus("current")
if mibBuilder.loadTexts:
    pktcEDVAEndPntDtmfMinPlayout.setUnits("milliseconds")


class _PktcEDVAEndPntHookState_Type(Integer32):
    """Custom type pktcEDVAEndPntHookState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onHook", 1),
          ("onHookWithActivity", 2),
          ("offHook", 3))
    )


_PktcEDVAEndPntHookState_Type.__name__ = "Integer32"
_PktcEDVAEndPntHookState_Object = MibTableColumn
pktcEDVAEndPntHookState = _PktcEDVAEndPntHookState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 6, 1, 1, 2),
    _PktcEDVAEndPntHookState_Type()
)
pktcEDVAEndPntHookState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEDVAEndPntHookState.setStatus("current")


class _PktcEDVAEndPntFaxDetection_Type(TruthValue):
    """Custom type pktcEDVAEndPntFaxDetection based on TruthValue"""
    defaultValue = 2


_PktcEDVAEndPntFaxDetection_Type.__name__ = "TruthValue"
_PktcEDVAEndPntFaxDetection_Object = MibTableColumn
pktcEDVAEndPntFaxDetection = _PktcEDVAEndPntFaxDetection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 6, 1, 1, 3),
    _PktcEDVAEndPntFaxDetection_Type()
)
pktcEDVAEndPntFaxDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVAEndPntFaxDetection.setStatus("current")


class _PktcEDVAEndPntQosPreconditions_Type(Integer32):
    """Custom type pktcEDVAEndPntQosPreconditions based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("required", 1),
          ("supported", 2),
          ("disabled", 3))
    )


_PktcEDVAEndPntQosPreconditions_Type.__name__ = "Integer32"
_PktcEDVAEndPntQosPreconditions_Object = MibTableColumn
pktcEDVAEndPntQosPreconditions = _PktcEDVAEndPntQosPreconditions_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 6, 1, 1, 4),
    _PktcEDVAEndPntQosPreconditions_Type()
)
pktcEDVAEndPntQosPreconditions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVAEndPntQosPreconditions.setStatus("current")
_PktcEDVAPrLossProfile_ObjectIdentity = ObjectIdentity
pktcEDVAPrLossProfile = _PktcEDVAPrLossProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 7)
)
_PktcEDVAPrLossTable_Object = MibTable
pktcEDVAPrLossTable = _PktcEDVAPrLossTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    pktcEDVAPrLossTable.setStatus("current")
_PktcEDVAPrLossEntry_Object = MibTableRow
pktcEDVAPrLossEntry = _PktcEDVAPrLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 7, 1, 1)
)
pktcEDVAPrLossEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcEDVAPrLossEntry.setStatus("current")


class _PktcEDVAPrLossDA_Type(Integer32):
    """Custom type pktcEDVAPrLossDA based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_PktcEDVAPrLossDA_Type.__name__ = "Integer32"
_PktcEDVAPrLossDA_Object = MibTableColumn
pktcEDVAPrLossDA = _PktcEDVAPrLossDA_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 7, 1, 1, 1),
    _PktcEDVAPrLossDA_Type()
)
pktcEDVAPrLossDA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVAPrLossDA.setStatus("current")
if mibBuilder.loadTexts:
    pktcEDVAPrLossDA.setUnits("dB")


class _PktcEDVAPrLossAD_Type(Integer32):
    """Custom type pktcEDVAPrLossAD based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_PktcEDVAPrLossAD_Type.__name__ = "Integer32"
_PktcEDVAPrLossAD_Object = MibTableColumn
pktcEDVAPrLossAD = _PktcEDVAPrLossAD_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 7, 1, 1, 2),
    _PktcEDVAPrLossAD_Type()
)
pktcEDVAPrLossAD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVAPrLossAD.setStatus("current")
if mibBuilder.loadTexts:
    pktcEDVAPrLossAD.setUnits("dB")
_PktcEDVAMWIProfile_ObjectIdentity = ObjectIdentity
pktcEDVAMWIProfile = _PktcEDVAMWIProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 8)
)
_PktcEDVAMWISignalTypesTable_Object = MibTable
pktcEDVAMWISignalTypesTable = _PktcEDVAMWISignalTypesTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    pktcEDVAMWISignalTypesTable.setStatus("current")
_PktcEDVAMWISignalTypesEntry_Object = MibTableRow
pktcEDVAMWISignalTypesEntry = _PktcEDVAMWISignalTypesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 8, 1, 1)
)
pktcEDVAMWISignalTypesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcEDVAMWISignalTypesEntry.setStatus("current")


class _PktcEDVAMwiOnHook_Type(Integer32):
    """Custom type pktcEDVAMwiOnHook based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mwiFskInd", 1),
          ("mwiDtmfInd", 2))
    )


_PktcEDVAMwiOnHook_Type.__name__ = "Integer32"
_PktcEDVAMwiOnHook_Object = MibTableColumn
pktcEDVAMwiOnHook = _PktcEDVAMwiOnHook_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 8, 1, 1, 1),
    _PktcEDVAMwiOnHook_Type()
)
pktcEDVAMwiOnHook.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVAMwiOnHook.setStatus("current")


class _PktcEDVAMwiOffHook_Type(Integer32):
    """Custom type pktcEDVAMwiOffHook based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mwiToneInd", 1),
          ("mwiAncInd", 2))
    )


_PktcEDVAMwiOffHook_Type.__name__ = "Integer32"
_PktcEDVAMwiOffHook_Object = MibTableColumn
pktcEDVAMwiOffHook = _PktcEDVAMwiOffHook_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 8, 1, 1, 2),
    _PktcEDVAMwiOffHook_Type()
)
pktcEDVAMwiOffHook.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVAMwiOffHook.setStatus("current")
_PktcEDVACodecProfile_ObjectIdentity = ObjectIdentity
pktcEDVACodecProfile = _PktcEDVACodecProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 9)
)


class _PktcEDVACodecG711Pkt_Type(Integer32):
    """Custom type pktcEDVACodecG711Pkt based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
    )


_PktcEDVACodecG711Pkt_Type.__name__ = "Integer32"
_PktcEDVACodecG711Pkt_Object = MibScalar
pktcEDVACodecG711Pkt = _PktcEDVACodecG711Pkt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 9, 1),
    _PktcEDVACodecG711Pkt_Type()
)
pktcEDVACodecG711Pkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVACodecG711Pkt.setStatus("current")
if mibBuilder.loadTexts:
    pktcEDVACodecG711Pkt.setUnits("milliseconds")


class _PktcEDVACodecT38_Type(TruthValue):
    """Custom type pktcEDVACodecT38 based on TruthValue"""
    defaultValue = 1


_PktcEDVACodecT38_Type.__name__ = "TruthValue"
_PktcEDVACodecT38_Object = MibScalar
pktcEDVACodecT38 = _PktcEDVACodecT38_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 9, 2),
    _PktcEDVACodecT38_Type()
)
pktcEDVACodecT38.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVACodecT38.setStatus("current")


class _PktcEDVACodecV152_Type(TruthValue):
    """Custom type pktcEDVACodecV152 based on TruthValue"""
    defaultValue = 1


_PktcEDVACodecV152_Type.__name__ = "TruthValue"
_PktcEDVACodecV152_Object = MibScalar
pktcEDVACodecV152 = _PktcEDVACodecV152_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 9, 3),
    _PktcEDVACodecV152_Type()
)
pktcEDVACodecV152.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVACodecV152.setStatus("current")
_PktcEDVACodecPubRepAddrType_Type = InetAddressType
_PktcEDVACodecPubRepAddrType_Object = MibScalar
pktcEDVACodecPubRepAddrType = _PktcEDVACodecPubRepAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 9, 4),
    _PktcEDVACodecPubRepAddrType_Type()
)
pktcEDVACodecPubRepAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVACodecPubRepAddrType.setStatus("current")
_PktcEDVACodecPubRepAddr_Type = InetAddress
_PktcEDVACodecPubRepAddr_Object = MibScalar
pktcEDVACodecPubRepAddr = _PktcEDVACodecPubRepAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 9, 5),
    _PktcEDVACodecPubRepAddr_Type()
)
pktcEDVACodecPubRepAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVACodecPubRepAddr.setStatus("current")


class _PktcEDVACodecRTCPXR_Type(TruthValue):
    """Custom type pktcEDVACodecRTCPXR based on TruthValue"""
    defaultValue = 1


_PktcEDVACodecRTCPXR_Type.__name__ = "TruthValue"
_PktcEDVACodecRTCPXR_Object = MibScalar
pktcEDVACodecRTCPXR = _PktcEDVACodecRTCPXR_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 9, 6),
    _PktcEDVACodecRTCPXR_Type()
)
pktcEDVACodecRTCPXR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVACodecRTCPXR.setStatus("current")


class _PktcEDVACodecRTCPRate_Type(Integer32):
    """Custom type pktcEDVACodecRTCPRate based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_PktcEDVACodecRTCPRate_Type.__name__ = "Integer32"
_PktcEDVACodecRTCPRate_Object = MibScalar
pktcEDVACodecRTCPRate = _PktcEDVACodecRTCPRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 9, 7),
    _PktcEDVACodecRTCPRate_Type()
)
pktcEDVACodecRTCPRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVACodecRTCPRate.setStatus("current")
if mibBuilder.loadTexts:
    pktcEDVACodecRTCPRate.setUnits("seconds")
_PktcEDVAAnnounceProfile_ObjectIdentity = ObjectIdentity
pktcEDVAAnnounceProfile = _PktcEDVAAnnounceProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 10)
)
_PktcEDVAToneIdentifier_Type = OctetString
_PktcEDVAToneIdentifier_Object = MibScalar
pktcEDVAToneIdentifier = _PktcEDVAToneIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 10, 1),
    _PktcEDVAToneIdentifier_Type()
)
pktcEDVAToneIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVAToneIdentifier.setStatus("current")
_PktcEDVAAudioAnnounceId_Type = OctetString
_PktcEDVAAudioAnnounceId_Object = MibScalar
pktcEDVAAudioAnnounceId = _PktcEDVAAudioAnnounceId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 10, 2),
    _PktcEDVAAudioAnnounceId_Type()
)
pktcEDVAAudioAnnounceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVAAudioAnnounceId.setStatus("current")
_PktcEDVALocInfoProfile_ObjectIdentity = ObjectIdentity
pktcEDVALocInfoProfile = _PktcEDVALocInfoProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 11)
)
_PktcEDVALocationInfoPref_Type = PktcEUETCLocInfoType
_PktcEDVALocationInfoPref_Object = MibScalar
pktcEDVALocationInfoPref = _PktcEDVALocationInfoPref_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 11, 1),
    _PktcEDVALocationInfoPref_Type()
)
pktcEDVALocationInfoPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEDVALocationInfoPref.setStatus("current")
_PktcEDVALocationInfoType_Type = PktcEUETCLocInfoType
_PktcEDVALocationInfoType_Object = MibScalar
pktcEDVALocationInfoType = _PktcEDVALocationInfoType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 11, 2),
    _PktcEDVALocationInfoType_Type()
)
pktcEDVALocationInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEDVALocationInfoType.setStatus("current")
_PktcEDVALocationInfo_Type = PktcEUETCLocInfo
_PktcEDVALocationInfo_Object = MibScalar
pktcEDVALocationInfo = _PktcEDVALocationInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 11, 3),
    _PktcEDVALocationInfo_Type()
)
pktcEDVALocationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEDVALocationInfo.setStatus("current")
_PktcEDVAConformance_ObjectIdentity = ObjectIdentity
pktcEDVAConformance = _PktcEDVAConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 2)
)
_PktcEDVACompliances_ObjectIdentity = ObjectIdentity
pktcEDVACompliances = _PktcEDVACompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 2, 1)
)
_PktcEDVAGroups_ObjectIdentity = ObjectIdentity
pktcEDVAGroups = _PktcEDVAGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 2, 2)
)

# Managed Objects groups

pktcEDVAProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 2, 2, 1)
)
pktcEDVAProfileGroup.setObjects(
    ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVAProfileVersion")
)
if mibBuilder.loadTexts:
    pktcEDVAProfileGroup.setStatus("current")

pktcEDVAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 2, 2, 2)
)
pktcEDVAGroup.setObjects(
      *(("CL-PKTC-EUE-EDVA-MIB", "pktcEDVALineNumberCount"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVANetDisc"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVAAnsSup"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVADtmfRelay"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVAPrLossDA"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVAPrLossAD"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVAMwiOnHook"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVAMwiOffHook"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVACodecG711Pkt"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVACodecT38"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVACodecV152"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVACodecPubRepAddrType"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVACodecPubRepAddr"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVACodecRTCPXR"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVACodecRTCPRate"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVAToneIdentifier"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVAAudioAnnounceId"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVAEndPntDtmfMinPlayout"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVAEndPntHookState"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVAEndPntFaxDetection"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVAEndPntQosPreconditions"))
)
if mibBuilder.loadTexts:
    pktcEDVAGroup.setStatus("current")

pktcEDVADeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 2, 2, 3)
)
pktcEDVADeprecatedGroup.setObjects(
      *(("CL-PKTC-EUE-EDVA-MIB", "pktcEDVAToneIdentifier"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVAAudioAnnounceId"))
)
if mibBuilder.loadTexts:
    pktcEDVADeprecatedGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcEDVACompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 2, 1, 1)
)
pktcEDVACompliance.setObjects(
      *(("CL-PKTC-EUE-EDVA-MIB", "pktcEDVAProfileGroup"),
        ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVAGroup"))
)
if mibBuilder.loadTexts:
    pktcEDVACompliance.setStatus(
        "current"
    )

pktcEDVADeprecatedCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 2, 1, 2)
)
pktcEDVADeprecatedCompliance.setObjects(
    ("CL-PKTC-EUE-EDVA-MIB", "pktcEDVADeprecatedGroup")
)
if mibBuilder.loadTexts:
    pktcEDVADeprecatedCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CL-PKTC-EUE-EDVA-MIB",
    **{"PktcEUETCLocInfoType": PktcEUETCLocInfoType,
       "PktcEUETCLocInfo": PktcEUETCLocInfo,
       "pktcEDVAMIB": pktcEDVAMIB,
       "pktcEDVANotification": pktcEDVANotification,
       "pktcEDVAObjects": pktcEDVAObjects,
       "pktcEDVAProfile": pktcEDVAProfile,
       "pktcEDVAProfileVersion": pktcEDVAProfileVersion,
       "pktcEDVALineNumberCount": pktcEDVALineNumberCount,
       "pktcEDVANetDiscProfile": pktcEDVANetDiscProfile,
       "pktcEDVANetDiscTable": pktcEDVANetDiscTable,
       "pktcEDVANetDiscEntry": pktcEDVANetDiscEntry,
       "pktcEDVANetDisc": pktcEDVANetDisc,
       "pktcEDVAAnsSupProfile": pktcEDVAAnsSupProfile,
       "pktcEDVAAnsSupTable": pktcEDVAAnsSupTable,
       "pktcEDVAAnsSupEntry": pktcEDVAAnsSupEntry,
       "pktcEDVAAnsSup": pktcEDVAAnsSup,
       "pktcEDVADtmfProfile": pktcEDVADtmfProfile,
       "pktcEDVADtmfRelay": pktcEDVADtmfRelay,
       "pktcEDVAEndPointCfgProfile": pktcEDVAEndPointCfgProfile,
       "pktcEDVAEndPntConfigTable": pktcEDVAEndPntConfigTable,
       "pktcEDVAEndPntConfigEntry": pktcEDVAEndPntConfigEntry,
       "pktcEDVAEndPntDtmfMinPlayout": pktcEDVAEndPntDtmfMinPlayout,
       "pktcEDVAEndPntHookState": pktcEDVAEndPntHookState,
       "pktcEDVAEndPntFaxDetection": pktcEDVAEndPntFaxDetection,
       "pktcEDVAEndPntQosPreconditions": pktcEDVAEndPntQosPreconditions,
       "pktcEDVAPrLossProfile": pktcEDVAPrLossProfile,
       "pktcEDVAPrLossTable": pktcEDVAPrLossTable,
       "pktcEDVAPrLossEntry": pktcEDVAPrLossEntry,
       "pktcEDVAPrLossDA": pktcEDVAPrLossDA,
       "pktcEDVAPrLossAD": pktcEDVAPrLossAD,
       "pktcEDVAMWIProfile": pktcEDVAMWIProfile,
       "pktcEDVAMWISignalTypesTable": pktcEDVAMWISignalTypesTable,
       "pktcEDVAMWISignalTypesEntry": pktcEDVAMWISignalTypesEntry,
       "pktcEDVAMwiOnHook": pktcEDVAMwiOnHook,
       "pktcEDVAMwiOffHook": pktcEDVAMwiOffHook,
       "pktcEDVACodecProfile": pktcEDVACodecProfile,
       "pktcEDVACodecG711Pkt": pktcEDVACodecG711Pkt,
       "pktcEDVACodecT38": pktcEDVACodecT38,
       "pktcEDVACodecV152": pktcEDVACodecV152,
       "pktcEDVACodecPubRepAddrType": pktcEDVACodecPubRepAddrType,
       "pktcEDVACodecPubRepAddr": pktcEDVACodecPubRepAddr,
       "pktcEDVACodecRTCPXR": pktcEDVACodecRTCPXR,
       "pktcEDVACodecRTCPRate": pktcEDVACodecRTCPRate,
       "pktcEDVAAnnounceProfile": pktcEDVAAnnounceProfile,
       "pktcEDVAToneIdentifier": pktcEDVAToneIdentifier,
       "pktcEDVAAudioAnnounceId": pktcEDVAAudioAnnounceId,
       "pktcEDVALocInfoProfile": pktcEDVALocInfoProfile,
       "pktcEDVALocationInfoPref": pktcEDVALocationInfoPref,
       "pktcEDVALocationInfoType": pktcEDVALocationInfoType,
       "pktcEDVALocationInfo": pktcEDVALocationInfo,
       "pktcEDVAConformance": pktcEDVAConformance,
       "pktcEDVACompliances": pktcEDVACompliances,
       "pktcEDVACompliance": pktcEDVACompliance,
       "pktcEDVADeprecatedCompliance": pktcEDVADeprecatedCompliance,
       "pktcEDVAGroups": pktcEDVAGroups,
       "pktcEDVAProfileGroup": pktcEDVAProfileGroup,
       "pktcEDVAGroup": pktcEDVAGroup,
       "pktcEDVADeprecatedGroup": pktcEDVADeprecatedGroup}
)
