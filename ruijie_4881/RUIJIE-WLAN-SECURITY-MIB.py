# SNMP MIB module (RUIJIE-WLAN-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-WLAN-SECURITY-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:52:30 2025
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

(ruijieApgWlanId,) = mibBuilder.importSymbols(
    "RUIJIE-AC-MGMT-MIB",
    "ruijieApgWlanId")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieWLANsecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61)
)
if mibBuilder.loadTexts:
    ruijieWLANsecurityMIB.setRevisions(
        ("2009-10-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieWLANsecurityTraps_ObjectIdentity = ObjectIdentity
ruijieWLANsecurityTraps = _RuijieWLANsecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 0)
)
_RuijieWLANsecurityMIBObjects_ObjectIdentity = ObjectIdentity
ruijieWLANsecurityMIBObjects = _RuijieWLANsecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1)
)


class _RuijieAPworkmode_Type(Integer32):
    """Custom type ruijieAPworkmode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fitap", 1),
          ("fatap", 2))
    )


_RuijieAPworkmode_Type.__name__ = "Integer32"
_RuijieAPworkmode_Object = MibScalar
ruijieAPworkmode = _RuijieAPworkmode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 1),
    _RuijieAPworkmode_Type()
)
ruijieAPworkmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAPworkmode.setStatus("current")
_RuijieWLANsecurityConfigTable_Object = MibTable
ruijieWLANsecurityConfigTable = _RuijieWLANsecurityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieWLANsecurityConfigTable.setStatus("current")
_RuijieWLANsecurityConfigEntry_Object = MibTableRow
ruijieWLANsecurityConfigEntry = _RuijieWLANsecurityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1)
)
ruijieWLANsecurityConfigEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    ruijieWLANsecurityConfigEntry.setStatus("current")


class _RuijieWLANsecrymode_Type(Integer32):
    """Custom type ruijieWLANsecrymode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("staticwep", 2),
          ("wep8021x", 3),
          ("wpanone", 4),
          ("wpapsk", 5),
          ("wpa8021x", 6),
          ("tsn", 7))
    )


_RuijieWLANsecrymode_Type.__name__ = "Integer32"
_RuijieWLANsecrymode_Object = MibTableColumn
ruijieWLANsecrymode = _RuijieWLANsecrymode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 1),
    _RuijieWLANsecrymode_Type()
)
ruijieWLANsecrymode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWLANsecrymode.setStatus("current")


class _Ruijiestaticweplength_Type(Integer32):
    """Custom type ruijiestaticweplength based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wep40", 1),
          ("wep104", 2),
          ("wep128", 3))
    )


_Ruijiestaticweplength_Type.__name__ = "Integer32"
_Ruijiestaticweplength_Object = MibTableColumn
ruijiestaticweplength = _Ruijiestaticweplength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 2),
    _Ruijiestaticweplength_Type()
)
ruijiestaticweplength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiestaticweplength.setStatus("current")


class _Ruijie8021xweplength_Type(Integer32):
    """Custom type ruijie8021xweplength based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wep40", 1),
          ("wep104", 2),
          ("wep128", 3))
    )


_Ruijie8021xweplength_Type.__name__ = "Integer32"
_Ruijie8021xweplength_Object = MibTableColumn
ruijie8021xweplength = _Ruijie8021xweplength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 3),
    _Ruijie8021xweplength_Type()
)
ruijie8021xweplength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijie8021xweplength.setStatus("current")


class _RuijieWPAenabled_Type(TruthValue):
    """Custom type ruijieWPAenabled based on TruthValue"""
    defaultValue = 2


_RuijieWPAenabled_Type.__name__ = "TruthValue"
_RuijieWPAenabled_Object = MibTableColumn
ruijieWPAenabled = _RuijieWPAenabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 4),
    _RuijieWPAenabled_Type()
)
ruijieWPAenabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWPAenabled.setStatus("current")


