# SNMP MIB module (ALITER-UPS2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/aliter_42333/ALITER-UPS2-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:22:24 2025
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aliter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42333)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PsuSnmpVer(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpOff", 0),
          ("useSnmpV2c", 1),
          ("useSnmpV3", 3))
    )



class PsuTrapType(TextualConvention, Integer32):
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
        *(("disabled", 0),
          ("trap", 1),
          ("inform", 2))
    )



class Status(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AtComtanet_ObjectIdentity = ObjectIdentity
atComtanet = _AtComtanet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42333, 10)
)
_AtUPS2_ObjectIdentity = ObjectIdentity
atUPS2 = _AtUPS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2)
)


class _Ups2ObjectID_Type(OctetString):
    """Custom type ups2ObjectID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Ups2ObjectID_Type.__name__ = "OctetString"
_Ups2ObjectID_Object = MibScalar
ups2ObjectID = _Ups2ObjectID_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 1),
    _Ups2ObjectID_Type()
)
ups2ObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ups2ObjectID.setStatus("current")
_Ups2NETpar_ObjectIdentity = ObjectIdentity
ups2NETpar = _Ups2NETpar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 2)
)
_PUseDHCP_Type = Status
_PUseDHCP_Object = MibScalar
pUseDHCP = _PUseDHCP_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 2, 1),
    _PUseDHCP_Type()
)
pUseDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pUseDHCP.setStatus("current")
_PIPAddr_Type = IpAddress
_PIPAddr_Object = MibScalar
pIPAddr = _PIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 2, 2),
    _PIPAddr_Type()
)
pIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pIPAddr.setStatus("current")
_PIPMask_Type = IpAddress
_PIPMask_Object = MibScalar
pIPMask = _PIPMask_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 2, 3),
    _PIPMask_Type()
)
pIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pIPMask.setStatus("current")
_PIPGtw_Type = IpAddress
_PIPGtw_Object = MibScalar
pIPGtw = _PIPGtw_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 2, 4),
    _PIPGtw_Type()
)
pIPGtw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pIPGtw.setStatus("current")
_PIPDNS1_Type = Integer32
_PIPDNS1_Object = MibScalar
pIPDNS1 = _PIPDNS1_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 2, 5),
    _PIPDNS1_Type()
)
pIPDNS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pIPDNS1.setStatus("current")
_PIPDNS2_Type = Integer32
_PIPDNS2_Object = MibScalar
pIPDNS2 = _PIPDNS2_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 2, 6),
    _PIPDNS2_Type()
)
pIPDNS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pIPDNS2.setStatus("current")
_CmdPort_Type = Integer32
_CmdPort_Object = MibScalar
cmdPort = _CmdPort_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 2, 7),
    _CmdPort_Type()
)
cmdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdPort.setStatus("current")
_Ups2CHpar_ObjectIdentity = ObjectIdentity
ups2CHpar = _Ups2CHpar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3)
)
_PStartON_Type = TruthValue
_PStartON_Object = MibScalar
pStartON = _PStartON_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 1),
    _PStartON_Type()
)
pStartON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pStartON.setStatus("current")


class _POUT1_Type(Integer32):
    """Custom type pOUT1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("onIFpowerOK", 2),
          ("on", 3))
    )


_POUT1_Type.__name__ = "Integer32"
_POUT1_Object = MibScalar
pOUT1 = _POUT1_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 2),
    _POUT1_Type()
)
pOUT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOUT1.setStatus("current")


class _POUT2_Type(Integer32):
    """Custom type pOUT2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("onIFpowerOK", 2),
          ("on", 3))
    )


_POUT2_Type.__name__ = "Integer32"
_POUT2_Object = MibScalar
pOUT2 = _POUT2_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 3),
    _POUT2_Type()
)
pOUT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOUT2.setStatus("current")


class _POUT3_Type(Integer32):
    """Custom type pOUT3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("onIFpowerOK", 2),
          ("on", 3))
    )