class _RuijieWPAPairwisecipher_Type(Integer32):
    """Custom type ruijieWPAPairwisecipher based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tkip", 1),
          ("aes", 2),
          ("tkiporaes", 3))
    )


_RuijieWPAPairwisecipher_Type.__name__ = "Integer32"
_RuijieWPAPairwisecipher_Object = MibTableColumn
ruijieWPAPairwisecipher = _RuijieWPAPairwisecipher_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 5),
    _RuijieWPAPairwisecipher_Type()
)
ruijieWPAPairwisecipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWPAPairwisecipher.setStatus("current")


class _RuijieWPAakmmode_Type(Integer32):
    """Custom type ruijieWPAakmmode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021x", 1),
          ("psk", 2),
          ("pskor8021x", 3))
    )


_RuijieWPAakmmode_Type.__name__ = "Integer32"
_RuijieWPAakmmode_Object = MibTableColumn
ruijieWPAakmmode = _RuijieWPAakmmode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 6),
    _RuijieWPAakmmode_Type()
)
ruijieWPAakmmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWPAakmmode.setStatus("current")
_RuijieWPApskPassPhrase_Type = DisplayString
_RuijieWPApskPassPhrase_Object = MibTableColumn
ruijieWPApskPassPhrase = _RuijieWPApskPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 7),
    _RuijieWPApskPassPhrase_Type()
)
ruijieWPApskPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWPApskPassPhrase.setStatus("current")


class _RuijieWLANsecry80211i_Type(TruthValue):
    """Custom type ruijieWLANsecry80211i based on TruthValue"""
    defaultValue = 1


_RuijieWLANsecry80211i_Type.__name__ = "TruthValue"
_RuijieWLANsecry80211i_Object = MibTableColumn
ruijieWLANsecry80211i = _RuijieWLANsecry80211i_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 8),
    _RuijieWLANsecry80211i_Type()
)
ruijieWLANsecry80211i.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWLANsecry80211i.setStatus("current")


class _RuijieWAPIasuIpaddress_Type(Unsigned32):
    """Custom type ruijieWAPIasuIpaddress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieWAPIasuIpaddress_Type.__name__ = "Unsigned32"
_RuijieWAPIasuIpaddress_Object = MibTableColumn
ruijieWAPIasuIpaddress = _RuijieWAPIasuIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 9),
    _RuijieWAPIasuIpaddress_Type()
)
ruijieWAPIasuIpaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWAPIasuIpaddress.setStatus("current")


class _RuijieWAPIcertificateformat_Type(Integer32):
    """Custom type ruijieWAPIcertificateformat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("x509v3", 1),
          ("wapigbw", 2))
    )


_RuijieWAPIcertificateformat_Type.__name__ = "Integer32"
_RuijieWAPIcertificateformat_Object = MibTableColumn
ruijieWAPIcertificateformat = _RuijieWAPIcertificateformat_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 10),
    _RuijieWAPIcertificateformat_Type()
)
ruijieWAPIcertificateformat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWAPIcertificateformat.setStatus("current")


class _RuijieWAPImsrekeyClientoff_Type(TruthValue):
    """Custom type ruijieWAPImsrekeyClientoff based on TruthValue"""
    defaultValue = 2


_RuijieWAPImsrekeyClientoff_Type.__name__ = "TruthValue"
_RuijieWAPImsrekeyClientoff_Object = MibTableColumn
ruijieWAPImsrekeyClientoff = _RuijieWAPImsrekeyClientoff_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 11),
    _RuijieWAPImsrekeyClientoff_Type()
)
ruijieWAPImsrekeyClientoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWAPImsrekeyClientoff.setStatus("current")