_POUT3_Type.__name__ = "Integer32"
_POUT3_Object = MibScalar
pOUT3 = _POUT3_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 4),
    _POUT3_Type()
)
pOUT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOUT3.setStatus("current")


class _POUT4_Type(Integer32):
    """Custom type pOUT4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("onIFpowerOK", 2),
          ("on", 3))
    )


_POUT4_Type.__name__ = "Integer32"
_POUT4_Object = MibScalar
pOUT4 = _POUT4_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 5),
    _POUT4_Type()
)
pOUT4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOUT4.setStatus("current")


class _POUT5_Type(Integer32):
    """Custom type pOUT5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("onIFpowerOK", 2),
          ("on", 3))
    )


_POUT5_Type.__name__ = "Integer32"
_POUT5_Object = MibScalar
pOUT5 = _POUT5_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 6),
    _POUT5_Type()
)
pOUT5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOUT5.setStatus("current")


class _POUT6_Type(Integer32):
    """Custom type pOUT6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("onIFpowerOK", 2),
          ("on", 3))
    )


_POUT6_Type.__name__ = "Integer32"
_POUT6_Object = MibScalar
pOUT6 = _POUT6_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 7),
    _POUT6_Type()
)
pOUT6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOUT6.setStatus("current")


class _POutChain1_Type(Integer32):
    """Custom type pOutChain1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_POutChain1_Type.__name__ = "Integer32"
_POutChain1_Object = MibScalar
pOutChain1 = _POutChain1_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 9),
    _POutChain1_Type()
)
pOutChain1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOutChain1.setStatus("current")


class _POutChain2_Type(Integer32):
    """Custom type pOutChain2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 6),
    )


_POutChain2_Type.__name__ = "Integer32"
_POutChain2_Object = MibScalar
pOutChain2 = _POutChain2_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 10),
    _POutChain2_Type()
)
pOutChain2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOutChain2.setStatus("current")


class _PButton1_Type(Integer32):
    """Custom type pButton1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PButton1_Type.__name__ = "Integer32"
_PButton1_Object = MibScalar
pButton1 = _PButton1_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 11),
    _PButton1_Type()
)
pButton1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pButton1.setStatus("current")


class _PButton2_Type(Integer32):
    """Custom type pButton2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PButton2_Type.__name__ = "Integer32"
_PButton2_Object = MibScalar
pButton2 = _PButton2_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 12),
    _PButton2_Type()
)
pButton2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pButton2.setStatus("current")


class _PButton3_Type(Integer32):
    """Custom type pButton3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PButton3_Type.__name__ = "Integer32"
_PButton3_Object = MibScalar
pButton3 = _PButton3_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 13),
    _PButton3_Type()
)
pButton3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pButton3.setStatus("current")


class _PButton4_Type(Integer32):
    """Custom type pButton4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PButton4_Type.__name__ = "Integer32"
_PButton4_Object = MibScalar
pButton4 = _PButton4_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 14),
    _PButton4_Type()
)
pButton4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pButton4.setStatus("current")


class _PButton5_Type(Integer32):
    """Custom type pButton5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PButton5_Type.__name__ = "Integer32"
_PButton5_Object = MibScalar
pButton5 = _PButton5_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 15),
    _PButton5_Type()
)
pButton5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pButton5.setStatus("current")


class _PButton6_Type(Integer32):
    """Custom type pButton6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PButton6_Type.__name__ = "Integer32"
_PButton6_Object = MibScalar
pButton6 = _PButton6_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 16),
    _PButton6_Type()
)
pButton6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pButton6.setStatus("current")


class _POvrAtt_Type(Integer32):
    """Custom type pOvrAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_POvrAtt_Type.__name__ = "Integer32"
_POvrAtt_Object = MibScalar
pOvrAtt = _POvrAtt_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 17),
    _POvrAtt_Type()
)
pOvrAtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOvrAtt.setStatus("current")


class _PRecDelay_Type(Integer32):
    """Custom type pRecDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_PRecDelay_Type.__name__ = "Integer32"
_PRecDelay_Object = MibScalar
pRecDelay = _PRecDelay_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 3, 18),
    _PRecDelay_Type()
)
pRecDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRecDelay.setStatus("current")
if mibBuilder.loadTexts:
    pRecDelay.setUnits("seconds")
_Ups2Gpar_ObjectIdentity = ObjectIdentity
ups2Gpar = _Ups2Gpar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 4)
)


class _PButtS_Type(Integer32):
    """Custom type pButtS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_PButtS_Type.__name__ = "Integer32"
_PButtS_Object = MibScalar
pButtS = _PButtS_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 4, 1),
    _PButtS_Type()
)
pButtS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pButtS.setStatus("current")


class _PAlertS_Type(Integer32):
    """Custom type pAlertS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_PAlertS_Type.__name__ = "Integer32"
_PAlertS_Object = MibScalar
pAlertS = _PAlertS_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 4, 2),
    _PAlertS_Type()
)
pAlertS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAlertS.setStatus("current")
_Ups2TIMpar_ObjectIdentity = ObjectIdentity
ups2TIMpar = _Ups2TIMpar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 5)
)


class _PTimeZone_Type(Integer32):
    """Custom type pTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-13, 14),
    )


_PTimeZone_Type.__name__ = "Integer32"
_PTimeZone_Object = MibScalar
pTimeZone = _PTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 5, 1),
    _PTimeZone_Type()
)
pTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTimeZone.setStatus("current")
_PUseDST_Type = TruthValue
_PUseDST_Object = MibScalar
pUseDST = _PUseDST_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 5, 2),
    _PUseDST_Type()
)
pUseDST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pUseDST.setStatus("current")


class _PNTPAddress_Type(OctetString):
    """Custom type pNTPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_PNTPAddress_Type.__name__ = "OctetString"
_PNTPAddress_Object = MibScalar
pNTPAddress = _PNTPAddress_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 5, 3),
    _PNTPAddress_Type()
)
pNTPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNTPAddress.setStatus("current")


class _PNTPPeriod_Type(Integer32):
    """Custom type pNTPPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_PNTPPeriod_Type.__name__ = "Integer32"
_PNTPPeriod_Object = MibScalar
pNTPPeriod = _PNTPPeriod_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 5, 4),
    _PNTPPeriod_Type()
)
pNTPPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNTPPeriod.setStatus("current")
if mibBuilder.loadTexts:
    pNTPPeriod.setUnits("minutes")
_Ups2SNMPpar_ObjectIdentity = ObjectIdentity
ups2SNMPpar = _Ups2SNMPpar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6)
)
_PAgentON_Type = TruthValue
_PAgentON_Object = MibScalar
pAgentON = _PAgentON_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 1),
    _PAgentON_Type()
)
pAgentON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAgentON.setStatus("current")
_PVersion_Type = PsuSnmpVer
_PVersion_Object = MibScalar
pVersion = _PVersion_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 2),
    _PVersion_Type()
)
pVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pVersion.setStatus("current")


class _PAPort_Type(Unsigned32):
    """Custom type pAPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PAPort_Type.__name__ = "Unsigned32"
_PAPort_Object = MibScalar
pAPort = _PAPort_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 3),
    _PAPort_Type()
)
pAPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAPort.setStatus("current")


class _PTPort_Type(Unsigned32):
    """Custom type pTPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PTPort_Type.__name__ = "Unsigned32"
_PTPort_Object = MibScalar
pTPort = _PTPort_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 4),
    _PTPort_Type()
)
pTPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTPort.setStatus("current")
_PTrapType_Type = PsuTrapType
_PTrapType_Object = MibScalar
pTrapType = _PTrapType_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 5),
    _PTrapType_Type()
)
pTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapType.setStatus("current")