class _RuijieWAPIimportcertificate_Type(Integer32):
    """Custom type ruijieWAPIimportcertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ca", 1),
          ("local", 2),
          ("as", 3))
    )


_RuijieWAPIimportcertificate_Type.__name__ = "Integer32"
_RuijieWAPIimportcertificate_Object = MibTableColumn
ruijieWAPIimportcertificate = _RuijieWAPIimportcertificate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 12),
    _RuijieWAPIimportcertificate_Type()
)
ruijieWAPIimportcertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWAPIimportcertificate.setStatus("current")
_RuijieWAPIcacertificatename_Type = DisplayString
_RuijieWAPIcacertificatename_Object = MibTableColumn
ruijieWAPIcacertificatename = _RuijieWAPIcacertificatename_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 13),
    _RuijieWAPIcacertificatename_Type()
)
ruijieWAPIcacertificatename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWAPIcacertificatename.setStatus("current")
_RuijieWAPIlocalcertificatename_Type = DisplayString
_RuijieWAPIlocalcertificatename_Object = MibTableColumn
ruijieWAPIlocalcertificatename = _RuijieWAPIlocalcertificatename_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 14),
    _RuijieWAPIlocalcertificatename_Type()
)
ruijieWAPIlocalcertificatename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWAPIlocalcertificatename.setStatus("current")
_RuijieWAPIascertificatename_Type = DisplayString
_RuijieWAPIascertificatename_Object = MibTableColumn
ruijieWAPIascertificatename = _RuijieWAPIascertificatename_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 15),
    _RuijieWAPIascertificatename_Type()
)
ruijieWAPIascertificatename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWAPIascertificatename.setStatus("current")
_RuijieRSNenabled_Type = TruthValue
_RuijieRSNenabled_Object = MibTableColumn
ruijieRSNenabled = _RuijieRSNenabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 16),
    _RuijieRSNenabled_Type()
)
ruijieRSNenabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRSNenabled.setStatus("current")


class _RuijieRSNPairwisecipher_Type(Integer32):
    """Custom type ruijieRSNPairwisecipher based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tkip", 1),
          ("aes", 2),
          ("tkiporaes", 3))
    )


_RuijieRSNPairwisecipher_Type.__name__ = "Integer32"
_RuijieRSNPairwisecipher_Object = MibTableColumn
ruijieRSNPairwisecipher = _RuijieRSNPairwisecipher_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 17),
    _RuijieRSNPairwisecipher_Type()
)
ruijieRSNPairwisecipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRSNPairwisecipher.setStatus("current")


class _RuijieRSNakmmode_Type(Integer32):
    """Custom type ruijieRSNakmmode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021x", 1),
          ("psk", 2),
          ("pskor8021x", 3))
    )


_RuijieRSNakmmode_Type.__name__ = "Integer32"
_RuijieRSNakmmode_Object = MibTableColumn
ruijieRSNakmmode = _RuijieRSNakmmode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 18),
    _RuijieRSNakmmode_Type()
)
ruijieRSNakmmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRSNakmmode.setStatus("current")
_RuijieRSNpskPassPhrase_Type = DisplayString
_RuijieRSNpskPassPhrase_Object = MibTableColumn
ruijieRSNpskPassPhrase = _RuijieRSNpskPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 19),
    _RuijieRSNpskPassPhrase_Type()
)
ruijieRSNpskPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRSNpskPassPhrase.setStatus("current")


class _RuijieWEPAuthenAlgorithm_Type(Integer32):
    """Custom type ruijieWEPAuthenAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 1),
          ("sharedKey", 2))
    )