class _PComunity1_Type(OctetString):
    """Custom type pComunity1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PComunity1_Type.__name__ = "OctetString"
_PComunity1_Object = MibScalar
pComunity1 = _PComunity1_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 6),
    _PComunity1_Type()
)
pComunity1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pComunity1.setStatus("current")


class _PComunity2_Type(OctetString):
    """Custom type pComunity2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PComunity2_Type.__name__ = "OctetString"
_PComunity2_Object = MibScalar
pComunity2 = _PComunity2_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 7),
    _PComunity2_Type()
)
pComunity2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pComunity2.setStatus("current")


class _PComunity3_Type(OctetString):
    """Custom type pComunity3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PComunity3_Type.__name__ = "OctetString"
_PComunity3_Object = MibScalar
pComunity3 = _PComunity3_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 8),
    _PComunity3_Type()
)
pComunity3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pComunity3.setStatus("current")


class _PComun1ACS_Type(Unsigned32):
    """Custom type pComun1ACS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_PComun1ACS_Type.__name__ = "Unsigned32"
_PComun1ACS_Object = MibScalar
pComun1ACS = _PComun1ACS_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 9),
    _PComun1ACS_Type()
)
pComun1ACS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pComun1ACS.setStatus("current")


class _PComun2ACS_Type(Unsigned32):
    """Custom type pComun2ACS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_PComun2ACS_Type.__name__ = "Unsigned32"
_PComun2ACS_Object = MibScalar
pComun2ACS = _PComun2ACS_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 10),
    _PComun2ACS_Type()
)
pComun2ACS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pComun2ACS.setStatus("current")


class _PComun3ACS_Type(Unsigned32):
    """Custom type pComun3ACS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_PComun3ACS_Type.__name__ = "Unsigned32"
_PComun3ACS_Object = MibScalar
pComun3ACS = _PComun3ACS_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 11),
    _PComun3ACS_Type()
)
pComun3ACS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pComun3ACS.setStatus("current")
_PTrap1ON_Type = TruthValue
_PTrap1ON_Object = MibScalar
pTrap1ON = _PTrap1ON_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 12),
    _PTrap1ON_Type()
)
pTrap1ON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrap1ON.setStatus("current")
_PTrap1IPaddr_Type = IpAddress
_PTrap1IPaddr_Object = MibScalar
pTrap1IPaddr = _PTrap1IPaddr_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 13),
    _PTrap1IPaddr_Type()
)
pTrap1IPaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrap1IPaddr.setStatus("current")


class _PTrap1DNSaddr_Type(OctetString):
    """Custom type pTrap1DNSaddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PTrap1DNSaddr_Type.__name__ = "OctetString"
_PTrap1DNSaddr_Object = MibScalar
pTrap1DNSaddr = _PTrap1DNSaddr_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 14),
    _PTrap1DNSaddr_Type()
)
pTrap1DNSaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrap1DNSaddr.setStatus("current")


class _PTrap1user_Type(OctetString):
    """Custom type pTrap1user based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PTrap1user_Type.__name__ = "OctetString"
_PTrap1user_Object = MibScalar
pTrap1user = _PTrap1user_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 15),
    _PTrap1user_Type()
)
pTrap1user.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrap1user.setStatus("current")
_PTrap2ON_Type = TruthValue
_PTrap2ON_Object = MibScalar
pTrap2ON = _PTrap2ON_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 16),
    _PTrap2ON_Type()
)
pTrap2ON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrap2ON.setStatus("current")
_PTrap2IPaddr_Type = IpAddress
_PTrap2IPaddr_Object = MibScalar
pTrap2IPaddr = _PTrap2IPaddr_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 17),
    _PTrap2IPaddr_Type()
)
pTrap2IPaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrap2IPaddr.setStatus("current")


class _PTrap2DNSaddr_Type(OctetString):
    """Custom type pTrap2DNSaddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PTrap2DNSaddr_Type.__name__ = "OctetString"
_PTrap2DNSaddr_Object = MibScalar
pTrap2DNSaddr = _PTrap2DNSaddr_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 18),
    _PTrap2DNSaddr_Type()
)
pTrap2DNSaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrap2DNSaddr.setStatus("current")


class _PTrap2user_Type(OctetString):
    """Custom type pTrap2user based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PTrap2user_Type.__name__ = "OctetString"
_PTrap2user_Object = MibScalar
pTrap2user = _PTrap2user_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 19),
    _PTrap2user_Type()
)
pTrap2user.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrap2user.setStatus("current")
_PTrap3ON_Type = TruthValue
_PTrap3ON_Object = MibScalar
pTrap3ON = _PTrap3ON_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 20),
    _PTrap3ON_Type()
)
pTrap3ON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrap3ON.setStatus("current")
_PTrap3IPaddr_Type = IpAddress
_PTrap3IPaddr_Object = MibScalar
pTrap3IPaddr = _PTrap3IPaddr_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 21),
    _PTrap3IPaddr_Type()
)
pTrap3IPaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrap3IPaddr.setStatus("current")


class _PTrap3DNSaddr_Type(OctetString):
    """Custom type pTrap3DNSaddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PTrap3DNSaddr_Type.__name__ = "OctetString"
_PTrap3DNSaddr_Object = MibScalar
pTrap3DNSaddr = _PTrap3DNSaddr_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 22),
    _PTrap3DNSaddr_Type()
)
pTrap3DNSaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrap3DNSaddr.setStatus("current")


class _PTrap3user_Type(OctetString):
    """Custom type pTrap3user based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PTrap3user_Type.__name__ = "OctetString"
_PTrap3user_Object = MibScalar
pTrap3user = _PTrap3user_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 6, 23),
    _PTrap3user_Type()
)
pTrap3user.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrap3user.setStatus("current")
_Ups2SYSinfo_ObjectIdentity = ObjectIdentity
ups2SYSinfo = _Ups2SYSinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 7)
)


class _SerialNum_Type(OctetString):
    """Custom type serialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SerialNum_Type.__name__ = "OctetString"
_SerialNum_Object = MibScalar
serialNum = _SerialNum_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 7, 1),
    _SerialNum_Type()
)
serialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNum.setStatus("current")


class _FirmwVer_Type(OctetString):
    """Custom type firmwVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_FirmwVer_Type.__name__ = "OctetString"
_FirmwVer_Object = MibScalar
firmwVer = _FirmwVer_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 7, 2),
    _FirmwVer_Type()
)
firmwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwVer.setStatus("current")


class _FwADC_Type(OctetString):
    """Custom type fwADC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_FwADC_Type.__name__ = "OctetString"
_FwADC_Object = MibScalar
fwADC = _FwADC_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 7, 3),
    _FwADC_Type()
)
fwADC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwADC.setStatus("current")
_BckdoorIP_Type = IpAddress
_BckdoorIP_Object = MibScalar
bckdoorIP = _BckdoorIP_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 7, 4),
    _BckdoorIP_Type()
)
bckdoorIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bckdoorIP.setStatus("current")
_BckdoorMask_Type = IpAddress
_BckdoorMask_Object = MibScalar
bckdoorMask = _BckdoorMask_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 7, 5),
    _BckdoorMask_Type()
)
bckdoorMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bckdoorMask.setStatus("current")
_SnmpVerMin_Type = Integer32
_SnmpVerMin_Object = MibScalar
snmpVerMin = _SnmpVerMin_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 7, 6),
    _SnmpVerMin_Type()
)
snmpVerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpVerMin.setStatus("current")
_SnmpVerMax_Type = Integer32
_SnmpVerMax_Object = MibScalar
snmpVerMax = _SnmpVerMax_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 7, 7),
    _SnmpVerMax_Type()
)
snmpVerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpVerMax.setStatus("current")
_Ups2RTC_Type = DateAndTime
_Ups2RTC_Object = MibScalar
ups2RTC = _Ups2RTC_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 7, 8),
    _Ups2RTC_Type()
)
ups2RTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ups2RTC.setStatus("current")
_Ups2BATinfo_ObjectIdentity = ObjectIdentity
ups2BATinfo = _Ups2BATinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 8)
)
_UpsBatVoltage_Type = Integer32
_UpsBatVoltage_Object = MibScalar
upsBatVoltage = _UpsBatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 8, 1),
    _UpsBatVoltage_Type()
)
upsBatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsBatVoltage.setUnits("0.001 Volt DC")
_UpsBatDisCurrent_Type = Integer32
_UpsBatDisCurrent_Object = MibScalar
upsBatDisCurrent = _UpsBatDisCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 8, 2),
    _UpsBatDisCurrent_Type()
)
upsBatDisCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatDisCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsBatDisCurrent.setUnits("0.001 Amp DC")
_UpsBatChaCurrent_Type = Integer32
_UpsBatChaCurrent_Object = MibScalar
upsBatChaCurrent = _UpsBatChaCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 8, 3),
    _UpsBatChaCurrent_Type()
)
upsBatChaCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatChaCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsBatChaCurrent.setUnits("0.001 A DC")
_UpsBatTemperature_Type = Integer32
_UpsBatTemperature_Object = MibScalar
upsBatTemperature = _UpsBatTemperature_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 8, 4),
    _UpsBatTemperature_Type()
)
upsBatTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatTemperature.setStatus("current")
if mibBuilder.loadTexts:
    upsBatTemperature.setUnits("0.1 degrees Centigrade")


class _UpsBatStatus_Type(Integer32):
    """Custom type upsBatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("batCrit", 1),
          ("batLow", 2),
          ("batMid", 3),
          ("batFull", 4),
          ("batNone", 5))
    )