_RuijieWEPAuthenAlgorithm_Type.__name__ = "Integer32"
_RuijieWEPAuthenAlgorithm_Object = MibTableColumn
ruijieWEPAuthenAlgorithm = _RuijieWEPAuthenAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 20),
    _RuijieWEPAuthenAlgorithm_Type()
)
ruijieWEPAuthenAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWEPAuthenAlgorithm.setStatus("current")
_RuijieWLANsecurityStatus_Type = RowStatus
_RuijieWLANsecurityStatus_Object = MibTableColumn
ruijieWLANsecurityStatus = _RuijieWLANsecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 21),
    _RuijieWLANsecurityStatus_Type()
)
ruijieWLANsecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWLANsecurityStatus.setStatus("current")
_RuijieACauthenMethodsupport_Type = Integer32
_RuijieACauthenMethodsupport_Object = MibTableColumn
ruijieACauthenMethodsupport = _RuijieACauthenMethodsupport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 22),
    _RuijieACauthenMethodsupport_Type()
)
ruijieACauthenMethodsupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieACauthenMethodsupport.setStatus("current")


class _RuijieWLANEAPAuthenSupport_Type(Integer32):
    """Custom type ruijieWLANEAPAuthenSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableEAPAuthentication", 0),
          ("disableEAPAuthentication", 1),
          ("notSupportingEAPAuthentication", 2))
    )


_RuijieWLANEAPAuthenSupport_Type.__name__ = "Integer32"
_RuijieWLANEAPAuthenSupport_Object = MibTableColumn
ruijieWLANEAPAuthenSupport = _RuijieWLANEAPAuthenSupport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 2, 1, 23),
    _RuijieWLANEAPAuthenSupport_Type()
)
ruijieWLANEAPAuthenSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWLANEAPAuthenSupport.setStatus("current")
_RuijieWEPDefaultKeysTable_Object = MibTable
ruijieWEPDefaultKeysTable = _RuijieWEPDefaultKeysTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieWEPDefaultKeysTable.setStatus("current")
_RuijieWEPDefaultKeysEntry_Object = MibTableRow
ruijieWEPDefaultKeysEntry = _RuijieWEPDefaultKeysEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 3, 1)
)
ruijieWEPDefaultKeysEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
    (0, "RUIJIE-WLAN-SECURITY-MIB", "ruijieWEPDefaultKeyIndex"),
)
if mibBuilder.loadTexts:
    ruijieWEPDefaultKeysEntry.setStatus("current")


class _RuijieWEPDefaultKeyIndex_Type(Integer32):
    """Custom type ruijieWEPDefaultKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RuijieWEPDefaultKeyIndex_Type.__name__ = "Integer32"
_RuijieWEPDefaultKeyIndex_Object = MibTableColumn
ruijieWEPDefaultKeyIndex = _RuijieWEPDefaultKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 3, 1, 1),
    _RuijieWEPDefaultKeyIndex_Type()
)
ruijieWEPDefaultKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieWEPDefaultKeyIndex.setStatus("current")
_RuijieWEPDefaultKeyValue_Type = OctetString
_RuijieWEPDefaultKeyValue_Object = MibTableColumn
ruijieWEPDefaultKeyValue = _RuijieWEPDefaultKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 3, 1, 2),
    _RuijieWEPDefaultKeyValue_Type()
)
ruijieWEPDefaultKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWEPDefaultKeyValue.setStatus("current")