_UpsBatStatus_Type.__name__ = "Integer32"
_UpsBatStatus_Object = MibScalar
upsBatStatus = _UpsBatStatus_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 8, 5),
    _UpsBatStatus_Type()
)
upsBatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatStatus.setStatus("current")


class _UpsBatSOC_Type(Integer32):
    """Custom type upsBatSOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsBatSOC_Type.__name__ = "Integer32"
_UpsBatSOC_Object = MibScalar
upsBatSOC = _UpsBatSOC_Object(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 8, 6),
    _UpsBatSOC_Type()
)
upsBatSOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatSOC.setStatus("current")
if mibBuilder.loadTexts:
    upsBatSOC.setUnits("% State of Charge")
_Compls_ObjectIdentity = ObjectIdentity
compls = _Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 9)
)
_Objs_ObjectIdentity = ObjectIdentity
objs = _Objs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 10)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 11)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 12)
)
_EventsV2_ObjectIdentity = ObjectIdentity
eventsV2 = _EventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 12, 0)
)

# Managed Objects groups

objectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 11, 1)
)
objectGroup.setObjects(
      *(("ALITER-UPS2-MIB", "firmwVer"),
        ("ALITER-UPS2-MIB", "fwADC"),
        ("ALITER-UPS2-MIB", "serialNum"),
        ("ALITER-UPS2-MIB", "snmpVerMin"),
        ("ALITER-UPS2-MIB", "pUseDHCP"),
        ("ALITER-UPS2-MIB", "pTrapType"),
        ("ALITER-UPS2-MIB", "bckdoorIP"),
        ("ALITER-UPS2-MIB", "bckdoorMask"),
        ("ALITER-UPS2-MIB", "pNTPAddress"),
        ("ALITER-UPS2-MIB", "pUseDST"),
        ("ALITER-UPS2-MIB", "pTimeZone"),
        ("ALITER-UPS2-MIB", "cmdPort"),
        ("ALITER-UPS2-MIB", "ups2ObjectID"),
        ("ALITER-UPS2-MIB", "pStartON"),
        ("ALITER-UPS2-MIB", "pOUT1"),
        ("ALITER-UPS2-MIB", "pOUT2"),
        ("ALITER-UPS2-MIB", "pOUT3"),
        ("ALITER-UPS2-MIB", "upsBatSOC"),
        ("ALITER-UPS2-MIB", "pOUT4"),
        ("ALITER-UPS2-MIB", "pOUT5"),
        ("ALITER-UPS2-MIB", "pOUT6"),
        ("ALITER-UPS2-MIB", "pOutChain1"),
        ("ALITER-UPS2-MIB", "pOutChain2"),
        ("ALITER-UPS2-MIB", "pButton1"),
        ("ALITER-UPS2-MIB", "pButton2"),
        ("ALITER-UPS2-MIB", "pButton3"),
        ("ALITER-UPS2-MIB", "pButton4"),
        ("ALITER-UPS2-MIB", "pButton5"),
        ("ALITER-UPS2-MIB", "pButton6"),
        ("ALITER-UPS2-MIB", "pOvrAtt"),
        ("ALITER-UPS2-MIB", "pRecDelay"),
        ("ALITER-UPS2-MIB", "pButtS"),
        ("ALITER-UPS2-MIB", "pAlertS"),
        ("ALITER-UPS2-MIB", "pNTPPeriod"),
        ("ALITER-UPS2-MIB", "pAgentON"),
        ("ALITER-UPS2-MIB", "pVersion"),
        ("ALITER-UPS2-MIB", "pAPort"),
        ("ALITER-UPS2-MIB", "pTPort"),
        ("ALITER-UPS2-MIB", "pComunity1"),
        ("ALITER-UPS2-MIB", "pComunity2"),
        ("ALITER-UPS2-MIB", "pComunity3"),
        ("ALITER-UPS2-MIB", "pComun1ACS"),
        ("ALITER-UPS2-MIB", "pComun2ACS"),
        ("ALITER-UPS2-MIB", "pComun3ACS"),
        ("ALITER-UPS2-MIB", "pTrap1ON"),
        ("ALITER-UPS2-MIB", "pTrap1IPaddr"),
        ("ALITER-UPS2-MIB", "pTrap1DNSaddr"),
        ("ALITER-UPS2-MIB", "pTrap1user"),
        ("ALITER-UPS2-MIB", "pTrap2ON"),
        ("ALITER-UPS2-MIB", "pTrap2IPaddr"),
        ("ALITER-UPS2-MIB", "pTrap2DNSaddr"),
        ("ALITER-UPS2-MIB", "pTrap2user"),
        ("ALITER-UPS2-MIB", "pTrap3ON"),
        ("ALITER-UPS2-MIB", "pTrap3IPaddr"),
        ("ALITER-UPS2-MIB", "pTrap3DNSaddr"),
        ("ALITER-UPS2-MIB", "pTrap3user"),
        ("ALITER-UPS2-MIB", "ups2RTC"),
        ("ALITER-UPS2-MIB", "upsBatVoltage"),
        ("ALITER-UPS2-MIB", "upsBatDisCurrent"),
        ("ALITER-UPS2-MIB", "upsBatChaCurrent"),
        ("ALITER-UPS2-MIB", "upsBatTemperature"),
        ("ALITER-UPS2-MIB", "upsBatStatus"),
        ("ALITER-UPS2-MIB", "snmpVerMax"),
        ("ALITER-UPS2-MIB", "pIPAddr"),
        ("ALITER-UPS2-MIB", "pIPMask"),
        ("ALITER-UPS2-MIB", "pIPGtw"),
        ("ALITER-UPS2-MIB", "pIPDNS1"),
        ("ALITER-UPS2-MIB", "pIPDNS2"))
)
if mibBuilder.loadTexts:
    objectGroup.setStatus("current")


# Notification objects

event1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 12, 0, 1)
)
event1.setObjects(
    ("ALITER-UPS2-MIB", "upsBatTemperature")
)
if mibBuilder.loadTexts:
    event1.setStatus(
        "current"
    )

event2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 12, 0, 2)
)
if mibBuilder.loadTexts:
    event2.setStatus(
        "current"
    )


# Notifications groups

notificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 42333, 10, 2, 11, 2)
)
notificationGroup.setObjects(
      *(("ALITER-UPS2-MIB", "event1"),
        ("ALITER-UPS2-MIB", "event2"))
)
if mibBuilder.loadTexts:
    notificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALITER-UPS2-MIB",
    **{"PsuSnmpVer": PsuSnmpVer,
       "PsuTrapType": PsuTrapType,
       "Status": Status,
       "aliter": aliter,
       "atComtanet": atComtanet,
       "atUPS2": atUPS2,
       "ups2ObjectID": ups2ObjectID,
       "ups2NETpar": ups2NETpar,
       "pUseDHCP": pUseDHCP,
       "pIPAddr": pIPAddr,
       "pIPMask": pIPMask,
       "pIPGtw": pIPGtw,
       "pIPDNS1": pIPDNS1,
       "pIPDNS2": pIPDNS2,
       "cmdPort": cmdPort,
       "ups2CHpar": ups2CHpar,
       "pStartON": pStartON,
       "pOUT1": pOUT1,
       "pOUT2": pOUT2,
       "pOUT3": pOUT3,
       "pOUT4": pOUT4,
       "pOUT5": pOUT5,
       "pOUT6": pOUT6,
       "pOutChain1": pOutChain1,
       "pOutChain2": pOutChain2,
       "pButton1": pButton1,
       "pButton2": pButton2,
       "pButton3": pButton3,
       "pButton4": pButton4,
       "pButton5": pButton5,
       "pButton6": pButton6,
       "pOvrAtt": pOvrAtt,
       "pRecDelay": pRecDelay,
       "ups2Gpar": ups2Gpar,
       "pButtS": pButtS,
       "pAlertS": pAlertS,
       "ups2TIMpar": ups2TIMpar,
       "pTimeZone": pTimeZone,
       "pUseDST": pUseDST,
       "pNTPAddress": pNTPAddress,
       "pNTPPeriod": pNTPPeriod,
       "ups2SNMPpar": ups2SNMPpar,
       "pAgentON": pAgentON,
       "pVersion": pVersion,
       "pAPort": pAPort,
       "pTPort": pTPort,
       "pTrapType": pTrapType,
       "pComunity1": pComunity1,
       "pComunity2": pComunity2,
       "pComunity3": pComunity3,
       "pComun1ACS": pComun1ACS,
       "pComun2ACS": pComun2ACS,
       "pComun3ACS": pComun3ACS,
       "pTrap1ON": pTrap1ON,
       "pTrap1IPaddr": pTrap1IPaddr,
       "pTrap1DNSaddr": pTrap1DNSaddr,
       "pTrap1user": pTrap1user,
       "pTrap2ON": pTrap2ON,
       "pTrap2IPaddr": pTrap2IPaddr,
       "pTrap2DNSaddr": pTrap2DNSaddr,
       "pTrap2user": pTrap2user,
       "pTrap3ON": pTrap3ON,
       "pTrap3IPaddr": pTrap3IPaddr,
       "pTrap3DNSaddr": pTrap3DNSaddr,
       "pTrap3user": pTrap3user,
       "ups2SYSinfo": ups2SYSinfo,
       "serialNum": serialNum,
       "firmwVer": firmwVer,
       "fwADC": fwADC,
       "bckdoorIP": bckdoorIP,
       "bckdoorMask": bckdoorMask,
       "snmpVerMin": snmpVerMin,
       "snmpVerMax": snmpVerMax,
       "ups2RTC": ups2RTC,
       "ups2BATinfo": ups2BATinfo,
       "upsBatVoltage": upsBatVoltage,
       "upsBatDisCurrent": upsBatDisCurrent,
       "upsBatChaCurrent": upsBatChaCurrent,
       "upsBatTemperature": upsBatTemperature,
       "upsBatStatus": upsBatStatus,
       "upsBatSOC": upsBatSOC,
       "compls": compls,
       "objs": objs,
       "groups": groups,
       "objectGroup": objectGroup,
       "notificationGroup": notificationGroup,
       "events": events,
       "eventsV2": eventsV2,
       "event1": event1,
       "event2": event2}
)