class _RuijieWEPDefaultKeyLength_Type(Integer32):
    """Custom type ruijieWEPDefaultKeyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wep40", 1),
          ("wep104", 2),
          ("wep128", 3))
    )


_RuijieWEPDefaultKeyLength_Type.__name__ = "Integer32"
_RuijieWEPDefaultKeyLength_Object = MibTableColumn
ruijieWEPDefaultKeyLength = _RuijieWEPDefaultKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 1, 3, 1, 3),
    _RuijieWEPDefaultKeyLength_Type()
)
ruijieWEPDefaultKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWEPDefaultKeyLength.setStatus("current")
_RuijieWlansecurityMIBConform_ObjectIdentity = ObjectIdentity
ruijieWlansecurityMIBConform = _RuijieWlansecurityMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 2)
)
_RuijieWlansecurityMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieWlansecurityMIBCompliances = _RuijieWlansecurityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 2, 1)
)
_RuijieWlansecurityMIBGroups_ObjectIdentity = ObjectIdentity
ruijieWlansecurityMIBGroups = _RuijieWlansecurityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 2, 2)
)
_RuijieWlansecurityTrapvar_ObjectIdentity = ObjectIdentity
ruijieWlansecurityTrapvar = _RuijieWlansecurityTrapvar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 3)
)
_RuijieWlansecurityWepDecrytEnableTrapVar_Type = Integer32
_RuijieWlansecurityWepDecrytEnableTrapVar_Object = MibScalar
ruijieWlansecurityWepDecrytEnableTrapVar = _RuijieWlansecurityWepDecrytEnableTrapVar_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 3, 1),
    _RuijieWlansecurityWepDecrytEnableTrapVar_Type()
)
ruijieWlansecurityWepDecrytEnableTrapVar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlansecurityWepDecrytEnableTrapVar.setStatus("current")
_RuijieWlansecurityDeviceMAC_Type = MacAddress
_RuijieWlansecurityDeviceMAC_Object = MibScalar
ruijieWlansecurityDeviceMAC = _RuijieWlansecurityDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 3, 2),
    _RuijieWlansecurityDeviceMAC_Type()
)
ruijieWlansecurityDeviceMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlansecurityDeviceMAC.setStatus("current")

# Managed Objects groups

ruijieWlansecuritycofigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 2, 2, 1)
)
ruijieWlansecuritycofigGroup.setObjects(
      *(("RUIJIE-WLAN-SECURITY-MIB", "ruijieAPworkmode"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWLANsecrymode"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijiestaticweplength"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijie8021xweplength"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWPAenabled"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWPAPairwisecipher"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWPAakmmode"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWPApskPassPhrase"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWLANsecry80211i"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWAPIasuIpaddress"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWAPIcertificateformat"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWAPImsrekeyClientoff"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWAPIimportcertificate"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWAPIcacertificatename"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWAPIlocalcertificatename"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWAPIascertificatename"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieRSNenabled"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieRSNPairwisecipher"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieRSNakmmode"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieRSNpskPassPhrase"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWEPAuthenAlgorithm"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWLANsecurityStatus"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieACauthenMethodsupport"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWLANEAPAuthenSupport"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWlansecurityWepDecrytEnableTrapVar"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWlansecurityDeviceMAC"))
)
if mibBuilder.loadTexts:
    ruijieWlansecuritycofigGroup.setStatus("current")

ruijieWEPDefaultKeysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 2, 2, 2)
)
ruijieWEPDefaultKeysGroup.setObjects(
      *(("RUIJIE-WLAN-SECURITY-MIB", "ruijieWEPDefaultKeyValue"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWEPDefaultKeyLength"))
)
if mibBuilder.loadTexts:
    ruijieWEPDefaultKeysGroup.setStatus("current")


# Notification objects

ruijieWlansecurityWepDecrytErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 0, 1)
)
ruijieWlansecurityWepDecrytErr.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWlansecurityDeviceMAC"))
)
if mibBuilder.loadTexts:
    ruijieWlansecurityWepDecrytErr.setStatus(
        "current"
    )


# Notifications groups

ruijieWlansecurityTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 2, 2, 3)
)
ruijieWlansecurityTrapGroup.setObjects(
    ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWlansecurityWepDecrytErr")
)
if mibBuilder.loadTexts:
    ruijieWlansecurityTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieWlansecurityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 61, 2, 1, 1)
)
ruijieWlansecurityMIBCompliance.setObjects(
      *(("RUIJIE-WLAN-SECURITY-MIB", "ruijieWlansecuritycofigGroup"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWEPDefaultKeysGroup"),
        ("RUIJIE-WLAN-SECURITY-MIB", "ruijieWlansecurityTrapGroup"))
)
if mibBuilder.loadTexts:
    ruijieWlansecurityMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-WLAN-SECURITY-MIB",
    **{"ruijieWLANsecurityMIB": ruijieWLANsecurityMIB,
       "ruijieWLANsecurityTraps": ruijieWLANsecurityTraps,
       "ruijieWlansecurityWepDecrytErr": ruijieWlansecurityWepDecrytErr,
       "ruijieWLANsecurityMIBObjects": ruijieWLANsecurityMIBObjects,
       "ruijieAPworkmode": ruijieAPworkmode,
       "ruijieWLANsecurityConfigTable": ruijieWLANsecurityConfigTable,
       "ruijieWLANsecurityConfigEntry": ruijieWLANsecurityConfigEntry,
       "ruijieWLANsecrymode": ruijieWLANsecrymode,
       "ruijiestaticweplength": ruijiestaticweplength,
       "ruijie8021xweplength": ruijie8021xweplength,
       "ruijieWPAenabled": ruijieWPAenabled,
       "ruijieWPAPairwisecipher": ruijieWPAPairwisecipher,
       "ruijieWPAakmmode": ruijieWPAakmmode,
       "ruijieWPApskPassPhrase": ruijieWPApskPassPhrase,
       "ruijieWLANsecry80211i": ruijieWLANsecry80211i,
       "ruijieWAPIasuIpaddress": ruijieWAPIasuIpaddress,
       "ruijieWAPIcertificateformat": ruijieWAPIcertificateformat,
       "ruijieWAPImsrekeyClientoff": ruijieWAPImsrekeyClientoff,
       "ruijieWAPIimportcertificate": ruijieWAPIimportcertificate,
       "ruijieWAPIcacertificatename": ruijieWAPIcacertificatename,
       "ruijieWAPIlocalcertificatename": ruijieWAPIlocalcertificatename,
       "ruijieWAPIascertificatename": ruijieWAPIascertificatename,
       "ruijieRSNenabled": ruijieRSNenabled,
       "ruijieRSNPairwisecipher": ruijieRSNPairwisecipher,
       "ruijieRSNakmmode": ruijieRSNakmmode,
       "ruijieRSNpskPassPhrase": ruijieRSNpskPassPhrase,
       "ruijieWEPAuthenAlgorithm": ruijieWEPAuthenAlgorithm,
       "ruijieWLANsecurityStatus": ruijieWLANsecurityStatus,
       "ruijieACauthenMethodsupport": ruijieACauthenMethodsupport,
       "ruijieWLANEAPAuthenSupport": ruijieWLANEAPAuthenSupport,
       "ruijieWEPDefaultKeysTable": ruijieWEPDefaultKeysTable,
       "ruijieWEPDefaultKeysEntry": ruijieWEPDefaultKeysEntry,
       "ruijieWEPDefaultKeyIndex": ruijieWEPDefaultKeyIndex,
       "ruijieWEPDefaultKeyValue": ruijieWEPDefaultKeyValue,
       "ruijieWEPDefaultKeyLength": ruijieWEPDefaultKeyLength,
       "ruijieWlansecurityMIBConform": ruijieWlansecurityMIBConform,
       "ruijieWlansecurityMIBCompliances": ruijieWlansecurityMIBCompliances,
       "ruijieWlansecurityMIBCompliance": ruijieWlansecurityMIBCompliance,
       "ruijieWlansecurityMIBGroups": ruijieWlansecurityMIBGroups,
       "ruijieWlansecuritycofigGroup": ruijieWlansecuritycofigGroup,
       "ruijieWEPDefaultKeysGroup": ruijieWEPDefaultKeysGroup,
       "ruijieWlansecurityTrapGroup": ruijieWlansecurityTrapGroup,
       "ruijieWlansecurityTrapvar": ruijieWlansecurityTrapvar,
       "ruijieWlansecurityWepDecrytEnableTrapVar": ruijieWlansecurityWepDecrytEnableTrapVar,
       "ruijieWlansecurityDeviceMAC": ruijieWlansecurityDeviceMAC}
)
